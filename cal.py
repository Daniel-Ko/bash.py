import sys
import argparse
from datetime import datetime
import calendar as cal


parser = argparse.ArgumentParser()

parser.add_argument("month", nargs="?",  type=int, default=datetime.now().month, help="1-12 determines the month")
parser.add_argument("year", nargs="?", type=int, default=datetime.now().year, help="1-9999 4-digit year")
parser.add_argument("-m", help="Display Monday as the first day of the week", action="store_true")
parser.add_argument("-t", help="Give today's date", action="store_true")
parser.add_argument("-y", help="Display a calendar for the current year", action="store_true")

args = parser.parse_args()

if args.month < 1 or args.month > 12:
    print("Invalid month") 
    sys.exit(0)  

if args.year < 1 or args.year > 9999:
    print("Invalid year")
    sys.exit(0)

if args.t:
    print(datetime.now().strftime("  (%Y-%m-%d %H:%M)"))
first_day_of_week = cal.SUNDAY if not args.m else cal.MONDAY
textcal = cal.TextCalendar(first_day_of_week)

if args.y:
    textcal.pryear(args.year)
else:
    textcal.prmonth(args.year, args.month)




