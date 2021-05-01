# Import required libraries
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Import python-dotenv to read environment variables
from dotenv import load_dotenv

# Take environment variables from .env
load_dotenv()

# Email address of sender
emailSender = ""

# Password of sender's email address
emailPassword = ""

# Subject of the email that will be sent
emailSubject = ""

# Open and read a CSV file
with open('email.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for line in reader:
    message = "Hello " + line[1] + ". Your " + line[2] + " plan has been activated."
    
    # print(message) # <- Just for debugging

    # Determine receiver of the email from a CSV file which is the first column (index starts from 0).
    emailReceiver = line[0]
    
    # Core code to send email
    msg = MIMEMultipart() # <- Create a class instance of Multipurpose Internet Mail Extensions (MIME) which is an Internet standard that is used to support the transfer of single or multiple text and non-text attachments
    msg['From'] = emailSender
    msg['To'] = emailReceiver
    msg['Subject'] = emailSubject
    msg.attach(MIMEText(message, "plain"))
    text = msg.as_string()

    # Establish the server (using Gmail)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    
    # Authentication process
    server.login(emailSender, emailPassword)
    
    # Send Email
    server.sendmail(emailSender, emailReceiver, text)

    # Exit the server    
    server.quit()
