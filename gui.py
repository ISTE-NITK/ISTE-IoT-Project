from Tkinter import *

def moveNode1():
	e1_x = int(i1_1.get())
	e1_y = int(i1_2.get())
	#disp = Label(root, text="%s" %e1_x).grid(row=10,column=10)
	node1=Button(root, text= 'Node One').grid(row=e1_x, column=e1_y, padx = 2, pady = 2)		#this works with constants but is unresponsive to my variables. WHY?
	return()
'''
def moveNode2():
	node2=Button(root, text= 'Node Two').grid(row=e2_x, column=e2_y, padx = 2, pady = 2)
	return

def moveNode3():
	node3=Button(root, text= 'Node Three').grid(row=e3_x, column=e3_y, padx = 2, pady = 2)		#make one function. needless waste of space and adds complexity
	return
'''
root=Tk()
#root.geometry('450x450 +500 +300')
root.title("IOT GUI ")
#**************		BODY	************

label_1 = Label(root, text = "Node 1:	").grid(row = 0, sticky = E)
label_2 = Label(root, text = "Node 2:	").grid(row = 1, sticky = E)
label_3 = Label(root, text = "Node 3:	").grid(row = 2, sticky = E)

i1_1 = StringVar()
e1_1 = Entry(root,textvariable=i1_1).grid(row = 0, column = 1, padx = 2, pady = 2)


i1_2 = StringVar()
e1_2 = Entry(root,textvariable=i1_2).grid(row = 0, column = 2, padx = 2, pady = 2)

'''
i2_1 = StringVar()
e2_1 = Entry(root,textvariable = i2_1).grid(row = 1, column = 1, padx = 2, pady = 2)
e2_x = int(i1_2.get())

i2_2 = StringVar()
e2_2 = Entry(root,textvariable = i2_2).grid(row = 1, column = 2, padx = 2, pady = 2)
e2_y = int(i1_2.get())

i3_1 = StringVar()
e3_1 = Entry(root,textvariable = i3_1).grid(row = 2, column = 1, padx = 2, pady = 2)
e3_x = int(i1_2.get())

i3_2 = StringVar()
e3_2 = Entry(root,textvariable = i3_2).grid(row = 2, column = 2, padx = 2, pady = 2)
e3_y = int(i1_2.get())
'''

button_1 = Button(root, text = "Submit",command = moveNode1).grid(row = 0, column = 3, padx = 2, pady = 2)
#button_2 = Button(root, text = "Submit",command = moveNode2).grid(row = 1, column = 3, padx = 2, pady = 2)
#button_3 = Button(root, text = "Submit",command = moveNode3).grid(row = 2, column = 3, padx = 2, pady = 2)

#***************************************
root.mainloop()