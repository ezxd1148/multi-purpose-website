"""
This is the sum & average calculator, like the name suggest it does what it do
"""
TOTAL_NUM = 0
NUM = 0
COUNT = 0

print("Welcome to the Sum & Average Calculator!")
print("Enter any NUMber to start and -1 to end:")

while NUM != -1:
    NUM = int(input())
    TOTAL_NUM += NUM
    if TOTAL_NUM == -1:
        TOTAL_NUM += 1
        break
    COUNT += 1

average = TOTAL_NUM / COUNT if COUNT > 0 else 0
print ("Sum: ", TOTAL_NUM)
print("Average: " , format(average, '.2f'))
