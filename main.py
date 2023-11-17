import sys
from AttendanceCalculator import AttendanceCalculator


try:
    n = int(sys.argv[1])
except IndexError:
    print("Please provide required parameter - number of days")
except ValueError:
    print("Please provide a valid integer for number of days")
except Exception as e:
    print("Oops something went wrong {}".format(e))
else:
    try:
        m = sys.argv[2]
    except:
        m=4

    attendanceCalculator = AttendanceCalculator(int(n), int(m))
    attendanceCalculator.get_ways_and_print()
