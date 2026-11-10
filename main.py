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
    pending_requests =[]
    
    while True:
        print("CAB POOL MATCHER")
        print("1. Add a new ride request")
        print("2. See everyone waiting and cabs")
        print("3. Quit the app")
        
        choice = input("Select an Option (1-3)=")
        
        if choice == "1":
            name = input("Student name=")
            destination = input("Enter Destination=")
            slot = input("Enter time slot(Morning/Afternoon/Evening/Night)=")
            year = input("Enter Year of Study=")
            request = RideRequest(name,destination,slot,year)
            pending_requests.append(request)
            print("added request")
            
        elif choice =="2":
            print("STUDENTS STILL WAITING")
            for i in pending_requests:
                print(i)
                
        elif choice =="3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice!!")
            
            
if __name__ == "__main__":
    main()
    