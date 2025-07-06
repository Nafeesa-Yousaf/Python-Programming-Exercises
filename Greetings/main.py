#checks the current hour and prints an appropriate greeting based on the time of day.
import time
t=int(time.strftime('%H'))
if(t>=4 and t<=10):
    print("Good Morning!")
elif(t>10 and t<=13):
    print("Good Noon!")
elif(t>13 and t<=16):
    print("Good Afternoon!")
elif(t>16 and t<=19):
    print("Good Evening!")
else:
    print("Good night!")