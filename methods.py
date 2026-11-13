from datetime import datetime 

cities = ["Delhi", "Jaipur"]
time_slots = ["Morning", "Afternoon", "Evening", "Night"]

class RideRequest:
    def __init__(self,student_name,destination,time_slot,year,submitted_at = None,):
        name = student_name.strip()
        if not name:
            raise ValueError("Student name cannot be empty.")

        formatted_dest = destination.strip().title()
        if formatted_dest not in cities:
            raise ValueError(f"We don't serve '{destination}'. Valid cities: {', '.join(cities)}.")

        formatted_slot = time_slot.strip().title()
        if formatted_slot not in time_slots:
            raise ValueError(f"Invalid time slot '{time_slot}'. Valid slots: {', '.join(time_slots)}.")

        if not (1 <= year <= 5):
            raise ValueError(f"Year must be an integer between {1} and {5}.")

        self.student_name = name
        self.destination = formatted_dest
        self.time_slot = formatted_slot
        self.year = year
        self.submitted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "student_name": self.student_name,
            "destination": self.destination,
            "time_slot": self.time_slot,
            "year": self.year,
            "submitted_at": self.submitted_at,
            }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_name=data["student_name"],
            destination=data["destination"],
            time_slot=data["time_slot"],
            year=int(data["year"]),
            submitted_at=data.get("submitted_at"),
        )

    def __str__(self):
        return (
            f"{self.student_name} (Year {self.year}) -> {self.destination} "
            f"[{self.time_slot}] | Submitted: {self.submitted_at}"
        )


class Cab:
    def __init__(self,driver_name,seats,destination,time_slot,has_left=False,students=[]):
        driver = driver_name.strip()
        if not driver:
            raise ValueError("Driver name cannot be empty.")

        if not isinstance(seats, int) or not (1 <= seats <= 4):
            raise ValueError(f"Seats must be between {1} and {4}.")

        formatted_dest = destination.strip().title()
        if formatted_dest not in cities:
            raise ValueError(f"Unsupported cab destination '{destination}'. Valid cities: {', '.join(cities)}.")

        formatted_slot = time_slot.strip().title()
        if formatted_slot not in time_slots:
            raise ValueError(f"Unsupported cab time slot '{time_slot}'. Valid slots: {', '.join(time_slots)}.")

        self.driver_name = driver
        self.seats = seats
        self.destination = formatted_dest
        self.time_slot = formatted_slot
        self.has_left = bool(has_left)
        self.students = students

    def to_dict(self):
        return {
            "driver_name": self.driver_name,
            "seats": self.seats,
            "destination": self.destination,
            "time_slot": self.time_slot,
            "has_left": self.has_left,
            "students": [student.to_dict() for student in self.students],
        }

    @classmethod
    def from_dict(cls, data):
        students = [RideRequest.from_dict(s) for s in data.get("students", [])]
        return cls(
            driver_name=data["driver_name"],
            seats=int(data["seats"]),
            destination=data["destination"],
            time_slot=data["time_slot"],
            has_left=data.get("has_left", False),
            students=students,
        )

    def __str__(self):
        if self.has_left:
            status = "Already Left"
        else:
            status = "Open"
        passengers = (", ".join(s.student_name for s in self.students) if self.students else "None")
        return (
            f"Driver: {self.driver_name} | {self.destination} ({self.time_slot}) | "
            f"Seats: {len(self.students)}/{self.seats} | Status: {status} | "
            f"Students: [{passengers}]"
        )