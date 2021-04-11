from random import randint
from tkinter import*
from tkinter import font
from tkinter.messagebox import showerror, showinfo
from typing import Collection
from tkinter import messagebox, filedialog, ttk
import math, random, os
from bs4 import BeautifulSoup
import requests
   
            
folder =""
# ================ functions ============
def openLocation():
    global folder
    folder = filedialog.askdirectory(title="Select Folder to save image")
    if(len(folder) > 1):
        print("Selected folder is:"+folder)
    else:
        messagebox.showerror("Error", "Please Select Folder!")

def Exit_app():
        """
        This function will destroy Bill App and close the application
        """
        mess = messagebox.askyesno("Exit", "Do You Really Want to Exit ?")
        if mess > 0:
            root.destroy()

Google_Image= 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
} #write: 'my user agent' in browser to get your browser user agent details
# ==================== APP DESIGN ==================
class image_scraper:
    def download_images(self):
        self.key = self.keyword.get()
        self.number = self.num.get()
        data = self.key
        num_images = int(self.number)
        global u_agnt
        print('Searching Images....')
        global Google_Image
        search_url = Google_Image + 'q=' + data #'q=' because its a query
        
        # request url, without u_agnt the permission gets denied
        response = requests.get(search_url, headers=u_agnt)
        html = response.text #To get actual result i.e. to read the html data in text mode
        
        # find all img where class='rg_i Q4LuWd'
        b_soup = BeautifulSoup(html, 'html.parser') #html.parser is used to parse/extract features from HTML files
        results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
        
        #extract the links of requested number of images with 'data-src' attribute and appended those links to a list 'imagelinks'
        #allow to continue the loop in case query fails for non-data-src attributes
        count = 0
        imagelinks= []
        for res in results:
            try:
                link = res['data-src']
                imagelinks.append(link)
                count = count + 1
                if (count >= num_images):
                    break
                
            except KeyError:
                continue
        
        print(f'Found {len(imagelinks)} images')
        print('Start downloading...')

        for i, imagelink in enumerate(imagelinks):
            # open each image link and save the file
            response = requests.get(imagelink)
            
            imagename = folder + '/' + data + str(i+1) + '.jpg'
            with open(imagename, 'wb') as file:
                file.write(response.content)

        print('Download Completed!')
        messagebox.showinfo("message", "Download Complete!")

    def __init__(self, root):
        self.root = root
        self.root.geometry("600x450+400+100")
        self.root.resizable(False, False)
        self.root.focus_force()
        self.root.grab_set()
        self.root.title("Image Downloader")
        bg_color = "#d7fca7"
        G_font = ("calibri body", 12, "bold")
        title = Label(self.root, text="Image Downloader", bd=8, relief=FLAT, bg=bg_color , fg="black", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

# =========== Variables =============
        self.keyword = StringVar()
        self.num = IntVar()
    
# ======================= " Search Box" ==========================

        f1 = LabelFrame(self.root, bd=8, relief=GROOVE, text=" Search Box ", font=("times new roman", 12, "bold"), fg="#C70039", bg=bg_color)
        f1.place(x=0, y=68, relwidth=1)

        keyword_label = Label(f1, text="What you want to Download (Ex. Cat)",bg=bg_color, fg="black" , font=G_font).grid(row=0, column=0, padx=20, pady=5)
        keyword_txt = Entry(f1, width=16, textvariable=self.keyword, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        num_label = Label(f1, text="Number of Images (Ex. 10)",bg=bg_color, fg="black" , font=G_font).grid(row=1, column=0, padx=20, pady=5)
        num_txt = Entry(f1, width=16, font="arial 15", textvariable=self.num , bd=7, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=50)

        folder = Label(f1, text="Where to download images",bg=bg_color, fg="black" , font=G_font).grid(row=2, column=0, padx=20, pady=5)
        bill_btn = Button(f1, text="Select", command=openLocation , font="arial 12 bold", bg="yellow").grid(row=2, column=1, pady=10, padx= 20)

# ================== Download Button ==============
        down = Label(self.root)
        down.place(y=260)
        down_btn = Button(down, text="Download", command=self.download_images, font=("times new roman", 12, "bold") , bg="red", fg="yellow", bd=5).grid(padx=250)
        dest = Label(self.root, font=("times new roman", 14, "bold"), fg="#C70039")
        dest.place(y=350)
        # ================== Exit Button ==================        
        exit_btn = Button(dest, text="EXIT",command=Exit_app, font=("times new roman", 12, "bold") , bg="cadetblue", fg="yellow", bd=5).grid()

# ================== about section ================        
        abt = Label(dest, text="Developed By: Shivakant Vishwakarma", font=("times new roman", 13, "bold"), fg="#17202A").grid(padx=140, pady=10, sticky="w")


        # user can input a search keyword and the count of images required
        # download images from google search image

        # The User-Agent request header contains a characteristic string 
        # that allows the network protocol peers to identify the application type, 
        # operating system, and software version of the requesting software user agent.
        # needed for google search


    
root = Tk()
obj = image_scraper(root)
root.mainloop()