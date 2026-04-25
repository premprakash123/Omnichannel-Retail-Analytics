import requests
import datetime
import os
import threading
import tkinter as tki
import tkinter.messagebox as Messagebox
import time
import yagmail
import csv
import cv2
from PIL import Image
from PIL import ImageTk
import pandas as pd
global attendance
col_names = ['Vehicle Number', 'Date', 'Time']
attendance = pd.DataFrame(columns=col_names)

class PhotoBoothApp:
        def __init__(self, vs, outputPath):
            # store the video stream object and output path, then initialize
            # the most recently read frame, thread for reading frames, and
            # the thread stop event
            self.vs = vs
            self.outputPath = outputPath
            self.frame = None
            self.thread = None
            self.stopEvent = None
            # initialize the root window and image panel
            self.root = tki.Tk()
            self.panel = None

            # create a button, that when pressed, will take the current
            # frame and save it to file
            btn = tki.Button(self.root, text="Take Image",font=('times', 15, ' bold '),
                             command=self.takeSnapshot)
            btn.place(x=850,y=600)
            btn1 = tki.Button(self.root, text="Email", font=('times', 15, ' bold '),
                             command=self.email)
            btn1.place(x=1000, y=600)
            # start a thread that constantly pools the video sensor for
            # the most recently read frame
            self.stopEvent = threading.Event()
            self.thread = threading.Thread(target=self.videoLoop, args=())
            self.thread.start()
            # set a callback to handle when the window is closed
            self.root.wm_title("PhotoBooth")
            self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)
            print("check")


        def videoLoop(self):
            # DISCLAIMER:
            # I'm not a GUI developer, nor do I even pretend to be. This
            # try/except statement is a pretty ugly hack to get around
            # a RunTime error that Tkinter throws due to threading
            try:
                # keep looping over frames until we are instructed to stop
                while not self.stopEvent.is_set():

                    self.frame = self.vs.read()

                    # OpenCV represents images in BGR order; however PIL
                    # represents images in RGB order, so we need to swap
                    # the channels, then convert to PIL and ImageTk format
                    image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                    image = Image.fromarray(image)
                    image = ImageTk.PhotoImage(image)

                    # if the panel is not None, we need to initialize it
                    if self.panel is None:
                        self.panel = tki.Label(image=image)
                        self.panel.image = image
                        self.panel.pack(side="left", padx=10, pady=10)

                    # otherwise, simply update the panel
                    else:
                        self.panel.configure(image=image)
                        self.panel.image = image

            except RuntimeError as e:
                    print("[INFO] caught a RuntimeError")


        def takeSnapshot(self):
            # grab the current timestamp and use it to construct the
            # output path
            global attendance
            ts = datetime.datetime.now()
            filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
            p = os.path.sep.join((self.outputPath, filename))
            print(self.outputPath)
            # save the file
            cv2.imwrite(p, self.frame.copy())
            print("[INFO] saved {}".format(filename))
            img = cv2.imread(p)

            img = cv2.resize(img, (320, 320))
            cv2.imshow("image_Output",img)
            time.sleep(2)
            regions = ['in', 'it']  # Change to your country
            with open("C:/Users/user/numberplate/Vehicle1/" + filename, 'rb') as fp:
                response = requests.post(
                    'https://api.platerecognizer.com/v1/plate-reader/',
                    data=dict(regions=regions),  # Optional
                    files=dict(upload=fp),
                    headers={'Authorization': 'Token 0679d4a079f0e38ebf3b404cc43bfed101a9377e'})
            result = response.json()
            result1 = result['results'][0]['plate']
            print(result1)
            result1 = result1.upper()
            message1 = tki.Label(self.root, text="Numberplate", fg="black", width=10, height=2,
                                 font=('times', 20, 'italic bold'))
            message1.place(x=950, y=30)
            message = tki.Label(self.root, text=result1, bg="white", fg="black", width=20, height=2,
                                font=('times', 20, 'italic bold'))
            message.place(x=850, y=100)

            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            attendance.loc[len(attendance)] = [result1, date, timeStamp]
            attendance = attendance.drop_duplicates(subset=['Vehicle Number'], keep='first')
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            Hour, Minute, Second = timeStamp.split(":")
            fileName = "Vehicle" + os.sep + "Vehicle_" + date + ".csv"
            attendance.to_csv(fileName, index=False, mode='a')
            print("Vehicle detailed Successful Saved")

        def email(self):

            date = datetime.date.today().strftime("%B %d, %Y")
            path = 'Vehicle'
            os.chdir(path)
            files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
            newest = files[-1]
            filename = newest
            sub = "Vehicle Report for " + str(date)
            # mail information
            yag = yagmail.SMTP(user="prinshu693@gmail.com", password='99814919')
            body = "kindly Find Attachment"
            # sent the mail
            yag.send(
                to="devdhar1953@gmail.com",
                subject=sub,  # email subject
                contents=body,  # email body
                attachments=filename  # file attached
            )
        def onClose(self):
            # set the stop event, cleanup the camera, and allow the rest of
            # the quit process to continue
            print("[INFO] closing...")
            self.stopEvent.set()
            self.vs.stop()
            self.root.quit()
