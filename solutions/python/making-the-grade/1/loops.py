"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    for index, score in enumerate(student_scores):
        student_scores[index] = round(score)
    return student_scores


def count_failed_students(student_scores):
    count = 0
    for socre in student_scores:
        if   socre <= 40:
            count += 1
    return count

def above_threshold(student_scores, threshold):
    updated_score = []
    for socre in student_scores:
        if   socre >= threshold:
            updated_score.append(socre)
    return updated_score

def letter_grades(highest):
    updated_score = []
    """Calcualting grade for D"""
    updated_score.append(41)
    difference = round( ( highest - 41 ) / 4 )
    """Calcualting grade for C"""
    updated_score.append(41+difference)
    """Calcualting grade for B"""
    updated_score.append(updated_score[1]+difference)
    """Calcualting grade for A"""
    updated_score.append(updated_score[2]+difference)
    return updated_score
    
def student_ranking(student_scores, student_names):
    list = []
    for index, student in enumerate(student_scores):
        list.append(str(index+1)+'. '+str(student_names[index]+': '+str(student)))
    return list

def perfect_score(student_info):
    for index, student in enumerate(student_info):
        if student[1] == 100:
            return student
    return []  
