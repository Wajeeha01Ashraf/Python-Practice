#Write a Python program to print the following string in a specific format (see the output).
#print("Twinkle twinkle little star\n\t How I wonder what you are\n\t\tUp above the world so high\n\t\t\tLike a diamond in the sky\nTwinkle twinkle little star\n\t How I wonder what you are")

#2. Write a Python program to find out what version of Python you are using.
'''import sys
print("Python_Version")
print(sys.version)
print("Python Version Info")
print(sys.version_info)
'''

#3. Write a Python program to display the current date and time. Sample Output : Current date and time : 2014-07-05 14:34:14
'''
from datetime import datetime
d_time=datetime.now()
print("Current Date and Time: ")
print(d_time.strftime("%Y-%m-%d %H-%M-%S"))
'''

#4. Write a Python program that calculates the area of a circle based on the radius entered by the user
'''
from math import pi
r=int(input("Enter the radius of circle: "))
area=pi*r**2
print(f"The area of the circle with radius {r} is: {area:.2f}")
'''

#5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
'''
f_name=input("Enter First Name: ")
l_name=input("Enter Last Name: ")
print("Hello "+l_name+ " " +f_name+ "!")
'''

#6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
'''
seq=input("Ask the number for the user: ")
list=seq.split(",")
tuple=tuple(list)
print("Lists: ",list)
print("Tuple: ",tuple)
'''

#7. Write a Python program that accepts a filename from the user and prints the extension of the file.
'''
file=input("Enter the filename: ")
f_exten=file.split(".")
print("The extension of the file is: "+repr(f_exten[-1]))
'''
#8. Write a Python program to display the first and last colors from the following list.
'''
color_list = ["Red", "Green", "White", "Black", "Blue"]

# Display the first and last colors
first_color = color_list[0]
last_color = color_list[-1]

print("First color: ",first_color)
print("Last color: ",last_color)
'''

#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). exam_st_date = (11, 12, 2014)
'''
e_st_date=(11,12,2024)
print("The examination will start from: %i/%i/%i"%e_st_date)
'''

#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
'''
n = input("Enter an integer: ")
result = int(n) + int(n*2) + int(n*3)
print("The result of n + nn + nnn for n = " +n+ " is:" ,result)
'''
#11.Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
'''
print(len.__doc__)
'''

#12. Write a Python program that prints the calendar for a given month and year.
'''
import calendar
y=int(input("Enter Year: "))
m=int(input("Enter Month: "))
print(calendar.month(y,m))
'''

#13. Write a Python program to print the following 'here document'.
'''
print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")
'''

#14. Write a Python program to calculate the number of days between two dates.
'''
from datetime import date
f_date=date(2024, 10, 1)
l_date=date(2024, 10, 21)
d=l_date-f_date
print(d.days)
'''
#15. Write a  Python program to get the volume of a sphere with radius six.
import math
'''
pi=3.14
r=6
V=4/3*pi*r**3
print("The volume of a sphere is: ",V)
'''

#16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
'''
def difference(n):
    if n<=17:
        return 17-n
    else:
        return (n-17)*2
num = int(input("Enter a number: "))
res=difference(num)
print("The result is: ",res)
num1 = int(input("Enter a number: "))
res1=difference(num1)
print("The result is: ",res1)
'''

#17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
'''
def thousand(n):
    return ((abs(1000-n)<=100)or(abs(2000-n)<=100))
print(thousand(1000))
print(thousand(900))
print(thousand(500))
'''

#18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
'''
def sum(x,y,z):
    sum1=x+y+z
    if x==y==z:
        return 3*sum1
    else:
        return sum1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
res = sum(num1, num2, num3)
print("The result is: ",res)
'''

#19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
'''
def to_string(s):
    if s.startswith("Is"):
        return s
    else:
        return "Is" + s
string = input("Enter a string: ")
result =to_string(string)
print("The result is: ",result)
'''

#20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
'''
def string(s,n):
    return s * n
string1 = input("Enter a string: ")
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("The number must be non-negative.")
else:
    result = string(string1, n)
    print("The result is: " , result)
'''

#21.  Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
'''
num=int(input("Enter any number: "))
if num%2==0:
    print("This is an even number: ")
else:
    print("This is an odd number: ")
'''

#22. Write a Python program to count the number 4 in a given list.
'''
list = input("Enter a list of numbers separated by spaces: ")
count =list.count('4')
print("The number 4 appears", count ,"times in the list.")
'''

#23.
#52. Write a Python program to print to STDERR.
'''import sys

# Print a message to STDERR
print("This is an error message.", file=sys.stderr)
'''

#53. Write a Python program to access environment variables.
'''
import os       #operating system including environment variables
for data in os.environ:
    print(data)         #name of the environment variable.
    print('-' * 15)     # Print a separator for clarity.
    print(os.environ[data])     #value of the environment variable.
    print('=' * 30)     # line of '=' characters as an additional separator.
'''

#54. Write a Python program to get the current username.
'''
import getpass #Module used for current user name
print(getpass.getuser())
'''

#55. Write a Python program to find local IP addresses using Python's stdlib.
'''
import socket       # network-related functions.
local= socket.gethostname()
ip= socket.gethostbyname_ex(local)[2]
filtered= [ip for ip in ip if not ip.startswith("127.")]
first = filtered[:1]
print(first[0])
'''

#56. Write a Python program to get the height and width of the console window.


