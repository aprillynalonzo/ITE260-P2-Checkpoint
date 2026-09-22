def compute_mean_score(score1, score2, score3):
    total_points = score1 + score2 + score3
    average_result = total_points / 3
    return round(average_result, 2)
    
def get_performance_level(average_score):
    if average_score >=90:
        return "Excellent"
    elif average_score >=80:
        return "Very Good"
    elif average_score >=75:
        return "Passed"
    else:
        return "Failed"
        
print ("STUDENT ACTIVITY SCORE SYSTEM")

total_students=int(input("Enter number of students to process: "))
while total_students < 3:
    print("Enter 3 or more students")
    total_students = int(input("Enter number of students to process: "))

for student_number in range(1, total_students + 1):
    print(f"\n==== STUDENT {student_number} ====")
    
    full_name = input("Student Name: ")
    activity_1 = float(input("Score for Activity 1: "))
    activity_2 = float(input("Score for Activity 2: "))
    activity_3 = float(input("Score for Activity 3: "))
    final_average = compute_mean_score(activity_1, activity_2, activity_3)
    
    standing = get_performance_level(final_average)
    
    print("\n----- RESULT -----")
    print(f"Name: {full_name}")
    print(f"Activity 1: {activity_1}")
    print(f"Activity 2: {activity_2}")
    print(f"Activity 3: {activity_3}")
    
    print(f"Average   : {final_average}")
    print(f"Status    : {standing}")

print("\n All student records processed successfully.")

        
    
