# pytosms
# (c) Brunston Poon 2016
# MIT License

import smtplib
from email.mime.text import MIMEText

class SMS(object):
    """
    SMS object with the following properties:
    
    Attributes:
        to: a string with the recipient's phone number
        fr: a string with the sender's phone number
        sendhost: a string with a domain the sender controls (alternately, "" for example.org)
        msg: a string containing the message (not to be longer than 120 chars)
    """
    
    def __init__(self, fr, to, sendhost, msg):
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

        carriers = ["@txt.att.net", "@txt.windmobile.ca", "@vtext.com",\
                    "@text.republicwireless.com", "@msg.fi.google.com",\
                    "@email.uscc.net", "@messaging.sprintpc.com",\
                    "@msg.telus.com", "@paging.acswireless.com",\
                    "@pcs.rogers.com", "@sms.mycricket.com",\
                    "@sms.ntwls.net","@tmomail.net"]
        
        #append the sending host to our from address
        fr_address = self.fr
        fr_address += self.sendhost

        for carrier in carriers:
            #trying each supported carrier in sequence
            to_address = self.to
            to_address += carrier
            print("trying carrier,",to_address)
            try:        
                s = smtplib.SMTP('localhost')
                s.sendmail(fr_address, to_address, self.msg)
                s.quit()
            except ConnectionRefusedError:
                print("You are not running an SMTP server, i.e. sendmail, on your local machine. Exiting.")
                return False

        return True
