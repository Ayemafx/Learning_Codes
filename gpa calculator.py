# Code for printing gpa without using if statement

marks = []

for x in range(7):
    m = int(input(f"Enter subj {x + 1} marks: "))
    while (m > 100) or (m < 0):
        m = int(input(" ---Please Enter Valid marks---: "))
    marks.append(m)


def calc_grade(m):
    # Grades
    f = ["F"] * 50
    d = ["D"] * 3
    dp = ["D+"] * 4
    cm = ["C-"] * 4
    c = ["C"] * 3
    cp = ["C+"] * 4
    bm = ["B-"] * 3
    b = ["B"] * 4
    bp = ["BP"] * 5
    am = ["A-"] * 5
    a = ["A"] * 5
    ap = ["A+"] * 11
    grade = f + d + dp + cm + c + cp + bm + b + bp + am + a + ap

    # Grade Points
    f = [0.0] * 50
    d = [1.0] * 3
    dp = [1.4] * 4
    cm = [1.8] * 4
    c = [2.0] * 3
    cp = [2.4] * 4
    bm = [2.8] * 3
    b = [3.0] * 4
    bp = [3.4] * 5
    am = [3.8] * 5
    a = [4.0] * 5
    ap = [4.0] * 11
    gp = f + d + dp + cm + c + cp + bm + b + bp + am + a + ap

    return (grade[m], gp[m])


for m in marks:
    g, gp = calc_grade(m)
    print(f"Grade = {g} | GradePoints = {gp}")








