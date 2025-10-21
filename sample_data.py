from database_config import get_db_session
from database_tables import User, Category, Product, create_all_tables

def insert_sample_data():
    with get_db_session() as session:
        users = [
            User(username="john", email="john@example.com", password_hash="hash123", first_name="John", last_name="Doe"),
            User(username="jane", email="jane@example.com", password_hash="hash456", first_name="Jane", last_name="Smith")
        ]
        session.add_all(users)
        
        categories = [
            Category(name="Electronics", slug="electronics"),
            Category(name="Books", slug="books")
        ]
        session.add_all(categories)
        
        products = [
            Product(name="Laptop", slug="laptop", price=999.99, stock_quantity=10, category_id=1),
            Product(name="Phone", slug="phone", price=599.99, stock_quantity=20, category_id=1)
        ]
        session.add_all(products)
        
        session.commit()
        print("Sample data inserted")

if __name__ == "__main__":
    create_all_tables()
    insert_sample_data()
