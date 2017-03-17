import getpass, imaplib
import email
import subprocess
import time
import os
import smtplib
from win10toast import ToastNotifier
def wait_sec(t):
    time.sleep(t)
def runScript(script):
    f_batch=open("Bscript.bat","w")
    for pt in script:
        f_batch.write(str(pt))
        f_batch.write("\n")
    f_batch.close()
    #p=subprocess.Popen("Bscript.bat",shell=True,stdout=subprocess.PIPE)
def showToast(frm,msg):
    toast=ToastNotifier()
    toast.show_toast(frm,msg)
    
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
    result, data = M.uid('search', None, 'FROM '+uemail) #search and return uids
    st=str(data[0],'utf-8')
    if(len(st)<=0):
        continue
    latest_email_uid = data[0].split()[-1]
    result, data = M.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    email_subject=email_message['subject']
    email_from=email_message['from']
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
     msg2=msg
     msg=msg.split("\r\n")
     if(email_subject=="show_notification"):
         showToast(email_from,msg2)
         prev_id=str(latest_email_uid,'utf-8')
         continue
     if(email_subject=="run_script"):
         runScript(msg)
         msg2="Bscript.bat"
         
     print("Command -\n"+msg2)
     p = subprocess.Popen(msg2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
     OUT="Output for "+"\""+msg2+"\" :-\n"
     stats="\nExecution incomplete"
     for line in p.stdout.readlines():
       OUT=OUT+line.decode('utf-8')
     if(p.poll()==None):
         stats="\nExecution complete"
#Sending Output to the user
     smtpObj.sendmail(cmail,uemail,'Subject: '+msg2+'\n'+OUT+stats)
     prev_id=str(latest_email_uid,'utf-8')
smtpObj.quit()
M.close()
M.logout()
