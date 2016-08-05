import os
from sikuli import *
import org.sikuli.basics.SikulixForJython

class Test():
    def run(self):
        a = os.path.abspath('Mozilla Firefox/firefox')
        print 'a= '+a
        b = os.path.dirname(a)
        print 'b= '+b
        open('firefox.exe')
        # fox = os.path.dirname(os.path.abspath('firefox.exe'))
        # print fox
        # foxit = fox+'\\'