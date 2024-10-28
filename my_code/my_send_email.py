import smtplib
from email.message import EmailMessage

def send_email(receiver, subject, message):
  SENDER_EMAIL = "YOUR_EMAIL@EMAIL.COM"  # replace with your email address
  SENDER_PASSWORD = "YOUR_PASSWORD"  # replace with your email password
  
  msg = EmailMessage()
  msg['Subject'] = subject
  msg['From'] = "YOUR_EMAIL@EMAIL.COM"
  msg['To'] = receiver
  msg.set_content(message)

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(SENDER_EMAIL, SENDER_PASSWORD)
  server.sendmail(receiver, subject, msg)
  server.quit()

if __name__ == '__main__':
  send_email("RECEIVER_EMAIL@EMAIL.COM", "Email from python", "Hello, This is an email from python test")