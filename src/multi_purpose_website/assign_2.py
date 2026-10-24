
def main():
    print("This file is working as is")

def calculate_steps():

    try:
        num_of_students = int(input("Enter number of students: "))
    except:
        raise TypeError

    sum = 0
    count = 0

    for i in range(num_of_students):
        steps = int(input(f"Enter steps for student {i + 1}: "))

        if steps >= 10000:
            count += 1

        sum = sum + steps

    percent = float((count/num_of_students) * 100)
    average_steps = (sum/num_of_students)
    achieved_target = count
    not_achieved_target = num_of_students - count

    return average_steps, achieved_target, not_achieved_target, percent
    

if __name__ == "__main__":
    main()
