#学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名：{self.name}|语文：{self.chinese}|数学：{self.math}|英语：{self.english}|总分：{self.chinese + self.math + self.english}"

    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


class Enumangement:
     system_version = "1.0"
     system_name = "教务管理系统"

     def __init__(self):
        self.student_list = []

#添加学生成绩
     def add_student(self):
         name = input("请输入学生姓名：")
         for s in self.student_list:
             if s.name == name:
                 print("该学生已存在，添加失败！")
                 return

         chinese = int(input("请输入学生语文成绩："))
         math = int(input("请输入学生数学成绩："))
         english = int(input("请输入学生英语成绩："))

         if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
             stu = Student(name,chinese,math,english)
             self.student_list.append(stu)
             print("添加成功")
         else:
             print("输入的分数有误，添加失败！")

#修改学生成绩
     def update_student(self):
         name = input("请输入学生姓名：")

         for s in self.student_list:
             if s.name == name:
                 print(f"当前成绩：{s}")

                 chinese = int(input("请输入修改后语文成绩："))
                 math = int(input("请输入修改后数学成绩："))
                 english = int(input("请输入修改后英语成绩："))

             if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                 stu = Student(name, chinese, math, english)
                 s.update_score(chinese,math,english)
                 print("修改成功")
                 print(f"修改后成绩：{s}")
                 return
             else:
                 print("输入的分数有误，添加失败！")
                 return
         print("未找到该学生，修改失败")

#删除学生成绩
     def delete__student(self):
         name = input("请输入要删除的学生姓名：")

         for s in self.student_list:
             if s.name == name:
                 self.student_list.remove(s)
                 print("删除成功")
                 return
             print("未找到该学生，删除失败")

#查询指定学生成绩
     def query_student(self):
         name = input("请输入需要查询学生信息的姓名")
         for s in self.student_list:
             if s.name == name:
                 print(s)
                 return
         print("未找到该学生")

#展示全部学生信息
     def show_all_student(self):
         for s in self.student_list:
             print(s)

     def run(self):
         print(f"欢迎使用{self.system_name} 系统的版本号：{self.system_version}")
         print()
         print("———————————————————————————————————————————————————————————————————————————————————————")
         print("——1.添加学生成绩  2.修改学生成绩  3.删除学生成绩  4.查询指定学生成绩  5.展示全部学生信息  6.退出系统——")
         print("———————————————————————————————————————————————————————————————————————————————————————")

         while True:
             choice = input("请输入您的选择(1~6)：")
             match choice:
                 case "1":
                     self.add_student()
                 case "2":
                     self.update_student()
                 case "3":
                     self.delete_student()
                 case "4":
                     self.query_student()
                 case "5":
                     self.show_all_student()
                 case "6":
                     print("欢迎下次再来")
                     break
                 case _:
                     print("输入有误，请重新输入")


if __name__ == '__main__':
    test_Enumangement = Enumangement()
    test_Enumangement.run()
