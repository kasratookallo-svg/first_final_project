# Curriculum Designing Program
# Made By Kasra Tookallo
# 11/28/2025
#------------------------------------------------------------------------------------------
from curriculum_dao import CurriculumDataAccess
from lesson_model import Curriculum

class LessonController:
    @staticmethod
    def save(lesson_name, lesson_code, teacher_name, lesson_credits):
        try:
            curiculum = Curriculum(
                lesson_name,
                lesson_code,
                teacher_name,
                lesson_credits
                 )
            curiculum_da = CurriculumDataAccess()
            curiculum_da.save(curiculum)
            return True , "Lesson Saved Successfully in Database."
        except Exception as e:
            return False , "Lesson saving Error !!!!"

    @staticmethod
    def edit(lesson_code, lesson_name, teacher_name, lesson_credits):
        try:
            curiculum = Curriculum(lesson_code, lesson_name, teacher_name, lesson_credits)
            curiculum_da = CurriculumDataAccess()
            curiculum_da.edit(curiculum)
            return True , "Lesson Edited Successfully in Database."
        except Exception as e:
            return False , f"Lesson Editing Error : {e}"

    @staticmethod
    def remove(lesson_code):
        try:
            curriculum_da = CurriculumDataAccess()
            curriculum_da.remove(lesson_code)
            return True , "Lesson Removed Successfully from Database."
        except Exception as e:
            return False , f"Lesson Removal Error : {e}"

    @staticmethod
    def find_all():
        try:
            curriculum_da = CurriculumDataAccess()
            return True , curriculum_da.find_all()
        except Exception as e:
            return False , f"Lesson Find All Error : {e}"

