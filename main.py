#make classes
#get clean input
#make terminal ui
import time

class RideRequest:
    def __init__(self,name,destination,slot,year):
        self.name = name
        self.destination = destination
        self.slot = slot
        self.year = year
        self.submitted = time.time()
        
class cab:
    def __init__(self,driver_name, seats, destination, slot):
        self.driver_name = driver_name
        self.seats = seats
        self.destination = destination
        self.slot = slot
        self.has_left = False
        self.passengers = []   



def main():
    print("hello world")

    

if __name__ == "__main__":
    main()
    