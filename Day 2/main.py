from validation import clean_text
from data import create_record
text = input("Enter you text: ")
cleaned_text = clean_text(text)
print(cleaned_text)
created_record = create_record(text)
print(created_record)