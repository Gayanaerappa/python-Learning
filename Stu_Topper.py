students = [
    {"Name": "Ravi", "Maths": 78, "Science": 88, "English": 80},
    {"Name": "Anu", "Maths": 85, "Science": 79, "English": 86},
    {"Name": "Kiran", "Maths": 90, "Science": 92, "English": 85},
    {"Name": "Meena", "Maths": 67, "Science": 70, "English": 72}
]

subjects = ["Maths", "Science", "English"]

for subject in subjects:
    topper = max(students, key=lambda s: s[subject])
    
    print(subject, "Topper:")
    print("Name:", topper["Name"])
    print("Marks:", topper[subject])
    print("----------------------")
