# ==========================================
# Python for AI Engineering - Day 1
# ==========================================

# Topics Covered:
# 1. Functions
# 2. Parameters and Arguments
# 3. Return Statement
# 4. Default Parameters
# 5. Multiple Returns
# 6. Modules [NOT DONE]
# 7. Imports
# 8. Error Handling
# 9. Type Hints
# 10. Clean Code
# 11. Single Responsibility Principle (SRP)
# 12. Mini Project - AI Data Pipeline Simulator
# 13. Git and GitHub

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
