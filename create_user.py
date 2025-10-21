from session import get_session
from models import User

def create_new_user(username, email, full_name, age=None):
    session = get_session()
    try:
        new_user = User(
            username=username,
            email=email,
            full_name=full_name,
            age=age
        )
        session.add(new_user)
        session.commit()
        user_id = new_user.id
        session.close()
        return user_id
    except Exception as e:
        session.rollback()
        session.close()
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    user_id = create_new_user("david", "david@example.com", "David Lee", 28)
    if user_id:
        print(f"User created with ID: {user_id}")
    else:
        print("Failed to create user")
