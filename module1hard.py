grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_students = sorted(students)
grades_1 = []
for i in grades:
    grades_1.append(sum(i)/len(i))

grade_book = dict(zip(sort_students, grades_1))
print(grade_book)

