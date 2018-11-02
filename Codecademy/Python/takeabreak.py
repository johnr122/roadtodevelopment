import time
import webbrowser

breakcount = 3
breaks = 0

print ("This program is ran at exactly "+time.ctime())

while (breaks < breakcount):
    time.sleep(7200);
    webbrowser.open("https://www.youtube.com/watch?v=2E2El1kdooM");
    
    breaks = breaks + 1