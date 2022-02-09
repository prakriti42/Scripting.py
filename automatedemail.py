'''
    Wriiten By : Prakriti Regmi 
    On : 8th Feb 2022
    Description : This is a simple python script to send an automated email to the user.    
'''



#Neceessary Libraries 
import smtplib , ssl 
from datetime import datetime



#Function to send the email
def send_email():

    #Fetching the current month
    currentMonth= datetime.now().strftime("%b")

    #Setting Email Subject 
    subject= "Product Update Details."
    #Setting Email Body
    body = f"Greetings, \n \n I hope this email finds you well. \n This is to inform that the product updates for the month of {currentMonth} has been successfully completed in all our media.\n\n\nWith Best Regards,\nPrakriti Regmi."
    
    #Compiling the entire email
    message = f"Subject : {subject}\n\n {body}"

    #Setting the email server 
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    #Setting the personal gmail credentials
    password = "idskaefmzabjqlhk"
    sender_email = "regmi.prakriti24@gmail.com"

    #Setting the receiver emails
    receiver_email = ["tbf110011@gmail.com", "regmi.prakriti24@gmail.com"]

    #Creating the ssl object
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try :
            try:
                #Logging into the email server
                server.login(sender_email, password)
            except smtplib.SMTPAuthenticationError:
                print("Authentication Error")
                return None
            #Sending the email
            server.sendmail(sender_email, receiver_email, str(message))
            print("email sent")
            return None
        except Exception as e:
            print(e)
            print("email not sent")
            return None
        server.quit()

#Calling the function
send_email()



    