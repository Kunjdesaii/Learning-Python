import random
class Train:
    def __init__(self, trainno):
        self.trainno = trainno

    def getbook(self ,source, destination):
        print(f"ticket is booked. your train number is {self.trainno} from {source} to {destination}")

    def status(self):
        print(f"status of train number {self.trainno} is confirmed")

    def fare(self, source, destination):
        print(f"fare is calculated for train number {self.trainno} from {source} to {destination} is {random.randint(100, 500)}")
        
t= Train(12345)
t.getbook("Delhi", "Mumbai")
t.status()
t.fare("Delhi", "Mumbai")