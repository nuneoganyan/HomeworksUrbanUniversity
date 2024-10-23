grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = []
students_in_journal = list(students)
students_in_journal.sort()
my_students = {}
i = 0
while i < len(students_in_journal) :
    average_grades.append(float(sum(grades[i])/len(grades[i])))
    my_students[students_in_journal[i]] = average_grades[i]
    i = i + 1
print(my_students)