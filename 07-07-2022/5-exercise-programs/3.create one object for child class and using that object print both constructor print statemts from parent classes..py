##3.create one object for child class and using that object print both constructor print statemts from parent classes.
class Father:
    def __init__(self):
        print("Father Class Instance Method")
class Son(Father):

    def __init__(self):
        super().__init__()
        print("Son class Instance Method")
        
s=Son()

