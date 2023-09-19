class maktabkhooneh:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def get_name(self):

        print ("my name is %s and my age is %i" % (self.name,self.age))

 

Maktabkhooneh = maktabkhooneh('maktabkhooneh',7)

Maktabkhooneh.get_name()