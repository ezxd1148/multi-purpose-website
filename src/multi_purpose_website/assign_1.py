"""
    assign_1.py, calculates amount of flour and donate to old folk house
"""

def main():
    """
    Health Check
    """
    sample_list = [10, 20.2, 30, 24, 3.0, 50, 20, 50, 60, 90]
    total_kg, average_kg, heavy_flour = calculates_flour(sample_list)

    print("Total KG: ", total_kg)
    print("Average KG: ", average_kg)
    print("Heave Flour: ", heavy_flour)

def calculates_flour(flour_weights: list[float]):
    """
    Handle the int range in html side
    """

    for i in flour_weights:
        if !(0 <= i <= 100):
            raise ValueError("Flour weight should only be in 0 - 100 range")

    if not flour_weights:
        raise ValueError("Flour list cannot be empty")

    total_kg = sum(flour_weights)
    average_kg = total_kg/len(flour_weights)
    heavy_flour = max(flour_weights)

    return total_kg, average_kg, heavy_flour

if __name__ == "__main__":
    main()
