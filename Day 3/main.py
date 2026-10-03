
import csv
import json
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Program started")

valid_data = []

try:
    with open("student.csv", "r", newline="") as file:

        logging.info("CSV file opened successfully")

        reader = csv.DictReader(file)

        for row in reader:

            try:
                row["Age"] = int(row["Age"])

                if row["Age"] < 0:
                    raise ValueError("Age cannot be negative")

                valid_data.append(row)

                logging.info("Data processed successfully")

            except ValueError:
                logging.error("Invalid age found")

except FileNotFoundError:
    logging.error("Student CSV file not found")


with open("student.json", "w") as file:
    json.dump(valid_data, file, indent=4)

logging.info("Data saved to JSON successfully")

print(json.dumps(valid_data, indent=4))

logging.info("Program completed")