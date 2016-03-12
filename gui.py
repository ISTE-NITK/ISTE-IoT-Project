from Tkinter import *

root= Tk() #blank window

#thelabel= Label(root, text='This is very easy.')
#thelabel.pack() 

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

root.mainloop()		#window should be on screen continuously until we close it. Thus we use an infinite loop 