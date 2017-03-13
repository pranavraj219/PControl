# PControl  
Python script to control one's PC using Gmail.   
Note:- Read completely before starting.  
Requirements -    
2 Gmail ids, python 3.5 or 3.5+ .  
Step 1 - Create two accounts in GMail. One for the computer(In this, the computer will be receiving commands and sending output to the user, Let's call this mail as cmail) and the other for yourself(This, you will be using to send commands to the computer and for receiving output,Let's call this mail as uemail,you can skip uemail creation, if you already have a gmail account.)   
Step 2 - After successfully creating the above two accounts, Sign in with your cmail account and then go to Top Right corner and Click on the button(Where you see your profile picture)->My Account->"Connected apps and sites".Then scroll down and Enable "Allow Less Secure Apps".  
Step 3 - To start using, first of all send a random command to the computer mail,this is to avoid any connection issues.For Example - Sign in through uemail in your browser and then compose an email,write the cmail address in "TO" field and then write
"echo hello" without the quotes in the body section.You can leave the "SUBJECT" blank.Now click on send.  
Step 4 - Start the script.When it asks "Your E-mail address(for sending commands):-",type your uemail address.(Example - pranavraj@gmail.com)  
Step 5 - "Email address for PC:-",Enter the cmail address which you created(example - jarvis@gmail.com).And then it's password.  
If logged in Successfully,  
If running the script for the first time after e-mail registration,it will execute the command which we gave "echo hello" and send you the output in your mail.  
Now you are all set.  
Open your uemail and start giving commands.Now you can execute any shell commands that are single step.  
For example:-  
shutdown, mkdir, ping, tracert, and so on.  
The command will be executed and the execution report and output will be sent to the uemail.  
Note that, it may take a bit time to get the output, because it depends upon the time the command takes to execute and the internet speed.   
Also, the script may not work in case of network in which some restrictions are their, like in some colleges. So,it would be better if the script is used with a mobile hotspot or dongle.
The command sent can take about 20-40 seconds to be read from the mail.
