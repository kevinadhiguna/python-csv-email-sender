# Import required libraries
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

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
