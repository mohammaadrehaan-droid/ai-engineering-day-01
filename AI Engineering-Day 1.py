print("=== AI Data Pipeline Simulator ===")


def data() -> dict:
    # Name input
    name = input("Enter your name: ")

    if name == "":
        raise ValueError("Name cannot be empty")

    # Age input
    try:
        age = int(input("Enter your age: "))

        if age < 1 or age > 100:
            raise ValueError("Age must be between 1 and 100")

    except ValueError as error:
        print("Error:", error)
        return {}

    # City input
    city = input("Enter your city: ")

    # Income input
    try:
        monthly_income = int(input("Enter your monthly income: "))

        if monthly_income < 0:
            raise ValueError("Income cannot be negative")

    except ValueError as error:
        print("Error:", error)
        return {}

    # Income category
    if monthly_income < 30000:
       print("category : Low = ",monthly_income)

    elif monthly_income >= 30000 and monthly_income < 100000:
        print("category : Medium = ",monthly_income)

    else:
        print("invalid category")

    return {
        "name": name,
        "age": age,
        "city": city,
        "monthly_income": monthly_income,
    
    }
 
result= data()
print(data())