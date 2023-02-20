#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# Lab01_2
# 229223 Sec 002

#Input
mill = int(input("Input milliseconds: "))

#CaLculate millisecond and change millisecond to second
millisec = (mill % 1000) 
millisec_to_sec = mill / 1000

#CaLculate second and change second to minute
sec = millisec_to_sec % 60
sec_to_minute = (millisec_to_sec - sec) / 60

#CaLculate minute and change minute to hour
minute = sec_to_minute % 60
minute_to_hour = (sec_to_minute - minute) / 60

#CaLculate hour and change hour to day
hour = minute_to_hour % 24
hour_to_day = minute_to_hour - hour

#CaLculate day
day = hour_to_day / 24

#Display Answer
print("%d day(s), %d hour(s), %d minute(s), %d second(s), and %d millisec(s) "  %(day , hour , minute , sec , millisec))

