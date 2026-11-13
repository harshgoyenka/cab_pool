from methods import RideRequest,cities,time_slots
from storage import load_cabs,save_cabs,load_requests,save_requests

def add_ride_request(pending_requests):
    print("\n--- New Ride Request ---")
    name = input("Student's name: ")
    destination = input(f"Destination ({'/'.join(cities)}): ")
    time_slot = input(f"Time slot ({'/'.join(time_slots)}): ")
    
    try:
        year = int(input("Year (1 to 5): ").strip())
    except ValueError:
        print(f"Error: not a valid year. Please enter a number from (1-5).")
        return

    try:
        request = RideRequest(student_name=name,destination=destination,time_slot=time_slot,year=year)
        pending_requests.append(request)
        print(f"Added request: {request}")
    except ValueError as err:
        print(f"Error: {err}")


def view_status(waiting_requests,cabs):
    print("\n=== Students Currently Waiting ===")
    if not waiting_requests:
        print("No students waiting.")
    else:
        i=1
        for req in waiting_requests:
            print(f"{i}. {req}")
            i+=1

    print("\n=== All Cabs ===")
    if not cabs:
        print("No cabs available.")
    else:
        open_cabs = [cab for cab in cabs if not cab.has_left]
        departed_cabs = [cab for cab in cabs if cab.has_left]

        print("Open Cabs:")
        if not open_cabs:
            print("None")
        else:
            i =1
            for cab in open_cabs:
                print(f"{i}. {cab}")
                i+=1

        print("Already Left:")
        if not departed_cabs:
            print("None")
        else:
            i=1
            for cab in departed_cabs:
                print(f"{i}. {cab}")
                i+=1

def main():
    cabs = load_cabs()
    pending_requests = load_requests()

    while True:
        print("\n==============================")
        print("      Cab Sharing Menu")
        print("==============================")
        print("1. Add a new ride request.")
        print("2. See everyone still waiting, plus all cabs.")
        print("3. Quit the app.")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_ride_request(pending_requests)
        elif choice == "2":
            view_status(pending_requests, cabs)
        elif choice == "3":
            save_cabs(cabs)
            save_requests(pending_requests)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()