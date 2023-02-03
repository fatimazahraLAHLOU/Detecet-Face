import cv2
from tkinter import *

from numpy import test


class FaceDetector:

    def _init_(self, master):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.webcam = cv2.VideoCapture(0)
        self.webcam.set(3, 640)
        self.webcam.set(4, 480)
        self.master = master
        self.master.title("𝔽𝕒𝕔𝕖 𝔻𝕖𝕥𝕖𝕔𝕥")
        self.master.geometry("640x480")
        self.label = Label(master)
        self.label.pack()
        self.timer = master.after(5, self.update_frame)

    def update_frame(self):
        ret, frame = self.webcam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        self.display_image(frame)
        self.timer = self.master.after(5, self.update_frame)

    def display_image(self, img):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        assert isinstance(test.jpg)
        img:test.jpg = test.PhotoImage(test=img)
        self.label.imgtk = img
        self.label.configure(test=img)

        class FaceDetector:
            def __init__(self, root):
                self.root = root


#root = Tk()
#face_detector = FaceDetector(root)
#root.mainloop()