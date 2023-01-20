import time
class elevator:

    inputs = []
    up = []
    down = []
    head = 1
    direction = "DOWN"
    seekProcedure = []

    def __init__(self, head, staticList = []):
        self.inputs.extend(staticList)
        self.head = head
        self.move()

    def inputsHandling(self):
        while not len(self.inputs) == 0:
            input = self.inputs.pop(0)
            if (input > self.head):
                if not self.up.__contains__(input):
                    self.up.append(input)
                    self.up.sort()
            else:
                if not self.down.__contains__(input):
                    self.down.append(input)
                    self.down.sort(reverse = True)
    def move(self):
        while(True):
            self.inputsHandling()
            if len(self.up) == 0 and len(self.down) == 0:
                self.direction = "both"
                break

            if self.direction == "UP" or self.direction == "both":
                if not len(self.up) == 0:
                    goalFloor = self.up[0]
                    if goalFloor == self.head:
                        self.seekProcedure.append(goalFloor)
                        print("arrived to floor" + str(goalFloor))
                        self.up.pop(0)
                    else:
                        self.head = self.head + 1
                else:
                    print("down")
                    self.direction = "DOWN"

            if self.direction == "DOWN" or self.direction == "both":
                if not len(self.down) == 0:
                    goalFloor = self.down[0]
                    if goalFloor == self.head:
                        self.seekProcedure.append(goalFloor)
                        print("arrived to floor" + str(goalFloor))
                        self.down.pop(0)
                    else:
                        self.head = self.head - 1
                else:
                    print("up")
                    self.direction = "UP"
            time.sleep(1.0)

    def addInput(self, floor):
        self.inputs.append(floor)

e = elevator(head = 7,staticList = [5,7,2,6,1,9,12])
print("stop")