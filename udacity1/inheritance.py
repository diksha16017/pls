class Parent():
    def __init__(self,last_name,eye_color):
        print("parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("last name : "+self.last_name)
        print ("eye color : "+self.eye_color)

class Child(Parent):
    def __init__(self,last_name,eye_color,toys):
        Parent.__init__(self, last_name, eye_color)
        print ("child constructor called")
        #Parent.__init__(self,last_name,eye_color)
        self.toys = toys

    def show_info(self):
        Parent.show_info(self)
        print("toys : "+str(self.toys))

papa = Parent("garg","black")
print(papa.last_name)
papa.show_info()

dia = Child("garg","black",6)
dia.show_info()

print(dia.last_name)
print(dia.toys)