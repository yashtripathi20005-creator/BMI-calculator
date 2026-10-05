def calculate_bmi(weight, height):
    """
    Calculate BMI using weight in kilograms and height in meters.
    """
    return weight / (height ** 2)


def get_bmi_category(bmi):
    """
    Determine the BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("===== BMI Calculator =====")

    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than 0.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print("\n===== Result =====")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
