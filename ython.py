#s.lower() will return "\tgeorgia\n".
#s.upper() will return "\tGEORGIA\n".

#task 3.16
#s.strip() will return "Good\tMorning"—the leading whitespace and the newline at the end are removed,
#but the tab between "Good" and "Morning" remains.

#task 3.17
#he format function returns a new string with values inserted into placeholders.

#task 3.18
#The output will show the entire item, ignoring the specified width.

#task.3.19
print(format(57.467657, "9.3f"))
print(format(12345678.923, "9.1f"))
print(format(57.4, ".2f"))
print(format(57.4, "10.2f"))

#task 3.20
print(format(57.467657, "9.3e"))
print(format(12345678.923, "9.1e"))
print(format(57.4, ".2e"))
print(format(57.4, "10.2e"))

#task 3.21
print(format(5789.467657, "9.3f"))
print(format(5789.467657, "<9.3f"))
print(format(5789.4, ".2f"))
print(format(5789.4, "<.2f"))
print(format(5789.4, ">9.2f"))

#task 3.22
print(format(0.457467657, "9.3%"))
print(format(0.457467657, "<9.3%"))

#task 3.23
print(format(45, "5d"))
print(format(45, "<5d"))
print(format(45, "5x"))
print(format(45, "<5x"))