#57. Write a Python program to get the execution time of a Python method.
'''
import time
def numbers(n):
    start = time.time()  # Start time
    total = sum(range(1, n + 1))  # Calculate the sum
    end_time = time.time()  # End time
    return total, end_time - start  # Return the sum and execution time
n = 5
result, exe_time = numbers(n)  # Call the function
print("\nSum of numbers from 1 to " ,n ,"is:",result)
print("Time taken to calculate: ",exe_time ,"seconds")
'''

#58. Write a Python program to sum the first n positive integers.
'''
n=int(input("Enter Positive Integers: "))
sum=(n*(n+1))/2
print("Sum of first",n,"positive integers:",sum)
'''

#59. Write a Python program to convert height (in feet and inches) to centimeters.
'''
def centimeters(feet, inches):
    return (feet * 20) + (inches * 2)
feet = int(input("Enter height in feet: "))
print("Height in Feet",feet*12)
inches = int(input("Enter height in inches: "))
print("Height in inches", inches*2)
cm =feet*12+inches*2
print("Height in centimeters: ",cm)
'''

#60. Write a Python program to calculate the hypotenuse of a right angled triangle.
'''
from math import sqrt
base=int(input("Enter Base: "))
height=int(input("Enter Height: "))
c=sqrt(base**2+height**2)
print(c)
'''

#61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.
'''
feet = int(input("Enter height in feet: "))
print("The distance in inches is %i inches." ,feet*8)
print("The distance in yards is %.2f yards.", feet/2)
print("The distance in miles is %.2f miles.", feet/52)
'''

#62. Write a Python program to convert all units of time into seconds.
'''
days = int(input("Input days: "))
hours = int(input("Input hours: "))
minutes = int(input("Input minutes: "))
seconds = int(input("Input seconds: "))
time = days*3600*24 + hours*3600 + minutes*60 + seconds
print("The amount of seconds:", time)
'''

#63. Write a Python program to get an absolute file path.
'''
def file_path(path):
    import os
    return os.path.abspath(path)
print("Absolute file path: ", file_path("excersise.txt"))
'''

#64. Write a Python program that retrieves the date and time of file creation and modification.
# Import the 'os.path' and 'time' modules to work with file system paths and timestamps.
'''
import os.path, time

# Print the last modified timestamp of the file "test.txt" in a human-readable format.
print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))

# Print the creation timestamp of the file "test.txt" in a human-readable format.
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

'''

#65. Write a Python program that converts seconds into days, hours, minutes, and seconds.
'''
time=float(input("Input time in seconds: "))
day=time//(24*3600)
time=time%(24*3600)
hour=time//3600
minutes = time // 60
time%=60
seconds=time
print("Days,Hours,Months,Seconds:  %d:%d:%d:%d" % (day, hour, minutes, seconds))
'''

#66. Write a Python program to calculate the body mass index.
'''
height=float(input("Enter your height: "))
weight=int(input("Enter your weight: "))
bmi=weight/(height*height)
print(bmi)
'''

#67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
'''
kpa = float(input("Input pressure in kilopascals: "))
print("The pressure in pounds per square inch: %.2f psi",kpa / 4.2865)
print("The pressure in millimeters of mercury: %.2f mmHg" ,kpa * 760 / 9.54)
print("Atmosphere pressure: %.2f atm.",kpa / 10.34)
'''

#68. Write a Python program to calculate sum of digits of a number.
'''def sum(number):
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total
number = int(input("Enter a number: "))
result = sum(number)
print("The sum of digits of ", number ,"is:" ,result)
'''

#69. Write a Python program to sort three integers without using conditional statements and loops
'''
x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))
a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - (a1 + a3)
print("Numbers in sorted order: ", a1, a2, a3)
'''

#70. Write a  Python program to sort files by date.
'''
import os
directory = input("Enter the directory path: ")
files = os.listdir(directory)
sorted_files = sorted(files, key=lambda file: os.path.getmtime(os.path.join(directory, file))) # Sort files by modification time
for file in sorted_files:
    print(file)
'''

#71. Write a Python program to get a directory listing, sorted by creation date.
'''
import os
import sys
import time
path = sys.argv[1]\
    if len(sys.argv) == 2 else '.'
files = [(os.path.getctime(os.path.join(path, fn)), fn)
         for fn in os.listdir(path)
         if os.path.isfile(os.path.join(path, fn))]
for ctime, filename in sorted(files):
    print(time.ctime(ctime), filename)

#72. Write a Python program to get the details of the math module.
import math
math_ls = dir(math)
print(math_ls)


#73. Write a Python program to calculate the midpoints of a line.
# Input coordinates of the endpoints
x1, y1 = map(float, input("Enter the coordinates of the first point (x1, y1): ").split(','))
x2, y2 = map(float, input("Enter the coordinates of the second point (x2, y2): ").split(','))
midpoint_x = (x1 + x2) / 2
midpoint_y = (y1 + y2) / 2
# Output the midpoint
print("The midpoint of the line segment is: ",midpoint_x, midpoint_y)

#74. Write a Python program to hash a word.



#75. Write a Python program to get the copyright information and write Copyright information in Python code.
import sys
print("\nPython Copyright Information")
print(sys.copyright)


#76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
import sys
print("This is the name/path of the script:"), sys.argv[0]
print("Number of arguments:", len(sys.argv))
print("Argument List:", str(sys.argv))

#77. Write a Python program to test whether the system is a big-endian platform or a little-endian platform.
import sys
if sys.byteorder=="little":
    print("\n\nLittle-endian platform.")
else:
    print("Big=endian platform.")
'''
#78.  Write a Python program to find the available built-in modules.
import sys
import textwrap
module=",".join(sorted(sys.builtin_module_names))
print(textwrap.fill(module))

#79. Write a Python program to get the size of an object in bytes.



list=['A','']