import pandas as pd
import numpy as np


# ==========================================
# STEP 1: CSV FILE LOAD KARNA
# Step 1: Load the CSV file
# ==========================================

df = pd.read_csv("students_raw.csv")

# Original data ko display karna
# Display the original data
print("Original Data:")
print(df)


# ==========================================
# STEP 2: DATA INSPECT KARNA
# Step 2: Inspect the data
# ==========================================

# Pehli 3 rows dekhna
# View the first 3 rows
print("\nFirst 3 Rows:")
print(df.head(3))

# Aakhri 2 rows dekhna
# View the last 2 rows
print("\nLast 2 Rows:")
print(df.tail(2))

# Rows aur columns ki quantity dekhna
# Check the number of rows and columns
print("\nShape:")
print(df.shape)

# Saare column names dekhna
# View all column names
print("\nColumns:")
print(df.columns)

# Har column ka data type dekhna
# Check the data type of each column
print("\nData Types:")
print(df.dtypes)

# DataFrame ki basic information dekhna
# View basic information about the DataFrame
print("\nData Info:")
df.info()

# Numerical data ka statistical summary dekhna
# View the statistical summary of numerical data
print("\nData Description:")
print(df.describe())


# ==========================================
# STEP 3: MISSING VALUES CHECK KARNA
# Step 3: Check for missing values
# ==========================================

# Har column mein missing values count karna
# Count missing values in each column
print("\nMissing Values:")
print(df.isna().sum())


# ==========================================
# STEP 4: MISSING VALUES HANDLE KARNA
# Step 4: Handle missing values
# ==========================================

# Age ki missing value ko average age se fill karna
# Fill missing Age values with the average Age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Education ki missing value ko "Unknown" se fill karna
# Fill missing Education values with "Unknown"
df["Education"] = df["Education"].fillna("Unknown")

print("\nData After Filling Missing Values:")
print(df)


# ==========================================
# STEP 5: DUPLICATE DATA REMOVE KARNA
# Step 5: Remove duplicate data
# ==========================================

# Duplicate rows ko identify karna
# Identify duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated())

# Duplicate rows ko remove karna
# Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)


# ==========================================
# STEP 6: FILTERING
# Step 6: Filter the data
# ==========================================

# Sirf 18 ya us se zyada age wale students select karna
# Select only students aged 18 or above
df = df[df["Age"] >= 18]

print("\nAfter Age Filtering:")
print(df)


# ==========================================
# STEP 7: DATA PROCESSING WITH FUNCTION
# Step 7: Process data using a function
# ==========================================

# Age ke according group banane wala function
# Function to create an age group
def age_group(age):

    # 21 ya us se zyada age ko 21+ group mein rakhna
    # Put ages 21 or above into the 21+ group
    if age >= 21:
        return "21+"

    # Baqi ages ko 18-20 group mein rakhna
    # Put other ages into the 18-20 group
    else:
        return "18-20"


# Function ko Age column ki har value par apply karna
# Apply the function to every value in the Age column
df["Age_Group"] = df["Age"].apply(age_group)

print("\nAfter Processing:")
print(df)


# ==========================================
# STEP 8: DATA SORT KARNA
# Step 8: Sort the data
# ==========================================

# Age ko badi se chhoti order mein sort karna
# Sort Age from highest to lowest
df = df.sort_values("Age", ascending=False)

print("\nSorted Data:")
print(df)


# ==========================================
# STEP 9: NUMPY CALCULATIONS
# Step 9: Perform numerical calculations with NumPy
# ==========================================

# Pandas Age column ko NumPy array mein convert karna
# Convert the Pandas Age column into a NumPy array
ages = np.array(df["Age"])

print("\nNumPy Calculations:")

# Total age calculate karna
# Calculate the total age
print("Total Age:", ages.sum())

# Average age calculate karna
# Calculate the average age
print("Average Age:", ages.mean())

# Maximum age find karna
# Find the maximum age
print("Maximum Age:", ages.max())

# Minimum age find karna
# Find the minimum age
print("Minimum Age:", ages.min())


# ==========================================
# STEP 10: VALUE COUNTS
# Step 10: Count unique values
# ==========================================

# Har course mein kitne students hain ye count karna
# Count how many students are in each course
print("\nStudents Per Course:")
print(df["Course"].value_counts())


# ==========================================
# STEP 11: GROUPBY
# Step 11: Group the data
# ==========================================

# Har course ke students ki average age calculate karna
# Calculate the average age for each course
print("\nAverage Age Per Course:")
print(df.groupby("Course")["Age"].mean())


# ==========================================
# STEP 12: FINAL CSV SAVE KARNA
# Step 12: Save the final processed data
# ==========================================

# Processed DataFrame ko new CSV file mein save karna
# Save the processed DataFrame into a new CSV file
df.to_csv("students_processed.csv", index=False)

print("\nProcessing Completed!")
print("Final data saved in students_processed.csv")