issue:
if two requests are sent at the same time, then it causes error.(although this won't happen in this program)

1. The data is saved after every change
2. cab can leave with 1-2 students as it is done just using list slicing
3. cabs and requests json is different so even if there are no cabs, it would just mean that we cannot dispatch any more cabs.
4. if two students are in the same year, we compare them by time they are submitted using heap function.
5. adding a request is also associated with saving it to file. so in all it a dict lookup ( O(log k)), then heappush (O(log n)) and also writing to file (O(n))


run by 
python.exe main.py

the cab file looks like this:
[
{
    "driver_name": ,
    "seats": ,
    "destination": ,
    "time_slot": ,
    "has_left": ,
    "students":
  }
]

to make the program persistant the requests are saved in a file
[
  {
    "student_name": ",
    "destination": 
    "time_slot": ,
    "year": ,
    "submitted_at": 
  }
]

