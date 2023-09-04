from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Replace 'sqlite:///your_database.db' with your actual database URL
DATABASE_URL = 'sqlite:///database.db'
engine = create_engine(DATABASE_URL)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    
    # Define the one-to-many relationship between Restaurant and Review
    reviews = relationship('Review', back_populates='restaurant')

    def __repr__(self):
        return f"<Restaurant(name='{self.name}', price={self.price})>"

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    
    # Define the one-to-many relationship between Customer and Review
    reviews = relationship('Review', back_populates='customer')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<Customer(full_name='{self.full_name()}')>"

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True)
    star_rating = Column(Integer, nullable=False)

    # Define foreign key relationships
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    # Define the many-to-one relationship with Restaurant and Customer
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars"

    def __repr__(self):
        return f"<Review(star_rating={self.star_rating})>"

if __name__ == '__main__':
    # Create the database tables
    Base.metadata.create_all(engine)
