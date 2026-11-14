from methods import RideRequest,cities,time_slots
from storage import load_cabs,save_cabs,load_requests,save_requests
import heapq

def generate_queue(pending_requests):
    trip_queue={}
    for i in pending_requests:
        push_queue(i,trip_queue)
    return trip_queue

def push_queue(i,trip_queue):
    key = (i.destination,i.time_slot)
    if key not in trip_queue:
        trip_queue[key] = []
    heapq.heappush(trip_queue[key],(-i.year,i.submitted_at,i))


def dispatch_cab(trip_queue, cabs):
    print("\n=== Let a Cab Leave ===")
    open_cabs = [cab for cab in cabs if not cab.has_left]

    if not open_cabs:
        print("No open cabs available to send off.")
        return
    
    for id,cab in enumerate(open_cabs,start=1):
        print(f"{id}. {cab}")

    choice = int(input("Choose an open cab to dispatch (0 to cancel)"))
    if choice == 0:
        print("Dispatch cancelled.")
        return

    selected_cab = open_cabs[choice-1]

    boarded = selected_cab.dispatch(trip_queue)

    print(f"\nDispatched: {selected_cab.driver_name} -> {selected_cab.destination} "
        f"[{selected_cab.time_slot}] | Final Seats: {len(selected_cab.students)}/{selected_cab.seats}")
    
    if boarded:
        print("Newly boarded students (removed from waiting list):")
        for student in boarded:
            print(f"  - {student.student_name} (Year {student.year})")
    else:
        print("No new waiting students boarded.")
    
    requests = [i[-1] for i in trip_queue.values() for req in i]
    save_requests(requests)
    save_cabs(cabs)


def find_matches(trip_queue, cabs):
    print("\n=== Match Preview (No Seats Assigned) **old ===")

    open_cabs = [cab for cab in cabs if not cab.has_left]

    if not open_cabs:
        print("No open cabs available.")
        return
    
    shown = list()
    
    for id,cab in enumerate(open_cabs,start=1):
        seats_available = cab.seats - len(cab.students)
        print(
            f"\n{id}. Cab: {cab.driver_name} -> {cab.destination} [{cab.time_slot}] "
            f"(Available seats: {seats_available}/{cab.seats})"
        )

        if seats_available <= 0:
            print("Matched students: None (Cab is full)")
            continue
        
        key = (cab.destination, cab.time_slot)
        req = trip_queue.get(key,[])
        
        students = [i[-1] for i in sorted(req) if i[-1] not in shown][:seats_available]

        if not students:
            print("Matched students: None")
        else:
            for student in students:
                print(f"- {student.student_name} (Year {student.year}) | Submitted: {student.submitted_at}")
                shown.append(student)


def add_ride_request(trip_queue):
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
        push_queue(request,trip_queue)
        print(f"Added request: {request}")
        
        requests = [i[-1] for i in trip_queue.values() for req in i]
        save_requests(requests)
            
    except ValueError as err:
        print(f"Error: {err}")


def view_status(trip_queue,cabs):
    print("\n=== Students Currently Waiting ===")
    if not trip_queue.values():
        print("No students waiting.")
    else:
        requests = [req[-1] for i in trip_queue.values() for req in i]
        for id,req in enumerate(requests,start=1):
            print(f"{id}. {req}")

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
            for id,cab in enumerate(open_cabs,start=1):
                print(f"{id}. {cab}")

        print("Already Left:")
        if not departed_cabs:
            print("None")
        else:
            for id,cab in enumerate(departed_cabs,start=1):
                print(f"{id}. {cab}")

def main():
    cabs = load_cabs()
    pending_requests = load_requests()
    #one time use only all other changes are done directly to this queue
    trip_queue=generate_queue(pending_requests)

    while True:
        print("\n==============================")
        print("      Cab Sharing Menu")
        print("==============================")
        print("1. Add a new ride request.")
        print("2. See everyone still waiting, plus all cabs (both open and already left).")
        print("3. Find matches (preview).")
        print("4. Let a cab leave.")
        print("5. Quit the app.")

        choice = input("Choose an option (1-5)")

        if choice == "1":
            add_ride_request(trip_queue)
        elif choice == "2":
            view_status(trip_queue, cabs)
        elif choice == "3":
            find_matches(trip_queue, cabs)
        elif choice == "4":
            dispatch_cab(trip_queue, cabs)
        elif choice == "5":
            save_cabs(cabs)
            requests = [i[-1] for i in trip_queue.values() for req in i]
            save_requests(requests)
            print("Data saved. Goodbye!")
            break

if __name__ == "__main__":
    main()