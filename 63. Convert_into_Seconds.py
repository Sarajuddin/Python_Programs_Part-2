# 63. Write a Python program to convert seconds to day, hour, minutes and seconds.

time = int(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("Days : Hours : Minutes : Seconds -> %d : %d : %d : %d" % (day, hour, minutes, seconds))