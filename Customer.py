class Customers:
    _Array = []

    def __init__(self, cusName="Victor", famName="Njoroge"):
        self._customer_given_name = cusName
        self._family_given_name = famName
        self._reviews = []

    def get_cusName(self):
        return self._customer_given_name
    
    def get_famName(self):
        return self._family_given_name
    
    def fullName(self):
        return f"{self._customer_given_name} {self._family_given_name}"
    
    newName = property(get_cusName, get_famName)

cusFirstName = input("Enter First Name: ")
cusFamilyName = input("Enter Family Name: ")
person = Customers(cusFirstName, cusFamilyName)
print(person.fullName())  
