
import re

# Molding Studies
class   Curriculum:
    # Method
    def __init__(self, lesson_name, lesson_code, teacher_name , lesson_credits):
        # Property
        self.lesson_name = lesson_name
        self.lesson_code = lesson_code
        self.teacher_name = teacher_name
        self.lesson_credits = lesson_credits
        self.lesson_list = []
#---------------------------------------------------------------------------------------------------
                                    # Encapsulation
    #def get_lesson_name(self):
     #   return self.lesson_name

    #def get_lesson_code(self):
     #   return self.lesson_code

    #def get_teacher_name(self):
     #   return self.teacher_name

    #def get_lesson_credits(self):
     #   return self.lesson_credits

    #def set_lesson_name(self, lesson_name):
     #   print("Setter activated.")
      #  if not re.match(r"^[a-zA-Z\s]{3,30}$",self.lesson_name):
       #     raise NameError("Lesson Name must be letter and space !!!!")
        #self.__lesson_name = lesson_name

    #def set_lesson_code(self, lesson_code):
     #   print("Setter activated.")
      #  if not (type(self.lesson_code) == int and self.lesson_code > 0):
       #     raise NameError("Code Error!!!!")
        #self.__lesson_code = lesson_code

    #def set_teacher_name(self, teacher_name):
     #   print("Setter activated.")
      #  if not (r"^[a-zA-Z\s]{3,30}$", self.teacher_name):
       #     raise NameError("Teacher Name Error!!!!")
        #self.__teacher_name = teacher_name

    #def set_lesson_credits(self, lesson_credits):
     #   print("Setter activated.")
      #  if not (type(self.lesson_credits) == int and self.lesson_credits > 0):
       #     raise NameError("Lesson Credits Error!!!!")
        #self.__lesson_credits = lesson_credits


    #lesson_name = property(get_lesson_name, set_lesson_name)
    #lesson_code = property(get_lesson_code, set_lesson_code)
    #teacher_name = property(get_teacher_name, set_teacher_name)
    #lesson_credits = property(get_lesson_credits, set_lesson_credits)
#--------------------------------------------------------------------------------------------------------
    # Method_Show Result
    def save(self):
        print(f"INFO :   {self.lesson_name:10} , {self.lesson_code:} \t\t ,{self.teacher_name:10} , {self.lesson_credits}")

    # Method_function
    def validation(self ):

        if not re.match(r"^[a-zA-Z\s]{3,30}$",self.lesson_name):
            raise NameError("Lesson Name must be letters and space!!!!")

        if not (type(self.lesson_code) == int and self.lesson_code > 0):
            raise NameError("Code must be a positive integer!!!!")

        if not re.match(r"^[a-zA-Z\s]{3,30}$", self.teacher_name):
            raise NameError("Teacher Name must be letters and space!!!!")

        if not (type(self.lesson_credits) == int and self.lesson_credits > 0):
            raise NameError("Lesson Credits must be a positive integer!!!!")

        return True

    # Representation
    def __repr__(self):
        return f" \n{self.lesson_name} (Code :{self.lesson_code:^5})\t--->>\t{self.lesson_credits}\t( Credits ) \nTeacher's Name :\t\t {self.teacher_name}\n "

    def to_tuple(self):
        return tuple((self.lesson_name, self.lesson_code, self.teacher_name, self.lesson_credits))
