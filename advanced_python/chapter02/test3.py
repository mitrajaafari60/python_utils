class Vehicle:
    color = input()
    def __init__(model, name, color):
        model.name = name
        model.color = color

    def get_name(model):
        print("Vehicle name is %s" % model.name)
 
    def get_color(model):
        print("Vehicle color is %s" % model.color) 

Information = Vehicle("Hossein",color)
Information.get_name()
Information.get_color()