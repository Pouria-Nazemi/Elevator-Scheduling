from tkinter import *

floors = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15"
]

root = Tk()
root.title("Elevator Algorithm")
root.geometry("600x530")
# root.resizable(False, False)

# --------------------------------------------------------------------------------------------------------------
# Elevator 1
ele1_label = Label(root, bg='red', width=200, height=350)
ele1_label.place(x=0, y=0)
ele1_text = Label(root, text='Elevator 1', bg='white', font=('Cursive', 16, 'bold'))
ele1_text.place(x=50, y=5)

ele1_floorNumber = StringVar()
ele1_floorLabel = Label(root, textvariable=ele1_floorNumber, bg='red', font=('Cursive', 16, 'bold'))
ele1_floorLabel.place(x=50, y=50)
ele1_floor = 1
ele1_floorNumber.set(f"Floor: {ele1_floor}")


def ele1_showLabel():
    if ele1_floorList.get() != 'Floors':
        ele1_selectedFloorLabel.config(text=f'{ele1_floorList.get()} is selected')
        print(ele1_floorList.get())


ele1_selectedFloorLabel = Label(root, text="Select Floor")
ele1_selectedFloorLabel.place(x=50, y=100)

ele1_floorList = StringVar()
ele1_floorList.set("Floors")
drop = OptionMenu(root, ele1_floorList, *floors)
drop.place(x=20, y=130)

ele1_clickBtn = Button(root, text="click", command=ele1_showLabel)
ele1_clickBtn.place(x=120, y=132)

# --------------------------------------------------------------------------------------------------------------
# Elevator 2
ele2_label = Label(root, bg='green', width=200, height=350)
ele2_label.place(x=200, y=0)
ele2_text = Label(root, text='Elevator 2', bg='white', font=('Cursive', 16, 'bold'))
ele2_text.place(x=250, y=5)

ele2_floorNumber = StringVar()
ele2_floorLabel = Label(root, textvariable=ele2_floorNumber, bg='green', font=('Cursive', 16, 'bold'))
ele2_floorLabel.place(x=250, y=50)
ele2_floor = 6
ele2_floorNumber.set(f"Floor: {ele2_floor}")


def ele2_showLabel():
    if ele2_floorList.get() != 'Floors':
        ele2_selectedFloorLabel.config(text=f'{ele2_floorList.get()} is selected')
        print(ele2_floorList.get())


ele2_selectedFloorLabel = Label(root, text="Select Floor")
ele2_selectedFloorLabel.place(x=250, y=100)

ele2_floorList = StringVar()
ele2_floorList.set("Floors")
drop = OptionMenu(root, ele2_floorList, *floors)
drop.place(x=220, y=130)

ele2_clickBtn = Button(root, text="click", command=ele2_showLabel)
ele2_clickBtn.place(x=320, y=132)

# --------------------------------------------------------------------------------------------------------------
# Elevator 3
ele3_label = Label(root, bg='blue', width=200, height=350)
ele3_label.place(x=400, y=0)
ele3_text = Label(root, text='Elevator 3', bg='white', font=('Cursive', 16, 'bold'))
ele3_text.place(x=450, y=5)

ele3_floorNumber = StringVar()
ele3_floorLabel = Label(root, textvariable=ele3_floorNumber, bg='blue', font=('Cursive', 16, 'bold'))
ele3_floorLabel.place(x=450, y=50)
ele3_floor = 15
ele3_floorNumber.set(f"Floor: {ele3_floor}")


def ele3_showLabel():
    if ele3_floorList.get() != 'Floors':
        ele3_selectedFloorLabel.config(text=f'{ele3_floorList.get()} is selected')
        print(ele3_floorList.get())


ele3_selectedFloorLabel = Label(root, text="Select Floor")
ele3_selectedFloorLabel.place(x=450, y=100)

ele3_floorList = StringVar()
ele3_floorList.set("Floors")
drop = OptionMenu(root, ele3_floorList, *floors)
drop.place(x=420, y=130)

ele3_clickBtn = Button(root, text="click", command=ele3_showLabel)
ele3_clickBtn.place(x=520, y=132)

# ----------------   External Button & Logs   ------------------------------------------------------------------------------------
# External Button
logs_label = Label(root, bg='yellow', width=450, height=300)
logs_label.place(x=0, y=225)

external_text = Label(root, text='External Requests', bg='white', font=('Cursive', 16, 'bold'))
external_text.place(x=210, y=235)


def external_showLabel():
    if external_floorList.get() != 'Floors':
        external_selectedFloorLabel.config(text=f'{external_floorList.get()} is selected')
        print(external_floorList.get())


external_selectedFloorLabel = Label(root, text="Select Floor")
external_selectedFloorLabel.place(x=250, y=280)

external_floorList = StringVar()
external_floorList.set("Floors")
drop = OptionMenu(root, external_floorList, *floors)
drop.place(x=220, y=313)

external_clickBtn = Button(root, text="click", command=external_showLabel)
external_clickBtn.place(x=320, y=315)

# -----------------------------------------------------------------------------------------------------------------------------
# Logs
log_label = Label(root, bg='black', width=200, height=1)
log_label.place(x=0, y=360)
log_text = Label(root, text='Logs', bg='white', font=('Cursive', 16, 'bold'))
log_text.place(x=260, y=390)

log_textLabel = StringVar()
log_text = Label(root, textvariable=log_textLabel, bg='gray', font=('Cursive', 10, 'bold'))
log_text.place(x=250, y=430)
log_textLabel.set(f"Nothing ...")

root.mainloop()
