from google_calendar import Calendar
from test import Test

def main():

    # Fill These Up
    date = "8/26/2016"
    maxdate = "8/30/2016"
    allday = "yes" #yes or no
    mintime = "8:00am"
    maxtime = "5:00pm"
    title = "Tibz - Out of Office"
    guest = "glennbadong@gmail.com"

    # Where you call
    cal = Calendar()
    cal.run(date,allday,mintime,maxdate,maxtime,title,guest)

    tes = Test()
    # tes.run()

if __name__ == '__main__':
    main()