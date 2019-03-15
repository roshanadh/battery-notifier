# win10toast library for Toast notifications
from win10toast import ToastNotifier
# psutil library for monitoring battery and charge status
from psutil import sensors_battery
import time

toaster = ToastNotifier()

isNotifiedLow = False
isNotifiedHigh = False

battery = sensors_battery()
isPlugged = battery.power_plugged
batteryPercent = battery.percent

while(True):
    if batteryPercent <= 35 and isPlugged == False and isNotifiedLow == False:
        toaster.show_toast("Plug the charger", "Your battery percentage is getting low. \nPlease plug the charger!")
        isNotifiedLow = True
    elif batteryPercent <= 35 and isPlugged == True and isNotifiedLow == True:
        isNotifiedLow = False

    elif batteryPercent >= 85 and isPlugged == True and isNotifiedHigh == False:
        toaster.show_toast("Unplug the charger", "Battery is now sufficiently charged. \nYou may unplug the charger!")
        isNotifiedHigh = True
    elif batteryPercent >= 85 and isPlugged == False and isNotifiedHigh == True:
        isNotifiedHigh = False 

    battery = sensors_battery()
    isPlugged = battery.power_plugged
    batteryPercent = battery.percent

    time.sleep(30)