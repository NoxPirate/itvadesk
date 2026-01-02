
import sys
import os

# Add the application directory to the python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import create_app, db
from app.models import Ticket

def test_email_submission():
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    
    # Use an in-memory db or just use the existing one? 
    # Using existing one might pollute it, but it's fine for a test record we can delete.
    # Actually, let's just inspect the logic without full creating app if possible, 
    # but we need app context for DB.
    
    with app.app_context():
        client = app.test_client()
        
        # Data for submission
        test_email = "verification@example.com"
        test_issue = "Verification Issue Content"
        test_name = "Verification User"
        
        print(f"Submitting ticket with email: {test_email}")
        
        response = client.post('/submit_ticket', data={
            'name': test_name,
            'department': 'Testing',
            'email': test_email,
            'issue': test_issue
        }, follow_redirects=True)
        
        # Check if submission was successful (redirects to user_dashboard usually)
        if response.status_code != 200:
            print(f"Failed to submit ticket. Status code: {response.status_code}")
            return

        # Query the DB for this ticket
        ticket = Ticket.query.filter_by(user_name=test_name, department='Testing').order_by(Ticket.id.desc()).first()
        
        if ticket:
            print("Ticket found in DB.")
            print(f"Stored Issue Content:\n---\n{ticket.issue}\n---")
            
            if f"__Contact Email: {test_email}__" in ticket.issue:
                print("SUCCESS: Email is correctly appended to the issue.")
            else:
                print("FAILURE: Email NOT found in issue.")
                
            # Cleanup
            db.session.delete(ticket)
            db.session.commit()
            print("Test ticket deleted.")
        else:
            print("FAILURE: Ticket not found in DB.")

if __name__ == "__main__":
    test_email_submission()
