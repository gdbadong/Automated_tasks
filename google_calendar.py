import org.sikuli.basics.SikulixForJython
from sikuli import *

# Firefox path
mozilla_firefox = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

class Calendar():
    app = App('Mozilla Firefox')

    def steps(self,date,allday,mintime,maxdate,maxtime,title,guest):
        click('images/create')
        wait('images/start')
        if maxdate == "":
            maxdate = date
        if allday == 'no':
            type(title + Key.TAB + date + Key.TAB + mintime + Key.TAB + maxtime + Key.TAB + maxdate)
            click('images/addguest')
            type(guest + Key.ENTER)
            click('images/save')
        elif allday == 'yes':
            type(title + Key.TAB + date + Key.TAB + Key.TAB + Key.TAB + maxdate)
            click('images/allday')
            click('images/addguest')
            type(guest + Key.ENTER)
            click('images/save')

    def run(self,date,allday,mintime,maxdate,maxtime,title,guest):
        self.app.open(mozilla_firefox)
        self.app.focus()
        type(Key.SPACE,KeyModifier.ALT)
        type('x')
        type('d', Key.ALT)
        type('calendar.google.com' + Key.ENTER)
        waitVanish('images/mozilla_logo',FOREVER)

        if exists('images/google_login_page'):
            type('arcanys.test.auto@gmail.com' + Key.ENTER)
            type('t3st1ng!@34' + Key.ENTER)
            wait('images/google_logo1')

            self.steps(date,allday,mintime,maxdate,maxtime,title,guest)

        elif exists('images/google_logo1'):

            self.steps(date,allday,mintime,maxdate,maxtime,title,guest)