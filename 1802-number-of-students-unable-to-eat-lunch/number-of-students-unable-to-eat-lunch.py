class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        flag = 0

        while students and flag < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                flag = 0
            else:
                temp = students.pop(0)
                students.append(temp)
                flag += 1

        return len(students)