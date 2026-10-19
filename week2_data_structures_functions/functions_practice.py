"""Examples of core data structures and reusable functions."""

def sum_of_squares(numbers):
    """Return the sum of each number multiplied by itself."""
    return sum(number ** 2 for number in numbers)

def keep_at_least(values, minimum):
    """Return values greater than or equal to the given threshold."""
    return [value for value in values if value >= minimum]

def factorial(number):
    """Calculate a non-negative integer factorial recursively."""
    if number < 0:
        raise ValueError("Factorial is only defined here for non-negative integers.")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)

def main():
    scores = [42, 67, 81, 55, 93, 67]
    student = {"name": "Sample Student", "course": "Python", "scores": scores}
    coordinates = (21.1458, 79.0882)  # Example coordinates for Nagpur
    unique_scores = set(scores)
    doubled = list(map(lambda score: score * 2, scores))

    print("Student record:", student)
    print("Example tuple:", coordinates)
    print("Unique scores:", sorted(unique_scores))
    print("Doubled scores:", doubled)
    print("Scores at least 60:", keep_at_least(scores, 60))
    print("Sum of squares for [1, 2, 3]:", sum_of_squares([1, 2, 3]))
    print("Factorial of 5:", factorial(5))

if __name__ == "__main__":
    main()
