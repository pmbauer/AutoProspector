#Reads text from CSV file, formats it & sends via Gmail


import csv
import os
import smtplib

#define sender's Google authentication info
gmail_user = "holden@newlifescientific.com"
gmail_password = "33walrusesandrats1999"

#Name & path of CSV file. File must be in the same directory as the script, and must be named list.txt. Janky, I know. I'm going to fix that.
file_dir = os.path.dirname(os.path.realpath('__file__'))
file_name = "list.txt"

#opens file in read-mode, assigns opened file to variable 'csvfile'
csv_file = open(file_name, "r")

#initializes variable that calls reader function from csv module
entry_reader = csv.reader(csv_file, delimiter="," )

#prints every element in line (which is a list) on a new line
row_to_read = next(entry_reader)

#Extracts info from row_to_read list object, inserts it into body, and sends the info to the specified ("to") address, then closes the server.
def send_email(x):
    recipient = "holden@newlifescientific.com"
    email_text = (f"""
    From: {gmail_user}
    To: {recipient}
    Subject: --Watched Item--
    
    TITLE: {x[1]}
    
    URL: https://www.ebay.com/itm/{x[0]}
    
    PRICE: ${x[2]}
    
    VENDOR: {x[3]}
    
    ENDING DATE: {x[5]}

    \nThis is an automated message.
    """)

    server.sendmail(gmail_user, recipient, email_text)
    print(email_text)

    #This iterates to the next row in the CSV file
    row_to_read = next(entry_reader)

    while row_to_read != False:
        send_email(row_to_read)
    else:
        print("All emails sent.")
        exit()

#If connection to server is made, send_email() method is run. Otherwise, an authentication exception is raised.
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    send_email(row_to_read) #Initial send_email() function call

except smtplib.SMTPAuthenticationError:
    print("ERROR: Could not send email(s). Verify authentication information and/or network connection.")

#After script has run (successfully or unsuccessfully), prompt user to exit
finally:
    print("Exiting...")
    exit()

