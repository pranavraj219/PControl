import getpass, imaplib
import email
import subprocess
import time
import os
def wait_sec(t):
    time.sleep(t)
M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
uemail=input("Your E-mail address(for sending commands):")
cmail = input("Email address for PC: ")
password = getpass.getpass()
M.login(cmail, password)
M.select("inbox")
try:
    fi_obj=open("ID.txt")
    prev_id=fi_obj.read()
except IOError:
    print ("Eroor")
    prev_id=-1
#print (prev_id)
while(1):
    fo_obj=open("ID.txt","w")
    fo_obj.write(prev_id)
    fo_obj.close()
    wait_sec(3)
    print ("google")
    result, data = M.uid('search', None, 'FROM '+uemail) # search and return uids instead
    print (data)
    st=str(data[0],'utf-8')
    #print (len(st))
    if(len(st)<=0):
        print ("poo")
        #wait_sec(10)
        continue
    latest_email_uid = data[0].split()[-1]
    result, data = M.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)#from_bytes since in python3 it is bytes
    def get_first_text_block(email_message_instance):
      #  print ("HELLO")
        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif maintype == 'text':
            return email_message_instance.get_payload()

    #From= email.utils.parseaddr(email_message['From'])[1]
    msg=get_first_text_block(email_message)
    print(prev_id)
    print (latest_email_uid)
    if(prev_id!=str(latest_email_uid,'utf-8')):
     Process=subprocess.Popen([msg],shell=True)
     Process.wait()
     prev_id=str(latest_email_uid,'utf-8')
               #subprocess.Popen(["Taskkill /PID "+ /F
    #get_first_text_block(M,email_message)
     
M.close()
M.logout()
