class Person:
    def info(self):
        print("I am a Person")

class Worker:
    def work(self):
        print("I am Working")

class Engineer(Person, Worker):
    def role(self):
        print("I am an Engineer")

e = Engineer()
e.info()
e.work()
e.role()
