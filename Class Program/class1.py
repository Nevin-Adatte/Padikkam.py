class student:
    def __init__(self,name: str,place: str,age: int):
        self.name = name
        self.place = place
        self.age = age
    def set_age(self,age: int):
        self.age = age
    def get_age(self):
        return self.age
    def display_student_details(self):
        print("Name :", self.name)
        print("Place :", self.place)
        print("Age :", self.age)