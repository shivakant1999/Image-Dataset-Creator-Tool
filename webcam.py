import os
import cv2
from tkinter import *
from tkinter import messagebox, filedialog, ttk
class webcam():
    def __init__(self, root):
        self.root = root
        self.root.title("Webcam dataset creator")
        self.root.geometry("1000x550+200+70")
        self.root.resizable(False, False)
        self.root.config(bg="skyblue")
        title = Label(self.root, text="WEBCAM DATASET CREATOR", font=("Gaudy Old Style", 40)).place(x=0, y=0, relwidth=1)

        About = Label(self.root, text="Note:", font=("times new roman", 16, "italic"), fg="red", bg="skyblue").place(x=70, y=80)

        Text = Label(self.root, text="This is a python application to help you create your own image dataset, for custom machine learning projects \nsuch as Face Recognition System for a friend or for a particular company, Advanced AI powered attendance \nmanagement system that requires specific dataset. which can be really difficult to create some times. \nThus, this tool can be become handy in that case.", font=("times new roman", 14,"bold"), bg="skyblue", fg="#5e0941").place(x=70, y=110)

    
        def Exit_app():
                    """
                    This function will destroy App and close the application
                    """
                    mess = messagebox.askyesno("Exit", "Do You Really Want to Exit ?")
                    if mess > 0:
                        root.destroy()
        #folder = ""
        def openLocation():
            global folder
            folder = filedialog.askdirectory(title="Select Folder to save image")
            fold = folder
            if(len(folder) > 1):
                print("Selected folder is:"+folder)
            else:
                messagebox.showerror("Error", "Please Select Folder!")

        
        def record():
            global folder
            path = folder
            print(path)
            if path == str(""):
                messagebox.showinfo("Error", "Please Select folder")
            else:
                cap = cv2.VideoCapture(0)

            # print("folder is "+str(folder))
            # Define the codec and create VideoWriter object

                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(folder+str('/video.mp4'),fourcc, 10.0, (640,480))

            # loc = os.path.abspath("video.mp4")

                while(cap.isOpened()):
                    ret, frame = cap.read()
                    if ret==True:

                    # write the frame
                        out.write(frame)

                        cv2.imshow('frame',frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    else:
                        break

            # Release everything if job is finished
                cap.release()
                out.release()
                cv2.destroyAllWindows()

        folder = Label(self.root, text="Select folder where to save images",bg="skyblue", fg="black" , font=("times new roman", 14 ,"bold")).place(x=150, y=370)
        
        f_btn = Button(self.root, text="Select", command=openLocation , font=("times new roman", 12 ,"bold"), bg="#eb4272").place(x=450, y=370)

        save = Button(self.root, text="Record", command=record, font=("times new roman", 14, "bold") , bg="#edfc9f", fg="red").place(x=630, y=368)

        txt = Label(self.root, text="How to start recording ?", font=("times new roman", 14, "bold", "italic"), fg="red", bg="skyblue").place(x=400, y=240)

        Text1 = Label(self.root, text="When you're ready, press record button to start recording your video and when done recording (minimum 5 seconds)\n then press 'q' to stop recording. Rest of the process is automatic.", font=("times new roman", 13,"bold", "italic"), fg="black", bg="skyblue").place(x=105, y=280)


        abt = Label(self.root, text="Developed By: Shivakant Vishwakarma", font=("times new roman", 14, "bold"), fg="red", bg="skyblue").place(x=350, y=510)
        exit_btn = Button(self.root, text="EXIT", command=Exit_app , font=("times new roman", 14, "bold") , bg="cadetblue", fg="yellow", bd=5).place(x=480, y=460)

root = Tk()
obj = webcam(root)
root.mainloop()