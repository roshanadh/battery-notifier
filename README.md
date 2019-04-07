# battery-notifier
Push toast notifications in your Windows regarding battery and charge status

You're a battery-nerd. You like your device's battery percent within the golden range of 30 to 80.

However, you always remember to plug the charger late, and/or forget to unplug the charger early. What do you do?

(hint: use battery-notifier)

## Local
To use battery-notifier on your local system,

* Clone the repo
```sh
git clone https://github.com/roshanadh/battery-notifier
```
* Change your working directory to the cloned repo
```sh
cd battery-notifier
```
* Make a shortcut of run-script.vbs file
* Go to run and type shell:startup
* Move the previously created shortcut to the newly opened window
* Done!

This should run the VBScript everytime Windows boots and now the .vbs file runs the python script in every startup.
