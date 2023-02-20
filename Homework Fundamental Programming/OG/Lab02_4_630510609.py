#630510609
#กฤตเมธ ไทยเจริญ
#003
#Lab02_4
milliseconds = int(input("Input number of milliseconds: "))#Set milliseconds is integer 
OD = int(24*60*60*1000)#OD is time in a one day in milliseconds
Day = int(milliseconds/OD)#Take milliseconds didive OD to calculate for Day
Hr = int((milliseconds/OD - Day)*24)#Take milliseconds divde OD minus Day and multiply 24 for change day to hour
minute = int(((milliseconds/OD - Day)*24 - Hr)*60)#Take milliseconds divde OD minus Day and multiply 24 divide Hr and multiply 60 to change hour to minutes
seconds = int((((milliseconds/OD - Day)*24 - Hr)*60 - minute)*60)#Take milliseconds divde OD minus Day and multiply 24 divide Hr and multiply 60 divide minute and multiply 60 to change minute to seconds
millisec = int(milliseconds%1000)#Calculate millisec by take milliseconds in input and mod it
print("Results = %d day(s), %d hour(s), %d minute(s), %d second(s), and %d millisec(s)" %(Day,Hr,minute,seconds,millisec) )
