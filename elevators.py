import time, threading


class elevator(threading.Thread):

    def __init__(self, name, head=1, staticList=[]):
        threading.Thread.__init__(self)

        self.inputs = []
        self.up = []
        self.down = []
        self.head = 1
        self.direction = "both"
        self.seekProcedure = []
        self.name = ("elevator" + str(name))
        self.inputs.extend(staticList)
        self.head = head
        self.start()

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
                    self.down.sort(reverse=True)

    def run(self):
        while (True):
            self.inputsHandling()
            if len(self.up) == 0 and len(self.down) == 0:
                self.direction = "both"
                continue

            if self.direction == "UP" or self.direction == "both":
                if not len(self.up) == 0:
                    goalFloor = self.up[0]
                    if goalFloor == self.head:
                        self.seekProcedure.append(goalFloor)
                        print(self.name + " arrived to floor " + str(goalFloor) + "\n") #TODO
                        self.up.pop(0)
                    else:
                        self.head = self.head + 1
                else:
                    self.direction = "DOWN"

            if self.direction == "DOWN" or self.direction == "both":
                if not len(self.down) == 0:
                    goalFloor = self.down[0]
                    if goalFloor == self.head:
                        self.seekProcedure.append(goalFloor)
                        print(self.name + " arrived to floor " + str(goalFloor) + "\n") #TODO
                        self.down.pop(0)
                    else:
                        self.head = self.head - 1
                else:
                    self.direction = "UP"
            time.sleep(3) #TODO change time

    def addInput(self, floor):
        self.inputs.append(floor)

    def checkWhichFirst(self):
        if(len(self.up) != 0 and len(self.down) != 0 and self.direction == "both"):
            if(abs(self.head - self.up[0]) < self.head - self.down[0]):
                self.direction = "UP"
            else:
                self.direction = "DOWN"

