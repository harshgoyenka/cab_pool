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
        
class Cab:
    def __init__(self,driver_name, seats, destination, slot):
        self.driver_name = driver_name
        self.seats = seats
        self.destination = destination
        self.slot = slot
        self.has_left = False
        self.passengers = []   



def main():
    pending_requests =[]
    
    cabs = [
      Cab("Ramesh", 4, "Delhi", "Morning"),
      Cab("Suresh", 3, "Jaipur", "Night"),
      Cab("Mukesh", 4, "Delhi", "Evening"),
    ]
    
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
            if not pending_requests:
                print("No students waiting")
            else:
                for i in pending_requests:
                    print(f"Name:{i.name}| Destination:{i.destination}| Time:{i.slot}| Year:{i.year}")
                    
                    
            print("ALL CAB STATUS")
            for cab in cabs:
                status = "LEFT" if cab.has_left else "OPEN"
                count = len(cab.passengers)
                print(
                f"Driver: {cab.driver_name} | Route: {cab.destination}"
                f" ({cab.slot}) | Occupied: {count}/{cab.seats} | Status:"
                f" {status}"
                )
                
        elif choice =="3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice!!")
            
            
if __name__ == "__main__":
    main()
    