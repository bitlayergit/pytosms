#pytxtmsg, txtmsg.py
#(c) Brunston Poon 2016
#maintained by github/brupoon

import smtplib
from email.mime.text import MIMEText

class txtmsg(object):
    """
    txtmsg object with the following properties:
    
    Attributes:
        p_to: a string with the recipient's phone number
        p_from: a string with the sender's phone number
        msg: a string containing the message (not to be longer than 120 chars)
    """
    
    def __init__(self, p_to, p_from, msg):
        """Return a txtmsg object"""
        self.p_to = p_to
        self.p_from = p_from
        self.msg = msg
    
    def send(self):
        text_to_send = MIMEText(self.msg)
        to_number = self.p_to
        to_number += "@txt.att.net"
        text_to_send['From'] = self.p_from
        text_to_send['To'] = to_number
        
        s = smtplib.SMTP('localhost')
        s.send_message(text_to_send)
        s.quit()

            
if __name__=='__main__':
    testmsg = txtmsg("5555555555","foo","testmsg")
    testmsg.send()