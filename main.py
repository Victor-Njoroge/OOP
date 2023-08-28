from customer import Customers
from restaurant import Restaurants
from review import Review

if __name__ == "__main__":
    cusFirstName = input("Enter First Name: ")
    cusFamilyName = input("Enter Family Name: ")
    person = Customers(cusFirstName, cusFamilyName)

    restaurant_name = input("Enter Restaurant Name: ")
    rating = int(input("Enter Rating (1 to 5): "))
    person.add_review(restaurant_name, rating)

    print("Customer Reviews:")
    for review in person.get_reviews():
        print(f"Restaurant: {review.restaurant_name()}, Rating: {review.rating()}")

    restaurant_instance = Restaurants.get_or_create(restaurant_name)
    print("Restaurant Reviews:")
    for review in restaurant_instance.reviews():
        print(f"Customer: {review.customer_name()}, Rating: {review.rating()}")
