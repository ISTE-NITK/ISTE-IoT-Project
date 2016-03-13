from Tkinter import *


class IOTButtons:

	def __init__(self, master):		#__init__ gets called automatically whenever you create an object
									#self for most classes, master for gui. 
									#Master means root or main window (same thing, different names just to differentiate btwn variables)
		frame= Frame(master)		#we created a frame in the main window
		frame.pack()

		self.printButton = Button(frame, text="Print Message", command=self.printMessage)	#call a certain func when button is clicked
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text="Quit", command=frame.quit)	#frame.quit is an inbuilt function to break the main loop, ie quit
		self.quitButton.pack(side=LEFT)

	def printMessage(self):			#whenever we create an object from class IOTButtons, it throws this object in there
		print("Wow this actually worked")

root= Tk() #blank window
b = IOTButtons(root)	#object allows us to access stuff inside the class
						#any time we want to use something from a class, we need to make an object
root.mainloop


'''
label_1 = Label(root, text='Username')
label_2 = Label(root, text='Password')
entry_1 = Entry(root)			#entry from the user
entry_2 = Entry(root)


label_1.grid(row=0,sticky=E)	#this sticks the labels EAST 				
label_2.grid(row=1,sticky=E)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c = Checkbutton(root, text="Keep me logged in")	#literally a checkbutton
c.grid(columnspan=2)



def leftclick(event):			#event is something the user can do
	print("LEFT")

def middleclick(event):
	print("MIDDLE")

def rightclick(event):
	print("RIGHT")

frame= Frame(root, width=300, height=250)	#one widget handling multiple events
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightclick)
frame.pack()
#time for widgets! This is GUI part one, ie making our layout

#button1= Button(root, text="Button 1", command=leftclick) #binding a function to a widget
#button1.bind("<Button-1>")	#binds a button click to the button
#button2= Button(frame, text="Button 4", fg="purple")		#where to put it, what do you want to put in it, color of button

#time for part two: packing! We use this to display our widgets
#button1.pack(side= LEFT) #pack stacks blocks on top of each other by default

#button2.pack(side= TOP)
'''



root.mainloop()		#window should be on screen continuously until we close it. Thus we use an infinite loop 