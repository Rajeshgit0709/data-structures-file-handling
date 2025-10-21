from session import get_session
from models import User

def find_user_by_username(username):
    session = get_session()
    user = session.query(User).where(User.username == username).first()
    session.close()
    return user

if __name__ == "__main__":
    user = find_user_by_username("alice")
    if user:
        print(f"Found: {user.username}, Email: {user.email}")
    else:
        print("User not found")
