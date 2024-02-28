# Created by Calvin Dennis - 2/27/2024
# For use in Hafner's Discrete Math Class
# calvind151504@gmail.com

# ENTER GRADES HERE - ALL EMPTY FIELDS WILL BE IGNORE BY PROGRAM AND NOT CALCULATED (YOU CAN LEAVE THEM BLANK)
# ENSURE GRADES ARE ENTERED AS INT/FOAT - NOT STRING
# REPLACE 'None' WITH YOUR GRADE
# Save your file and update it over the semester :)

# HOMEWORKS
homework_grades = [

    # HW 2.1
    {'score': 8, 'total': 10},

    # HW 2.3
    {'score': 8, 'total': 10},

    # HW 2.4
    {'score': 6, 'total': 5},

    # Homework 3.3
    {'score': 10, 'total': 10},

    # HW 4.3
    {'score': None, 'total': 10},

    # HW 4.5
    {'score': None, 'total': 10},

    # HW 4.7A
    {'score': None, 'total': 10},

    # HW 4.7B
    {'score': None, 'total': 5},

    # HW 5.2
    {'score': None, 'total': 10},

    # HW 5.3
    {'score': None, 'total': 10},

    # HW 5.4
    {'score': None, 'total': 10},

]

# TEST GRADES
test_grades = [

    # TOTAL POINTS FOR TESTS 3-7 WERE UNKNOWN AT TIME OF WRITING - ENSURE 'None' IN
    # 'total' IS REPLACED FOR GRADE TO COUNT!

    # Test 1
    {'score': 44, 'total': 50},

    # Test 2
    {'score': 46, 'total': 48},

    # Test 3
    {'score': None, 'total': None},
    
    # Test 4
    {'score': None, 'total': None},

    # Test 5
    {'score': None, 'total': None},

    # Test 6
    {'score': None, 'total': None},

    # Test 7 (If there is one)
    {'score': None, 'total': None},

]

# FINAL EXAM
# NOT SURE HOW MUCH FINAL WILL BE WORTH... UPDATE final_exam_possible AS NECESSARY :)
final_exam_achieved = None
final_exam_possible = None

try:
    final_grade = (final_exam_achieved / final_exam_possible) * 100
    print('=== FINAL EXAM ===')
    print(f'- Achieved: {final_exam_achieved}\n- Possbile: {final_exam_possible}')
    print(f'- Score: {round(final_grade, 2)}%\n')

except TypeError:
    final_grade = None
    print('=== FINAL EXAM ===\n- Not entered (not an error)\n')


def main(hw_grades, test_grades, final = final_grade):

    hw = homework_grade_calculation(hw_grades)
    test = test_grade_calculation(test_grades)

    print(f'=== FINAL CALCULATED GRADE ===\n- Your total cumulative score is: {round(final_calculation(hw, test, final), 2)}%')
    return 0


# Calculate unweighted overall hw grade %
def homework_grade_calculation(grades):
    total_achieved = 0
    total_possible = 0

    for i in grades:
        if i['score'] != None and i['total'] != None:
            total_achieved += i['score']
            total_possible += i['total']

    score = (total_achieved / total_possible) * 100

    print('=== HOMEWORK ===')
    print(f'- Achieved: {total_achieved}\n- Possbile: {total_possible}')
    print(f'- Score: {round(score, 2)}%\n')
    return score

# Calculated unweighted overall test grade %
def test_grade_calculation(grades):
    total_achieved = 0
    total_possible = 0

    for i in grades:
        if i['score'] != None and i['total'] != None:
            total_achieved += i['score']
            total_possible += i['total']

    score = (total_achieved / total_possible) * 100

    print('=== TESTS ===')
    print(f'- Achieved: {total_achieved}\n- Possbile: {total_possible}')
    print(f'- Score: {round(score, 2)}%\n')
    return score



def final_calculation(hw, test, final):

    # No final grade in calculation
    if final != None:
        hw *= 0.15
        test *= 0.60
        final *= 0.25

        return ((hw + test + final) / 100) * 100
    
    # Final grade in calculation
    else:
        hw *= 0.15
        test *= 0.60

        return ((hw + test) / 75) * 100


main(homework_grades, test_grades)