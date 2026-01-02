# from flask_mail import Mail, Message
# from . import mail
# from flask import current_app
# from ast import main
# from flask import Blueprint, render_template, request, redirect, url_for, flash
# from flask_mail import Message
# from .models import Ticket
# from . import db

# main_bp = Blueprint("main", __name__)

# @main_bp.route("/")
# def index():
#     return render_template("index.html")

# @main_bp.route("/submit_ticket", methods=["POST"])
# def submit_ticket():
#     name = request.form.get("name").strip()
#     department = request.form.get("department")
#     issue = request.form.get("issue").strip()

#     if not name or not issue:
#         flash("Name and issue are required.", "warning")
#         return redirect(url_for("main.user_dashboard"))

#     t = Ticket(user_name=name, department=department, issue=issue)
#     db.session.add(t)
#     db.session.commit(send_email(
#     "New Ticket Received",
#     "thearman796@gmail.com",
#     f"""
# New Ticket Created

# User Name: {name}
# Department: {department}
# Issue: {issue}
# """
# )
# )

#     flash("Ticket submitted successfully.", "success")
#     return redirect(url_for("main.user_dashboard"))

# @main_bp.route("/user_dashboard")
# def user_dashboard():
#     return render_template("user_dashboard.html")


# def send_email(subject, to_email, body):
#     msg = Message(subject, recipients=[to_email])
#     msg.body = body
#     main.send(msg)


# @main_bp.route("/close-ticket/<int:id>")
# def close_ticket(id):

#     ticket = Ticket.query.get_or_404(id)
#     ticket.status = "Closed"
#     db.session.commit()

#     send_email(
#         "Your Ticket is Closed",
#         "armanshaikh191128@gmail.com",
#         f"""
# Hello,

# Your ticket has been closed successfully.

# Issue:
# {ticket.issue}

# Thanks,
# IT Support Team
# """
#     )

#     flash("Ticket closed successfully", "success")
#     return redirect(url_for("main.user_dashboard"))

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_mail import Message
from .models import Ticket, User
from . import db, mail

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/submit_ticket", methods=["POST"])
def submit_ticket():
    name = request.form.get("name", "").strip()
    department = request.form.get("department")
    email = request.form.get("email", "").strip()
    issue = request.form.get("issue", "").strip()

    if not name or not issue or not email:
        flash("Name, email, and issue are required.", "warning")
        return redirect(url_for("main.user_dashboard"))

    # Save to DB natively
    ticket = Ticket(user_name=name, email=email, department=department, issue=issue)
    db.session.add(ticket)
    db.session.commit()

    # Send Notification to Admin (using the requested test email for now or kept as is)
    # The user asked to use ritiks.987654321@gmail.com when user submit ticket.
    # Assuming this means the notification goes TO this email or FROM?
    # Context implies this is the USER's email.
    # We will send the admin notification as usual.

    send_email(
        "New Ticket Received",
        "ritiks.987654321@gmail.com", 
        f"""
New Ticket Created

User Name: {name}
Email: {email}
Department: {department}
Issue: {issue}
"""
    )

    flash("Ticket submitted successfully.", "success")
    return redirect(url_for("main.user_dashboard"))


@main_bp.route("/user_dashboard")
def user_dashboard():
    return render_template("user_dashboard.html")


def send_email(subject, to_email, body):
    print(f"DEBUG: Attempting to send email to {to_email}...")
    try:
        msg = Message(subject=subject, recipients=[to_email], body=body)
        mail.send(msg)
        print("DEBUG: Email sent successfully!")
    except Exception as e:
        print(f"DEBUG: Failed to send email: {e}")  


@main_bp.route("/close-ticket/<int:id>", methods=["POST"])
def close_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    ticket.status = "Closed"
    db.session.commit()

    try:
        user = User.query.filter_by(name=ticket.user_name).first()
        if user and user.email:
            send_email(
                "Your Ticket is Closed",
                "thearman769@gmail.com",
                f"""
Hello,

Your ticket has been closed successfully.

Issue:
{ticket.issue}

Thanks,
IT Support Team
"""
            )
    except Exception:
        pass

    flash("Ticket closed successfully", "success")
    return redirect(url_for("main.user_dashboard"))
