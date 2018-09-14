#Reads text from CSV file, formats it & sends via Gmail

#import modules
import csv
import os
import smtplib

#define sender's Google authentication info
gmail_user = "user@example.com"
gmail_password = "password"

#Name & path of CSV file. File must be in the same directory as the script, and must be named list.txt. Janky, I know. I'm going to fix that.
file_dir = os.path.dirname(os.path.realpath('__file__'))
file_name = "list.txt"

#opens file in read-mode, assigns opened file to variable 'csvfile'
csv_file = open(file_name, "r")

#initializes variable that calls reader function from csv module
entry_reader = csv.reader(csv_file, delimiter="," )

#prints every element in line (which is a list) on a new line
row_to_read = next(entry_reader)

#Extracts info form row_to_read list object, inserts it into body, and sends the info to the specified ("to") address, then closes the server.
def send_email(x):
    recipient = "recipient@example.com"
    #body = "\nTITLE: " + x[1] + "\n\nURL: https://www.ebay.com/itm/" + x[0] + "\n\nPRICE: $" + str(x[3]) + "\n\nVENDOR: " + x[4] + "\n\nENDING DATE: " + str(x[6])
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
    #.format(gmail_user, recipient, body)

    server.sendmail(gmail_user, recipient, email_text)
    print(email_text)

    #This iterates to the next row in the CSV file
    row_to_read = next(entry_reader)
    try:
        #Recursive method call using above 'row_to_read' variable as argument
        send_email(row_to_read)
    except:
        #Might want to change this to an error statement, as it could mislead you into thinking that the emails have been sent when in actuality a connection issue stopped the process.
        print("All emails sent.")
    

#If connection to server is made, send_email() method is run. Otherwise, an error is thrown.
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    send_email(row_to_read) #Initial send_email() function call

except:
   print("ERROR: Could not send email. Check formatting of input file and/or network connection.")