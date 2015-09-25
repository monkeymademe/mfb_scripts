odds on you don't have an /etc/X11/xorg.conf if not its okay just to create this fragment...

/etc/X11/xorg.conf

Code: Select all
    Section "InputClass"
       Identifier "calibration"
       Driver "evdev"
       MatchProduct "FT5406 memory based driver"

       Option "EmulateThirdButton" "1"
       Option "EmulateThirdButtonTimeout" "750"
       Option "EmulateThirdButtonMoveThreshold" "30"
    EndSection



(re)start X and you should find that a long press behaves like a right click, time to throw your mouse out?

Enjoy!
