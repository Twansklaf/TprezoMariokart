from Tkinter import *
from time import sleep


file = open("billboard.txt", "r")
arrived_cars = []

wind = Tk()
txt = []
can = Canvas(wind, width=600, height=900, background="white")

def scan_bb() :
	cars = file.readlines()
	for c in cars :
		if not c in arrived_cars :
			arrived_cars.append(c.replace('\n', '').split(":"))
			txt.append(can.create_text(0, 70 + 70*(len(arrived_cars)-1), text=arrived_cars[-1][0], font="Arial 16", fill="black", anchor=W))
			can.pack()
	# print(arrived_cars)

	wind.after(500, scan_bb)


def disp() :

	# photo = PhotoImage(file="gtr.gif")
	# photo.zoom(0.5, 0.5)
	# can.create_image(40, 20, anchor=NW, image=photo)
	can.pack()
	wind.after(2000,scan_bb)
	wind.mainloop()

disp()