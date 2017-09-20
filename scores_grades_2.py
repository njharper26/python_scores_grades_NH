import random 

def scores_grades(flr, ceil, total):
    count = 1
    while count <= total:
        score = random.randint(flr, ceil)
        if score < 70:
            print "Score: ", str(score) + "; Your grade is D"
        elif score < 80:
            print "Score: ", str(score) + "; Your grade is C"
        elif score < 90:
            print "Score: ", str(score) +  "; Your grade is B"
        else:
            print "Score: ", str(score) + "; Your grade is A"
        count += 1

    return "end of the program..."

print scores_grades(60, 100, 10)

    