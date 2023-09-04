from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review  # Import your SQLAlchemy models

# Replace 'sqlite:///your_database.db' with your actual database URL
DATABASE_URL = 'sqlite:///database.db'
engine = create_engine(DATABASE_URL)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a new restaurant to the database
def add_new_restaurant(name, price):
    new_restaurant = Restaurant(name=name, price=price)
    session.add(new_restaurant)
    session.commit()

# Function to add a new customer to the database
def add_new_customer(first_name, last_name):
    new_customer = Customer(first_name=first_name, last_name=last_name)
    session.add(new_customer)
    session.commit()

# Function to add a new review to the database
def add_new_review(restaurant_id, customer_id, star_rating):
    new_review = Review(
        restaurant_id=restaurant_id,
        customer_id=customer_id,
        star_rating=star_rating
    )
    session.add(new_review)
    session.commit()

# Function to query all restaurants
def get_all_restaurants():
    return session.query(Restaurant).all()

# Function to query all customers
def get_all_customers():
    return session.query(Customer).all()

# Function to query all reviews
def get_all_reviews():
    return session.query(Review).all()

if __name__ == '__main__':
    # Example usage:
    
    # Add a new restaurant
    add_new_restaurant(name='Restaurant A', price=3)

    # Add a new customer
    add_new_customer(first_name='John', last_name='Doe')

    # Add a new review
    add_new_review(restaurant_id=1, customer_id=1, star_rating=4)

    # Query all restaurants
    restaurants = get_all_restaurants()
    for restaurant in restaurants:
        print(f"Restaurant: {restaurant.name}, Price: {restaurant.price}")

    # Query all customers
    customers = get_all_customers()
    for customer in customers:
        print(f"Customer: {customer.full_name()}")

    # Query all reviews
    reviews = get_all_reviews()
    for review in reviews:
        print(review.full_review())
