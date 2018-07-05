#Reads text from CSV file, formats it & sends via Gmail

#import modules
import csv
import os
import smtplib

#define sender's Google authentication info
gmail_user = "sender@example.com"
gmail_password = "password123"


fileDir = os.path.dirname(os.path.realpath('__file__'))

#name of CSV file. Due to above line, no filepath needs defined
filename = "7.5.2k18.txt"

#opens file in read-mode, assigns opened file to variabel 'csvfile'
csvfile = open(filename, "r")

#initializes variable that calls reader function from csv module
entryReader = csv.reader(csvfile, delimiter="," )

#prints every element in line (which is a list) on a new line
row_to_read = next(entryReader)


#Extracts info form row_to_read list object, inserts it into body, and sends the info to the specified ("to") address, then closes the server.
def send_email(x):
    sent_from = "sender@example.com"
    to = "recipient@example.com"
    subject = str(x[1])
    body = "\nTITLE: " + x[1] + "\n\nURL: " + x[2] + "\n\nPRICE: $" + str(x[3]) + "\n\nVENDOR: " + x[4] + "\n\nENDING DATE: " + str(x[6])
    email_text = """
    From: {}
    To: {}
    Subject: --Watched Item--

    {}

    \nThis is an automated message.
    """.format(sent_from, to, body)
    server.sendmail(sent_from, to, email_text)
    print(body)
    #This iterates to the next row in the CSV file
    row_to_read = next(entryReader)
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
    #Initial send_email() function call
    send_email(row_to_read)

except:
    print("ERROR: Connection could not be established.")

    #def collect_listing_start_date(x):
    #   epoch_date = 

