import getpass, imaplib
import email
import subprocess
import time
import os
import smtplib
def wait_sec(t):
    time.sleep(t)
M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
uemail=input("Your E-mail address(for sending commands):- ")
while(1):
    try:
        cmail = input("Email address for PC:- ")
        password = getpass.getpass()
        M.login(cmail, password)            #Establishing IMAP connection with the server
        smtpObj.ehlo()                      #Establishing SMTP connection with the server
        smtpObj.login(cmail,password)
        print("Logged in Successfully as "+cmail)
        break
    except imaplib.IMAP4.error:
        print ("Login failed")
M.select("inbox")
try:
    fi_obj=open("ID.txt")
    prev_id=fi_obj.read()
except IOError:
    prev_id=-1
while(1):
    fo_obj=open("ID.txt","w")
    #Using previous ID to check the repetition of a single mail executing more than once
    fo_obj.write(str(prev_id))
    fo_obj.close()
    wait_sec(5)
    data = M.uid('search', None, 'FROM '+uemail) #search and return uids
    st=str(data[0],'utf-8')
    if(len(st)<=0):
        continue
    latest_email_uid = data[0].split()[-1]
    data = M.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    def get_text_block(email_message_instance):
        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif maintype == 'text':
            return email_message_instance.get_payload()
    
    if(prev_id!=str(latest_email_uid,'utf-8')):
#Parsing E-mail and executing command
     msg=get_text_block(email_message)
     print("Command -\n"+msg)
     p = subprocess.Popen(msg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
     OUT="Output for "+"\""+msg+"\" :-\n"
     stats="\nExecution incomplete"
     for line in p.stdout.readlines():
       OUT=OUT+line.decode('utf-8')
     if(p.poll()==None):
         stats="\nExecution complete"
#Sending Output to the user
     smtpObj.sendmail(cmail,uemail,'Subject: '+msg+'\n'+OUT+stats)
     prev_id=str(latest_email_uid,'utf-8')
smtpObj.quit()
M.close()
M.logout()
