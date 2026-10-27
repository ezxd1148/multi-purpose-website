"""
This just tool 2
"""


def main():
    """
    health checks
    """
    sample_list = [10000, 129321, 1, 12, 123, 4321, 54321]

    for i in sample_list:
        print(count_number(i))


def count_number(num: int):
    count = 0

    while num != 0:
        num //= 10
        count += 1
    return count


if __name__ == "__main__":
    main()
