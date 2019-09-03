#MIT FINAL EXAM
#PROBLEM 6-1

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

#PROBLEM 6-1
class ArrogantProfessor(Professor): 
    def say(self, stuff):
        return Person.say(self, 'It is obvious that ') + Person.say(self, stuff)
    def lecture(self, stuff): 
        return 'It is obvious that ' + Person.say(self, stuff)

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

ae.lecture('the sky is blue')
#PART 1 output is
#It is obvious that eric says: the sky is blue
