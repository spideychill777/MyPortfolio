#Remember to install the required packages before running the app:
#pip install Flask Flask-Mail python-dotenv

from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', '777')

app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        #create message of email
        msg = Message('New message from contact form',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        #Send email
        mail.send(msg)
        flash('Email sent successfully!', 'success')
    except Exception as e:
        print(f"Error sending email: {e}")
        flash('Failed to send email. Please try again later.', 'danger')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
    