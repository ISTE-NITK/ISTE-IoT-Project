from Tkinter import *

root= Tk() #blank window

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

'''
topframe= Frame(root)
topframe.pack()
bottomframe= Frame(root)
bottomframe.pack(side=BOTTOM)

#time for widgets! This is GUI part one, ie making our layout
button1= Button(topframe, text="Button 1", fg="red") #where to put it, what do you want to put in it, color of button
button2= Button(topframe, text="Button 2", fg="blue")
button3= Button(topframe, text="Button 3", fg="green")
button4= Button(bottomframe, text="Button 4", fg="purple")

#time for part two: packing! We use this to display our widgets
button1.pack(side= LEFT) #pack stacks blocks on top of each other by default
button2.pack(side= LEFT)
button3.pack(side= LEFT) #packs as far left as possible
button4.pack(side= TOP)
'''

root.mainloop()		#window should be on screen continuously until we close it. Thus we use an infinite loop 