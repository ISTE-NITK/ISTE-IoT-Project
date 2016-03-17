from Tkinter import *

root=Tk()

#**************		BODY	************
label_1=Label(root, text="Node 1").grid(row=0, sticky= E)
label_2=Label(root, text="Node 2").grid(row=1, sticky= E)
label_3=Label(root, text="Node 3").grid(row=2, sticky= E)

entry_1_x=Entry(root).grid(row=0, column=1, padx=2, pady=2)
entry_1_y=Entry(root).grid(row=0, column=2, padx=2, pady=2)
entry_2_x=Entry(root).grid(row=1, column=1, padx=2, pady=2)
entry_2_y=Entry(root).grid(row=1, column=2, padx=2, pady=2)
entry_3_x=Entry(root).grid(row=2, column=1, padx=2, pady=2)
entry_3_y=Entry(root).grid(row=2, column=2, padx=2, pady=2)


#***************************************
root.mainloop()