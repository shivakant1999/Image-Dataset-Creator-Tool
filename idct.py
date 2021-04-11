import os
from tkinter import *
from tkinter import messagebox
class tool():
    def __init__(self, root):
        self.root = root
        self.root.title("IMAGE DATASET CREATOR TOOL")
        self.root.geometry("1000x550+200+70")
        self.root.resizable(False, False)
        self.root.config(bg="skyblue")
        title = Label(self.root, text="IMAGE DATASET CREATOR TOOL", font=("Gaudy Old Style", 40)).place(x=0, y=0, relwidth=1)

        Text = Label(self.root, text="This is a python application to help you create your own image dataset, for custom machine learning \n projects such as Face Recognition System for a friend or for a particular company, Advanced AI\n powered attendance management system that requires specific dataset. which can be really difficult  \n to create some times. Thus, this tool can be become handy in that case.", font=("Helvetica", 16,"italic"), bg="#d8f2e8").place(x=18, y=120)

        About = Label(self.root, text="About", font=("times new roman", 24, "bold"), fg="red", bg="skyblue").place(x=450, y=70)


        def webcam(): 
            # newWindow = Toplevel(root) 
            # newWindow.focus_force() 
            # newWindow.grab_set()
            os.system('python webcam.py')
        

        def internet(): 
            # newWindow = Toplevel(root) 
            # newWindow.focus_force()
            # newWindow.grab_set()
            os.system('python img_dwld.py')
        

        def vid(): 
            os.system('python conv.py')
            # Popen('python conv.py')
            # call(["python", "conv.py"])


        def Exit_app():
            """
            This function will App and close the application
            """
            mess = messagebox.askyesno("Exit", "Do You Really Want to Exit ?")
            if mess > 0:
                root.destroy()    


        f2 = LabelFrame(self.root, bd=8, relief=GROOVE, font=("times new roman", 14, "bold"), fg="#C70039", bg="#f2ffc4")
        f2.place(x=70, y=250, width=250, height=200)
        text1 = Label(f2, text="Use this option to \ncreate your datset using \nyour webcam", font=('times new roman', 15, "bold"), bg="#f2ffc4").place(x=8, y=20)
        btn = Button(f2, text ="Webcam", font=("Gaudy Old Style", 12, "bold"), bg="#eaff63" , command = webcam).place(x=80, y=120)


        f3 = LabelFrame(self.root, bd=8, relief=GROOVE, font=("times new roman", 14, "bold"), fg="#C70039", bg="#f2ffc4")
        f3.place(x=370, y=250, width=250, height=200)
        text2 = Label(f3, text="Use this option to \ncreate your datset using \nvideo", font=('times new roman', 15, "bold"), bg="#f2ffc4").place(x=8, y=20)
        btn1 = Button(f3, text ="Video", font=("Gaudy Old Style", 12, "bold"), bg="#eaff63", command = vid).place(x=90, y=120)

        f4 = LabelFrame(self.root, bd=8, relief=GROOVE, font=("times new roman", 14, "bold"), fg="#C70039", bg="#f2ffc4")
        f4.place(x=670, y=250, width=250, height=200)
        text3 = Label(f4, text="Use this option to \ncreate your datset by \ndownloading images from \n internet via downloader", font=('times new roman', 15, "bold"), bg="#f2ffc4").place(x=8, y=12)
        btn1 = Button(f4, text ="Internet", font=("Gaudy Old Style", 12, "bold"), bg="#eaff63", command = internet).place(x=80, y=120)


        abt = Label(self.root, text="Developed By: Shivakant Vishwakarma", font=("times new roman", 14, "bold"), fg="red", bg="skyblue").place(x=350, y=460)
        exit_btn = Button(self.root, text="EXIT", command=Exit_app , font=("times new roman", 14, "bold") , bg="cadetblue", fg="yellow", bd=5).place(x=480, y=490)


root = Tk()
obj = tool(root)
root.mainloop()
