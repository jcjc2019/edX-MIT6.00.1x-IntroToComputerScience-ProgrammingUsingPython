#MIT FINAL EXAM
#PROBLEM 6 original code

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)
#original 
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return 'It is obvious that ' + self.say(stuff)
        
#PROBLEM 6-1
class ArrogantProfessor(Professor): 
    def say(self, stuff):
        return Person.say(self, 'It is obvious that ') + Person.say(self, stuff)
    def lecture(self, stuff): 
        return 'It is obvious that ' + Person.say(self, stuff)
        
#PROBLEM 6-2
class ArrogantProfessor(Professor): 
    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)

#PROBLEM 6-3
#Change the Professor class definition in order to achieve this.
class Professor(Lecturer): 
    def say(self, stuff):
        return 'Prof.' + self.name + 'says:' + Lecturer.lecture(stuff)

#BLOW ARE TESTS
e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

e.say('the sky is blue')
le.say('the sky is blue')
le.lecture('the sky is blue')
pe.say('the sky is blue')
pe.lecture('the sky is blue')
ae.say('the sky is blue')
#PART 1 output is
#eric says: It is obvious that eric says: the sky is blue
#PART 2 output is 
#eric says: It is obvious that I believe that eric says: the sky is blue
#PART 3 output is 
#Prof. eric says: I believe that eric says: the sky is blue 
ae.lecture('the sky is blue')
#PART 1 output is
#It is obvious that eric says: the sky is blue
#PART 2 output is
#It is obvious that I believe that eric says: the sky is blue
#PART 3 output is 
#Prof. eric says: It is obvious that I believe that eric says: the sky is blue 