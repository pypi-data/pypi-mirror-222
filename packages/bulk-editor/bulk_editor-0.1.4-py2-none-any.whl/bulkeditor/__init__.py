from PIL import Image as ImageEdit
from PIL import ImageFont, ImageDraw 
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import pkg_resources
import os
from tkinter import Tk, Label, Button, filedialog, messagebox, Text, INSERT



import cv2

'''
todo: 
4. Code architecture and code clean
5. Make it as a Compiler package
'''

class GetImageAxisAndCreateImage:
	
	def createImage(self,path,x,y, fontColor):
		directory_to_save = filedialog.askdirectory()
		fontFilePath = pkg_resources.resource_filename(__name__, 'Roboto-Bold.ttf')
		certificateFont= ImageFont.truetype(fontFilePath, 42)
		textFile = pkg_resources.resource_filename(__name__, 'Certificate.txt')
		nameList=[]
		certificateName = []
		file = open(textFile, "r")
		nameList = file.readlines()
		file.close
		for i in nameList:
			certificateName.append(i.replace("\n","").strip())
		for i in certificateName:
			certificateImage = ImageEdit.open(path) 
			editableImage = ImageDraw.Draw(certificateImage)    
			editableImage.text((x,y-30),i,fontColor,font=certificateFont)
			certificateImage.save(directory_to_save +"/"+ i.strip()+".png")
		messagebox.showinfo("Information", "File created succesfully")
		cv2.destroyAllWindows()
	
	def select_color(self, path, x, y):
		global fontColor
		fontColor = askcolor(title="Choose color for the text")
		print(fontColor) 

		if messagebox.askquestion("Form", "Confirm color and proceed") == "yes":
			self.createImage(path,x,y, fontColor[0])


	def Submit(self,path,x,y):
		if messagebox.askquestion("Form", "Confirm position") == "yes":
			self.select_color(path=path,x=x, y=y)


	def click_event(self, event, x, y, flags, params):
		# checking for left mouse clicks
		if event == cv2.EVENT_LBUTTONDOWN:

			# displaying the coordinates
			# on the Shell
			print(x, ' ', y)
			img = cv2.imread(params, 1)

			# displaying the coordinates
			# on the image window
			font = cv2.FONT_HERSHEY_COMPLEX
			cv2.putText(img,"Your text will lie here", (x,y), font,
					1, (255, 0, 0), 2)
			
			cv2.imshow('DoSmartie - Bulk Image Editor', img)
			self.Submit(params,x,y)

		# checking for right mouse clicks	
		if event==cv2.EVENT_RBUTTONDOWN:

			# displaying the coordinates
			# on the Shell
			print(x, ' ', y)
			self.Submit(params,x,y)
		
	def __init__(self, path) -> None:
		cv2.namedWindow("DoSmartie - Bulk Image Editor", cv2.WINDOW_NORMAL)
		img = cv2.imread(path, 1)
		cv2.imshow('DoSmartie - Bulk Image Editor', img)
		cv2.setMouseCallback('DoSmartie - Bulk Image Editor', self.click_event, path)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

class BulkEditor:

	def select_image(self):
		global windowA, windowB
		textFile = pkg_resources.resource_filename(__name__, 'Certificate.txt')
		self.text = self.textField.get("1.0", "end-1c")
		with open(textFile, 'w') as file:
			file.write(self.text)
		path = filedialog.askopenfilename()
		if len(path) > 0:
			image = GetImageAxisAndCreateImage(path)


	def __init__(self):
		root = Tk()
		root.title("DoSmartie - Bulk edit images")
		logoFilePath = pkg_resources.resource_filename(__name__, 'logo.png')
		ico =  ImageEdit.open(logoFilePath)
		photo = ImageTk.PhotoImage(ico)
		root.wm_iconphoto(False, photo)
		root.geometry("360x360")  
		heading = Label(root, text="Enter the data to be added")
		label = Label(root, text="Each image will be created from a single line of text.")
		self.textField = Text(root, height = 24, width = 52)
		panelA = None
		panelB = None
		btn = Button(root, text="Select an image", command=self.select_image)
		pdf_btn = Button(root, text="Image to PDF generator", command=ImageToPdf)
		pdf_btn.pack(side="bottom", fill="both", expand="no", padx="10", pady="10")
		btn.pack(side="bottom", fill="both", expand="no", padx="10", pady="15")
		heading.pack()
		label.pack()
		self.textField.pack()
		root.mainloop()


class ImageToPdf:
    source_directory = ""
    destination_directory = ""
    def sourceDirectory(self):
        self.source_directory = filedialog.askdirectory()
        print(self.source_directory)
        self.textField_source.insert("1.0", self.source_directory)
    
    def destinationDirectory(self):
        self.destination_directory = filedialog.askdirectory()
        print(self.destination_directory)
        self.textField_destination.insert("1.0", self.destination_directory)

    def __init__(self):
        img_root = Tk()
        img_root.title("DoSmartie - Image to Pdf Convertor")
        title1 = Label(img_root, text="Convert png, jpg & jpeg files to pdf in bulk")
        description_source = Label(img_root, text="Select your source directory containing images")
        self.textField_source = Text(img_root, height = 3, width = 52)
        btn_browse1 = Button(img_root, width=12, height=1, text="Browse...", command=lambda: self.sourceDirectory())
        description_destination = Label(img_root, text="Select your destination directory to save the PDF")
        self.textField_destination = Text(img_root, height = 3, width = 52)
        btn_browse2 = Button(img_root, width=12, height=1, text="Browse...", command=lambda: self.destinationDirectory())
        spacer = Label(img_root, text="                                   ")
        btn_confirm = Button(img_root, width=15, height=3, text="Convert", command=lambda:self.convertToPdf(self.source_directory, self.destination_directory))
        img_root.geometry("500x360")
        
        
        title1.pack()
        description_source.pack()
        self.textField_source.pack()
        btn_browse1.pack()
        description_destination.pack()
        self.textField_destination.pack()
        btn_browse2.pack()
        spacer.pack()
        btn_confirm.pack()
        img_root.mainloop()

    def convertToPdf(self, directory, destination_directory):
        for files in os.listdir(directory):
            if files.split(".")[-1] in ('png', 'jpg', 'jpeg'):
                print(files.split(".")[-1], end = " ")
                print(files)
                image = ImageEdit.open(os.path.join(directory, files))
                converted_image = image.convert('RGB')
                converted_image.save(os.path.join(destination_directory, '{0}.pdf'.format(files.split(".")[-2])))
        messagebox.showinfo("Information", "File created succesfully")
        

