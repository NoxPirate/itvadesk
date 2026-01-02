from flask_mail import Mail
import app


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'itvadesk@gmail.com'
app.config['MAIL_PASSWORD'] = 'jdffvrnipwmwtoeb'
app.config['MAIL_DEFAULT_SENDER'] = 'itvadesk@gmail.com'

mail = Mail(app)
