import random

horsesNames = set()
def generateRandom():
    num = random.randint(1, 100)
    if num not in horsesNames:
        horsesNames.add(num)
        return num
    else:
        return generateRandom()


class Horse:
    def __init__(self, finish=1000):
        self.speed = 0
        self.name = f"Horse#{generateRandom()}"
        self.disToFinish = finish
        self.inFinish = False
        self.time = 0
        self.avgSpeed = 0
        self.speeds = []

    def __str__(self):
        return f"{self.name}: {self.getTime()} ... average speed: {self.avgSpeed}"

    def __lt__(self, other):
        return self.time < other.time

    def getTime(self):
        def fixTime(tt):
            if tt < 10:
                return f"0{tt}"
            return f"{tt}"
        minutes = fixTime(self.time // 60)
        seconds = fixTime(self.time % 60)
        return f"{minutes}:{seconds}"

    def changeSpeed(self):
        self.speed = round(random.gauss(8.3, 15), 5)
        self.speeds.append(self.speed)

    def move(self):
        self.changeSpeed()
        self.disToFinish -= self.speed
        self.time += 1

    def checkInFinish(self):
        if self.disToFinish <= 0:
            self.inFinish = True
            self.avgSpeed = sum(self.speeds) / len(self.speeds)


def everyoneInFinish(horses):
    for horse in horses:
        if not horse.inFinish:
            return False
    return True


def preload():
    numH = int(input("how many horses: "))
    dis = int(input("how long trace: "))
    return [Horse(dis) for _ in range(numH)]


def simulate(horses):
    while not everyoneInFinish(horses):
        for horse in horses:
            if not horse.inFinish:
                horse.move()
                horse.checkInFinish()


def printRanks(horses):
    #horses.sort(key=lambda x: x.time)
    horses.sort()
    for i in range(1, len(horses)+1):
        print(f"{i}: {horses[i-1]}")


def main():
    horses = preload()
    simulate(horses)
    printRanks(horses)


main()
