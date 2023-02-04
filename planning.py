# from elevator import elevator
# from tkinter import *
#
# elevators = []
#
# elevator1 = elevator(name=1, staticList=[2, 5, 6, 1, 12])
# elevator2 = elevator(name=2, head=8)
# elevator3 = elevator(name=3, head=12, staticList=[3, 4])
#
# elevators.append(elevator1)
# elevators.append(elevator2)
# elevators.append(elevator3)
#
#
# def inputElePlan(floor):
#     minDistance = 100
#     for eachElevator in elevators:
#         distance = 0
#         if (floor - eachElevator.head) < 0:
#
#             if eachElevator.direction == "DOWN" or eachElevator.direction == "both":
#                 distance = abs(floor - eachElevator.head)
#             elif eachElevator.direction == "UP":
#                 distance = (eachElevator.up[-1] - eachElevator.head) * 2 + abs(floor - eachElevator.head)
#
#         elif (floor - eachElevator.head) > 0:
#             if eachElevator.direction == "UP" or eachElevator.direction == "both":
#                 distance = floor - eachElevator.head
#             elif eachElevator.direction == "DOWN":
#                 print(eachElevator.name + " check")
#                 logLabel.set(eachElevator.name + " check")
#                 distance = (eachElevator.head - eachElevator.down[-1]) * 2 + floor - eachElevator.head
#
#         if (minDistance > distance):
#             minDistance = distance
#             choosenElevator = eachElevator
#
#     print(choosenElevator.name)
#     logLabel.set(choosenElevator.name)
#
#     choosenElevator.addInput(floor)
#     for eachElevator in elevators:
#         print("head of " + str(eachElevator.name) + " head: " + str(
#             eachElevator.head) + " direction " + eachElevator.direction)
#
#         logLabel.set("head of " + str(eachElevator.name) + " head: " + str(
#             eachElevator.head) + " direction " + eachElevator.direction)
#
#     print(str(choosenElevator.name) + str(" floor:* ") + str(floor) + "\n")
#     logLabel.set(str(choosenElevator.name) + str(" floor:* ") + str(floor) + "\n")
#
#
# def getStatus(elevators):
#     for elevator in elevators:
#         print("head of " + str(elevator.name) + " head: " + str(elevator.head) + " direction " + elevator.direction)
#         logLabel.set(
#             "head of " + str(elevator.name) + " head: " + str(elevator.head) + " direction " + elevator.direction)
#
#
# root = Tk()
# root.title("Elevator Algorithm")
# root.geometry("950x640")
# # root.wm_attributes("-topmost", 1)  # set always on top
# # bg = PhotoImage(file="Base1.png")
# # bg = PhotoImage(file="Base2.png")
# label1 = Label(root)#, image=bg)
# label1.place(x=0, y=0)
#
# # logLabel = StringVar()
# # label2 = Label(root, textvariable=logLabel, bg='green', font=('Cursive', 16, 'bold'))
# # label2.place(x=400, y=605)
#
# inputElePlan(15)
# root.mainloop()
