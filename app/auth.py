from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required, current_user

auth_bp = Blueprint("auth", __name__, template_folder="templates")

@auth_bp.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and user.role == "admin" and user.check_password(password):
            login_user(user)
            flash("Logged in successfully as Admin.", "success")
            return redirect(url_for("admin.dashboard"))

        flash("Invalid credentials or not an admin.", "danger")

    return render_template("admin_login.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print(f"DEBUG: Login attempt for {email}")

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            print(f"DEBUG: Login successful for {user.name} ({user.role})")
            flash("Logged in successfully.", "success")
            # Redirect to user dashboard if user, admin dashboard if admin? 
            # Usually separate, but let's stick to user_dashboard for /login
            if user.role == 'admin':
                 print("DEBUG: Redirecting to admin dashboard")
                 return redirect(url_for("admin.dashboard"))
            
            print("DEBUG: Redirecting to user_dashboard")
            return redirect(url_for("main.user_dashboard"))

        print("DEBUG: Login failed - Invalid credentials")
        flash("Invalid credentials.", "danger")

    return render_template("user_login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.", "info")
    return redirect(url_for("auth.login"))

@auth_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        
        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "warning")
            return redirect(url_for("auth.register"))

        user = User(name=name, email=email, role="user")
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. Please login.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


