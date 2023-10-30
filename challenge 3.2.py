class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
def sort_students(student_list):
  sorted_students=sorted(student_list, key=lambda student:student.cgpa, reverse=True)
  return sorted_students
students=[Student("riya","A101","7.8"), Student("dino","B102","8.9"), Student("alice","C103","7.5"), Student("madhu","D104","6.5")]
sorted_students=sort_students(students)
for student in sorted_students:
  print("Name: {}, Roll number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))