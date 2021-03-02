from colorama import init, Fore, Back, Style
init()

CSI = "\x1b["

Clear_Screen =  CSI + "2J"
Red_Color = CSI + "31;49m"
Green_Color = CSI + "32;49m"
Yellow_Color = CSI + "33;49m"
Blue_Color = CSI + "34;49m"
Magenta_Color = CSI + "35;49m"
Cyan_Color = CSI + "36;49m"
Reset_Color = CSI + "0m"