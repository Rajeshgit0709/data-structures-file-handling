from session import get_session
from models import User

def get_all_users():
    session = get_session()
    users = session.query(User).all()
    session.close()
    return users

if __name__ == "__main__":
    users = get_all_users()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
