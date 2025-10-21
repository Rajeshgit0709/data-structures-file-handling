from session import get_session
from models import User

def update_user(username, **kwargs):
    session = get_session()
    try:
        session.query(User).where(User.username == username).update(kwargs)
        session.commit()
        session.close()
        return True
    except Exception as e:
        session.rollback()
        session.close()
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = update_user("alice", full_name="Alice Johnson", age=30)
    if success:
        print("User updated successfully")
    else:
        print("Failed to update user")
