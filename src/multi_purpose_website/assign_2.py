"""
assign_2.py, student step calculate
"""

def main():
    """
    health check
    """
    print("This file is working as is")
    calculate_steps(2)

def calculate_steps(num_of_students):
    """
    calculate steps of number of students
    """

    total_steps = 0
    count = 0

    for i in range(num_of_students):
        steps = int(input(f"Enter steps for student {i + 1}: "))

        if steps >= 10000:
            count += 1

        total_steps = total_steps + steps

    percent = float((count/num_of_students) * 100)
    average_steps = total_steps/num_of_students
    achieved_target = count
    not_achieved_target = num_of_students - count

    return average_steps, achieved_target, not_achieved_target, percent


if __name__ == "__main__":
    main()
