students = [
    {"name": "Lara",  "age": 23, "track": "AI",   "hours_studied": 40, "scores": [85, 90, 78]},
    {"name": "Omar",  "age": 31, "track": "Data", "hours_studied": 12, "scores": [60, 55, 70]},
    {"name": "Rim",   "age": 27, "track": "AI",   "hours_studied": 55, "scores": [95, 88, 92]},
    {"name": "Karim", "age": 19, "track": "Web",  "hours_studied": 8,  "scores": [50, 65, 40]},
    {"name": "Nour",  "age": 25, "track": "AI",   "hours_studied": 30, "scores": [75, 80, 85]},
    {"name": "Sami",  "age": 35, "track": "Data", "hours_studied": 48, "scores": [88, 91, 79]},
]
# Part 1: Exploring the Data
#1 - Print the names of the first and last students in the list.
print(students[0]["name"])
print(students[-1]["name"])

#2 - Print the average score of the student named "Rim".
for student in students:
    if student["name"] == "Rim":
        Rim_scores = student["scores"]
        average_Rim_score = sum(Rim_scores) / len(Rim_scores)
        print("Rim's average score:", round(average_Rim_score, 2))

#3 - Loop and print the names of all students 
for student in students:
    print(student["name"])

# Part 2: Filtering
# 4- Filter AI Track using a standard loop.
ai_students_loop = []
for student in students:
    if student["track"] == "AI":
        ai_students_loop.append(student)
print(len(ai_students_loop))

# 5- Filter AI Track using a list comprehension.
ai_students_comp = [student for student in students if student["track"] == "AI"]
print(ai_students_comp)

# 6 - Names of students who have studied more than 30 hours.
high_hours_students = [
    student["name"] for student in students 
    if student["hours_studied"] > 30]
print("Studied > 30 hours:", high_hours_students)

# # print(type(high_hours_students))

# 7 - Older than 24 AND in the AI track
older_ai_students = [
    student for student in students 
    if student["age"] > 24 and student["track"] == "AI"]
print("Older than 24 and in AI track:", older_ai_students)

# Part 3: Aggregation
# 8 - Average age of all students
avg_age = sum(student["age"] for student in students) / len(students)
print("Average age of all students:", round(avg_age, 2))

# 9 - Total hours studied
total_hours_studied = sum(student["hours_studied"] for student in students)
print("Total hours studied:", total_hours_studied)

#10 - Find student who studied the most hours
most_hours_student = students[0]
for student in students:
    if student["hours_studied"] > most_hours_student["hours_studied"]:
        most_hours_student = student
print(
    f"Most hours studied: {most_hours_student['name']} ({most_hours_student['hours_studied']} hours)"
)

# 11 - Final grade per student 
for student in students:
    final_grade = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']}: {round(final_grade, 1)}")


# Part 4 : Transforming
#12 - Reshape into list of dictionaries with name and average score
transformed_data = [
    {"name": s["name"], "average_score": round(sum(s["scores"]) / len(s["scores"]), 1)}
    for s in students
]
print("Transformed data:", transformed_data)

# 13 dictionary that maps each track to the number of students
track_counts = {}
for student in students:
    track = student["track"]
    if track in track_counts:
        track_counts[track] += 1
    else:
        track_counts[track] = 1
print("Track counts:", track_counts)

# 14 - Create a set of all the unique tracks in the dataset
# A set is ideal here because it automatically eliminates duplicate track names, and ensures only unique values remain.
unique_tracks = {student["track"] for student in students}
print("Unique tracks:", unique_tracks)

# Part 5: Reusable Functions (don't repeat yourself)
# 15 - Write a function `filter_by_track(students, track)`
def filter_by_track(students, track):
    result = []
    for student in students:
        if student["track"] == track:
            result.append(student)
    return result
# Test the function  with "AI" tracks
print("AI Track:", filter_by_track(students, "AI"))

# Test the function with  "Data" tracks
print("Data Students:", filter_by_track(students, "Data"))

# 16 - wrtite a function `average_score(student)` that takes a student dictionary and returns their average score. 
def average_score(student):
    scores = student["scores"]
    return sum(scores) / len(scores)
print("Average score of Nour:", average_score(students[2]))  # Testing Nour, who is the third student in the list
print("Average score of Karim:", average_score(students[1]))  # Testing Karim, who is the second student in the list

# 17 - Write a function `top_student(students)` that returns the name of the student with the highest average score. 
# (Use the function from #16 inside it — functions calling functions.)
def top_student(students):
    best_student = students[0]
    for student in students:
        if average_score(student) > average_score(best_student):
            best_student = student
    return best_student["name"]


# Test the function
print ("Top student:", top_student(students))

# 18 - Write a function `summary(students)` that returns a dictionary full overview.
def summary(students):
    total_students = len(students)
    avg_age = sum(student["age"] for student in students) / total_students
    tracks = {student["track"] for student in students}
    
    return {
        "total_students": total_students,
        "average_age": round(avg_age, 2),
        "tracks": tracks
    }
    
print(summary(students))    

 
