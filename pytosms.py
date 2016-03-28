# pytosms
# (c) Brunston Poon 2016
# MIT License

import smtplib
from email.mime.text import MIMEText

class SMS(object):
    """
    SMS object with the following properties:
    
    Attributes:
        p_to: a string with the recipient's phone number
        p_from: a string with the sender's phone number
        msg: a string containing the message (not to be longer than 120 chars)
    """
    
    def __init__(self, to, fr, msg, sendhost):
        """Return an SMS object"""
        self.to = to
        self.fr = fr
        self.msg = msg
        #generic domain if no sending domain specified (via "")
        if sendhost == "":
            self.sendhost = "@example.org"
        #this gets appended to our "from" phone number
        else:
            self.sendhost = "@"
            self.sendhost += sendhost


    def send(self):
        """
        Sends message. Returns True if successfully used SMTP server to send message,
        returns False if there is no server running.
        """
        text_to_send = MIMEText(self.msg)

        carriers = ["@txt.att.net", "@txt.windmobile.ca", "@vxtext.com",\
                    "@text.republicwireless.com", "@msg.fi.google.com",\
                    "@email.uscc.net", "@message.alltel.com", "@messaging.sprintpc.com",\
                    "@mobile.celloneusa.com", "@msg.telus.com", "paging.acswireless.com",\
                    "@pcs.rogers.com", "@questmp.com", "@sms.mycricket.com",\
                    "@sms.ntwls.net","@tmomail.net"]
        
        #append the sending host to our from address
        fr_address = self.fr
        fr_address += self.sendhost

        for carrier in carriers:
            to_address = self.to
            to_address += carrier
            
            try:        
                s = smtplib.SMTP('localhost')
                #s.send_message(text_to_send)
                s.sendmail(fr_addess, to_address, self.msg)
                s.quit()
            except ConnectionRefusedError:
                print("You are not running an SMTP server, i.e. sendmail, on your local machine. Exiting.")
                return False

        return True
