def score_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def score_grade2(score):
    if score >= 90:
        return "A"
    else:
        if score >= 80:
            return "B"
        else:
            if score >= 70:
                return "C"
            else:
                if score >= 60:
                    return "D"
                else:
                    return "F"


print(score_grade(30), score_grade2(30))
print(score_grade(80), score_grade2(80))
print(score_grade(65), score_grade2(65))
print(score_grade(92), score_grade2(92))
print(score_grade(77), score_grade2(77))
