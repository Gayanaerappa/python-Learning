import pandas as pd
import numpy as np

# -----------------------------
# 1. Create Sample Dataset
# -----------------------------

data = {
    "PatientID": range(1, 16),
    "Name": [
        "Amit", "Riya", "John", "Priya", "David",
        "Sara", "Rahul", "Anu", "Michael", "Neha",
        "Arjun", "Kiran", "Fatima", "Raj", "Sneha"
    ],
    "Age": [25, 34, 45, 29, 52, 41, 38, 22, 60, 31, 48, 36, 27, 55, 40],
    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Male", "Female", "Male", "Female"
    ],
    "Glucose": [85, 140, 120, 95, 160, 110, 130, 88, 170, 105, 150, 115, 90, 165, 125],
    "BloodPressure": [70, 90, 85, 72, 95, 80, 88, 65, 100, 75, 92, 82, 68, 98, 84],
    "BMI": [22.5, 31.2, 28.4, 24.1, 35.6, 26.3, 30.5, 21.8, 36.2, 25.0, 33.1, 27.4, 23.2, 34.8, 29.0],
    "Disease": [
        "No", "Yes", "Yes", "No", "Yes",
        "No", "Yes", "No", "Yes", "No",
        "Yes", "No", "No", "Yes", "Yes"
    ]
}

df = pd.DataFrame(data)

print("\n✅ ORIGINAL DATASET")
print(df)

# -----------------------------
# 2. Basic Info
# -----------------------------

print("\n✅ DATASET INFO")
print(df.info())

print("\n✅ STATISTICAL SUMMARY")
print(df.describe())

# -----------------------------
# 3. Data Cleaning Example
# -----------------------------

# Introduce missing values for demo
df.loc[3, "BMI"] = np.nan
df.loc[7, "Glucose"] = np.nan

print("\n✅ DATA WITH MISSING VALUES")
print(df)

# Fill missing values with mean
df["BMI"].fillna(df["BMI"].mean(), inplace=True)
df["Glucose"].fillna(df["Glucose"].mean(), inplace=True)

print("\n✅ AFTER HANDLING MISSING VALUES")
print(df)

# -----------------------------
# 4. Add Derived Columns
# -----------------------------

df["RiskScore"] = (df["Glucose"] * 0.4 +
                   df["BloodPressure"] * 0.3 +
                   df["BMI"] * 0.3)

print("\n✅ AFTER ADDING RiskScore COLUMN")
print(df[["Name", "Glucose", "BloodPressure", "BMI", "RiskScore"]])

# -----------------------------
# 5. Filtering Data
# -----------------------------

high_risk = df[df["RiskScore"] > 120]

print("\n✅ HIGH RISK PATIENTS")
print(high_risk[["Name", "Age", "RiskScore"]])

# -----------------------------
# 6. Grouping & Aggregation
# -----------------------------

print("\n✅ AVERAGE VALUES BY DISEASE STATUS")
grouped = df.groupby("Disease")[["Glucose", "BMI", "RiskScore"]].mean()
print(grouped)

# -----------------------------
# 7. Sorting
# -----------------------------

sorted_df = df.sort_values(by="RiskScore", ascending=False)

print("\n✅ PATIENTS SORTED BY RISK SCORE (DESC)")
print(sorted_df[["Name", "RiskScore"]])

# -----------------------------
# 8. Custom Queries
# -----------------------------

print("\n✅ PATIENTS ABOVE AGE 40")
print(df[df["Age"] > 40][["Name", "Age"]])

print("\n✅ FEMALE PATIENTS WITH DISEASE")
print(df[(df["Gender"] == "Female") & (df["Disease"] == "Yes")][["Name", "RiskScore"]])

# -----------------------------
# 9. Export Data
# -----------------------------

df.to_csv("processed_hospital_data.csv", index=False)

print("\n✅ Processed data saved to processed_hospital_data.csv")
