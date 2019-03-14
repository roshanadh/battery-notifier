# win10toast library for Toast notifications
from win10toast import ToastNotifier
# psutil library for monitoring battery and charge status
from psutil import sensors_battery

toaster = ToastNotifier()

battery = sensors_battery()
isPlugged = battery.power_plugged
batteryPercent = battery.percent

if batteryPercent <= 35 and isPlugged == False:
    toaster.show_toast("Plug the charger", "Your battery percentage is getting low. \nPlease plug the charger!")

elif batteryPercent >= 85 and isPlugged == True:
    toaster.show_toast("Unplug the charger", "Battery is now sufficiently charged. \nYou may unplug the charger!")

