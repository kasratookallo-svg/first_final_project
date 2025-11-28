from app.curriculum_dao import CurriculumDataAccess
from course_controller import LessonController
from lesson_model import Curriculum
curriculum = LessonController()

print(curriculum.save("Math"  , 123 ,"Akbari", 3))