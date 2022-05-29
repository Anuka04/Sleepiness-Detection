from tkinter import *
import os

def detection1():
	root = Tk()
	root.configure(background = "black")

	def run(): 
		os.system("python sleepiness_detection.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()
		
	root.title("DETECTION")
	Label(root, text="SLEEPINESS DETECTION",font=("courier",24),fg="black",bg="#87CEEB",height=2).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=5)
	Button(root,text="RUN",font=("courier new",25),bg="white",fg='black',command=run).grid(row=5,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
	Button(root,text="CLOSE",font=("courier new",25),bg="white",fg='black',command=root.destroy).grid(row=9,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)

	root.mainloop()