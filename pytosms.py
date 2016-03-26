#pytosms.py#
#(c) Brunston Poon 2016
#maintained by github/brupoon

import smtplib
from email.mime.text import MIMEText
import random
import string

class SMS(object):
    """
    SMS object with the following properties:
    
    Attributes:
        p_to: a string with the recipient's phone number
        p_from: a string with the sender's phone number
        msg: a string containing the message (not to be longer than 120 chars)
    """
    
    def __init__(self, p_to, p_from, msg):
        """Return an SMS object"""
        self.p_to = p_to
        self.p_from = p_from
        self.msg = msg
    
    def send(self):
        text_to_send = MIMEText(self.msg)

        carriers = ["@txt.att.net", "@txt.windmobile.ca", "@vxtext.com",\
                    "@text.republicwireless.com", "@msg.fi.google.com",\
                    "@email.uscc.net", "@message.alltel.com", "@messaging.sprintpc.com",\
                    "@mobile.celloneusa.com", "@msg.telus.com", "paging.acswireless.com",\
                    "@pcs.rogers.com", "@questmp.com", "@sms.mycricket.com",\
                    "@sms.ntwls.net","@tmomail.net"]

        self.p_to += "@txt.att.net"

        
        self.p_from += "@example.com"
        
        s = smtplib.SMTP('localhost')
        #s.send_message(text_to_send)
        s.sendmail(self.p_from, self.p_to, self.msg)
        s.quit()

