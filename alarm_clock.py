from time import strftime
import tkinter as tk
import pygame



#BACK
alarm_clocks = []
pygame.mixer.init()

def set_clock():
	clock.config(text = strftime("%H:%M:%S"))
	clock.after(1000,set_clock)


def set_alarm_clock(hour, minute):
	alarm_clocks.append({"hour":hour, "minute":minute})
	active_alarm()

def active_alarm():
	alarm_clock = "{}:{}:00".format(alarm_clocks[0]["hour"],alarm_clocks[0]["minute"])
	if alarm_clock == strftime("%H:%M:%S"):
		alarm.config(text = alarm_clock)
		pygame.mixer.music.load("osg_S_065.mp3")
		pygame.mixer.music.play(loops = 2)
		btn_stop_alarm.place(x = 325, y = 200)
	btn_set_alarm.after(1000,active_alarm)

def stop_alarm():
	pygame.mixer.music.stop()




#FRONT
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("500x250")
root.resizable(0,0)
root.config(bg = "black")

#LABEL
clock = tk.Label(root, bg = "black", fg = "white", font = "arial 50 bold")
clock.pack()
set_clock()

alarm = tk.Label(root, bg = "black", fg = "green", font = "arial 50 bold")
alarm.pack()

#ENTRY
hour = tk.Entry(root, width = 2, bg = "black", fg = "green", font = "arial 30")
hour.place(x = 195, y = 135)

minute = tk.Entry(root, width = 2, bg = "black", fg = "green", font = "arial 30")
minute.place(x = 255, y = 135)

#BUTTON
btn_set_alarm = tk.Button(root, text = "Set Alarm", command = lambda: set_alarm_clock(hour.get(),minute.get()))
btn_set_alarm.place(x = 100, y = 200)

btn_stop_alarm = tk.Button(root, text = "Stop Alarm", command = stop_alarm)


root.mainloop()

