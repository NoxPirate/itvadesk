from app import create_app, db
from app.models import User

app = create_app()

def create_admin(email, name, password):
    with app.app_context():
        if User.query.filter_by(email=email).first():
            print("Admin already exists.")
            return
        u = User(email=email, name=name, role="admin")
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        print("Admin user created.")

if __name__ == "__main__":
    # change these or accept input
    create_admin("arman@admin.com",'Arman','1')
    create_admin("ahmad1@admin.com",'Ahmad1','1')
create_admin("itva4@admin.com",'itva4','1')
create_admin("ankush2@admin.com",'Anksuh','1')