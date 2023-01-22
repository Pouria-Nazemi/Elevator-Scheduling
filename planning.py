import elevator

elevators = []

elevator1 = elevator(name = 1, staticList = [2,5,6,1,12])
elevator2 = elevator(name = 2, head = 8)
elevator3 = elevator(name = 3, head = 12, staticList = [3,4])

elevators.append(elevator1)
elevators.append(elevator2)
elevators.append(elevator3)

for elevator in elevators:
    print(elevator.name)
    
def inputElePlan(floor):
    minDistance = 100
    for eachElevator in elevators:
        distance = 0
        if (floor - eachElevator.head) < 0:
            
            if eachElevator.direction == "DOWN" or eachElevator.direction == "both":
                distance = abs(floor - eachElevator.head)
            elif eachElevator.direction == "UP":
                distance = (eachElevator.up[-1] - eachElevator.head) * 2 + abs(floor - eachElevator.head)
                
        elif (floor - eachElevator.head) > 0:
            if eachElevator.direction == "UP" or eachElevator.direction == "both":
                distance = floor - eachElevator.head
            elif eachElevator.direction == "DOWN":
                distance = (eachElevator.head - eachElevator.down[-1]) * 2 + floor - eachElevator.head
                
        if(minDistance > distance):
            minDistance = distance
            choosenElevator = eachElevator
            
    print(choosenElevator.name)        
    choosenElevator.addInput(floor)
    for eachElevator in elevators:
        print("head of " + str(eachElevator.name) + " head: " + str(eachElevator.head) + " direction " + eachElevator.direction)
    print(str(choosenElevator.name) +str(" floor:* ") + str(floor) + "\n")

def getStatus(elevators):
    for elevator in elevators:
        print("head of " + str(elevator.name) + " head: " + str(elevator.head) + " direction " + elevator.direction)

inputElePlan(2)