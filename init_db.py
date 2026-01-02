from app import create_app, db
from app.models import User

app = create_app()

def init_db():
    with app.app_context():
        # Create Tables
        db.create_all()
        print("Database tables created.")

        # Create Admin
        if not User.query.filter_by(email="arman@admin.com").first():
            u = User(email="arman@admin.com", name="Arman", role="admin")
            u.set_password("1")
            db.session.add(u)
            print("Admin 'arman@admin.com' created.")

        # Create Regular User
        if not User.query.filter_by(email="ritiks.987654321@gmail.com").first():
            u = User(email="ritiks.987654321@gmail.com", name="Ritik", role="user")
            u.set_password("1")
            db.session.add(u)
            print("User 'ritiks.987654321@gmail.com' created.")

        db.session.commit()
        print("Database initialization complete.")

if __name__ == "__main__":
    init_db()
