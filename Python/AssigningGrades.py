def find_score():
    scores = input("Enter the numbers: ")
    scoreslist= scores.split()
    for c in range(0,len(scoreslist)):
        scoreslist[c] = int(scoreslist[c])
    return scoreslist
def get_best_grade(scores):
    bestgrade = max(scores)
    return bestgrade
def assign_grade(bestgrade, score):
    if score >= (bestgrade-10):
        grade='A'
    elif ((score >= (bestgrade-20)) and (score < (bestgrade-10))):
        grade='B'
    elif ((score >= (bestgrade-30)) and (score < (bestgrade-20))):
        grade='C'
    elif ((score >= (bestgrade-40)) and (score < (bestgrade-30))):
        grade='D'
    else:
        grade='F'
    return grade
def main():
    scores = find_score()
    bestgrade=int(get_best_grade(scores))
    n=0
    for c in scores:
        grade = assign_grade(bestgrade, int(c))
        print("Student", str(n),"score is", str(c),"and grade is", grade )
        n+=1
main()