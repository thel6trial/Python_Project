class Student:
    #gồm 4 thông tin: tên, id, điểm 1 và điểm 2
    def __init__(self, name, id, mark1, mark2):
        self.name = name
        self.id = id
        self.mark1 = mark1
        self.mark2 = mark2
    #thêm học sinh vao danh sách
    def add(self, name, id, mark1, mark2):
        student1 = Student(name, id, mark1, mark2)
        list_student.append(student1)
    #tìm kiếm id học sinh
    def search(self,id1):
        for i in range(len(list_student)):
            if list_student[i].id == id1:
                return i
    #xoá học sinh theo id
    def delete(self, id1):
        i = student1.search(id1)
        del list_student[i]
    #update thông tin học sinh
    def update(self, id1, id2):
        i = student1.search(id1)
        no = id2
        list_student[i].id = no
    #hiển thị thông tin
    def display(self, student1):
        print("Thông tin học sinh: \n")
        print("Tên học sinh: ", student1.name)
        print("ID học sinh: ", student1.id)
        print("Điểm số học kì 1: ", student1.mark1)
        print("Điểm số học kì 2: ", student1.mark2)


list_student = []

student1 = Student('', 0, 0, 0)

button = int(input("Nhập chức năng"))
#Nếu chức năng 1, nhập danh sách các học sinh
if button == 1:
    student1.add('A', 1, 10, 9)
    student1.add('B', 2, 9, 9)
    student1.add('C', 3, 8, 10)

#Nếu chức năng 2, hiển thị thông tin học sinh
elif button == 2:
    for i in range(len(list_student)):
        student1.display(list_student[i])

# nếu chức năng 3, tìm kiếm học sinh
elif button == 3:
    id2 = int(input())
    s = student1.search(id2)
    student1.display(list_student[s])
#nếu chức năng 4, xoá học sịnh
elif button == 4:
    id2 = int(input())
    student1.delete(id2)
    print(len(list_student))
    print("Danh sách mới sau khi xoá")
    for i in range(len(list_student)):
        student1.display(list_student[i])

else:
    print("Chức năng chưa phù hợp")
