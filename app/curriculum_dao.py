# Curriculum Designing Program
# Made By Kasra Tookallo
# 11/28/2025

import sqlite3
class CurriculumDataAccess:

    def save(self,lesson):
        with sqlite3.connect("curriculum.db") as connection:
            cursor = connection.cursor()
            cursor.execute("insert into lessons (lesson_name, lesson_code, teacher_name, lesson_credits) values(?,?,?,?)",
                           [lesson.name ,lesson.code , lesson.teacher , lesson.credits ])
            connection.commit()

    def edit(self,lesson):
        with sqlite3.connect("curriculum.db") as connection:
            cursor = connection.cursor()
            cursor.execute("update lessons set lesson_name=?, lesson_credits=?, teacher_name=?, lesson_credits=? where lesson_code=? ",
                           [lesson.lesson_name , lesson.lesson_credits ,lesson.teacher_name ,lesson.lesson_code])
            connection.commit()

    def remove(self,lesson_code):
        with sqlite3.connect("curriculum.db") as connection:
            cursor = connection.cursor()
            cursor.execute("delete from lessons where lesson_code=?",[lesson_code])
            connection.commit()

    def find_all(self):
        with sqlite3.connect("curriculum.db") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from lessons order by lesson_name")
            return cursor.fetchall()
