class Restaurants:
    
    def __init__(self,name="Epashikino Resort & Spa"):
        self.__Restaurant_Name=name
        self._reviews=[]

    def name(self):
        return self.__Restaurant_Name
    
    def reviews(self):
        return self._reviews
    

    