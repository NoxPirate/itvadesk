from app import create_app, db
from app.models import User

app = create_app()

def create_user(email, name, password):
    with app.app_context():
        if User.query.filter_by(email=email).first():
            print(f"User {email} already exists.")
            return
        u = User(email=email, name=name, role="user")
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        print(f"Regular user {email} created.")

if __name__ == "__main__":
    create_user("user@example.com", "Test User", "1")
