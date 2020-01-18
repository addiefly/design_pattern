class Person:
    name = None
    gender = None

    def __init__(self):
        pass

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender


class Male(Person):
    def __init__(self, name):
        super(Male).__init__()
        self.gender = "Male"
        self.name = name
        print("Hello Mr.{}".format(name))


class Female(Person):
    def __init__(self, name):
        super(Female).__init__()
        self.gender = "Female"
        self.name = name
        print("Hello Miss.{}".format(name))


class Factory:
    def get_person(self, name, gender):
        if gender == "M":
            return Male(name)
        elif gender == "F":
            return Female(name)
        else:
            raise Exception("please input 'M' or 'F'")


GENDER = "A"


class PersonMetaClass(type):
    def __new__(cls, clsname, bases, dct):
        print(GENDER)
        if GENDER == "F":
            bases = (Female,)
        elif GENDER == "M":
            bases = (Male,)
        else:
            raise Exception("GENDER should br 'M' or 'F'")
        return type.__new__(cls, clsname, bases, dct)


class PersonFactory(Female):
    __metaclass__ = PersonMetaClass

    def __init__(self, name):
        super(PersonFactory, self).__init__(name)
        print(PersonFactory.__bases__)


if __name__ == '__main__':
    # factory = Factory()
    # person = factory.get_person("Lee", "HH")
    person = PersonFactory("Lee")
    print(person.get_name())
    print(person.get_gender())


