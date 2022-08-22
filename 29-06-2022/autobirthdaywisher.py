##Auto Birthday Wisher: 
##
## 
##
### Auto Birthday Wisher 
##
## 
##
##- **Pandas** is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, 
##
##built on top of the Python programming language. 
##
##```bash 
##
##pip inst One forgets to send birthday wishes to friends many times. At such times an automatic birthday wisher comes handy. An automatic birthday wisher via email makes one's life easy. It will send the birthday wishes to friends via email automatically via a server and using an excel sheet to store the data of friends and their birthdays along with email id. It'll send the wishes to friends for all the upcoming years until we stop the server. 
##
## 
##
#### Setup instructions 
##
## 
##
##In order to run this script, You just need the following modules: 
##
## 
##
##all pandas 
##
##``` 
##
## 
##
##- **Datetime** is a module used for Encapsulation of date/time values. 
##
##```bash 
##
##pip install DateTime 
##
##``` 
##
## 
##
##- **smtplib** module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon. 
##
## 
##
#### Configuration 
##
##1. Assign the Gmail Id of sender to the GMAIL_ID variable in *line 10* of **"Auto B'Day Wisher.py"** file. (e.g. 'xyz@gmail.com') 
##
##2. Similar to first step assign the Gmail password of sender to the GMAIL_PSWD variable in *line 11* of **"Auto B'Day Wisher.py"** file. (e.g. '1234') 
##
##3. In **"data.xlsx"** file insert the name of the receiver in second column under *Name*. Similarly update the **Birthday** field with the birth date of receiver in the given format*("%dd-%mm-%YYYY")*. Update the **Dailogue** field with a short message you want to send and the **Email** field with the email of the receiver. 
##
##4. Make sure to give permission to your google account from which you're sending email to **Allow less secure apps**. Just turn this *"ON"* from [here](https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-off-for-your-account). 
##
##5. Run the command 
##
##```bash 
##
##python "Auto B'Day Wisher.py
import pandas as pd
import datetime
import smtplib
import os

current_path=os.getcwd()
print(current_path)


gmail_id=input("Enter your email: ")
gmail_pwd=input("Enter password for your email id mentioned above: ")

def sendEmail(to,sub,msg):
    print(f"Email to {to} sent: \nSubject: {sub},  \nMessage: {msg}")
    s=smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(gmail_id,gmail_pwd)
    s.sendmail(gmail_id, to, f"Subject: {sub} \n\n{msg}")
    s.quit()
if __name__=="__main__":
    df=pd.read_excel(r"C:\Users\my22114\Documents\python programs\29-06-2022\autobirthday.xlsx")
    print(df)  
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    writeindex=[]
    for i in writeindex:
        for index,item in df.iterrows():
            bday=item["Birthday"]
            bdy=datetime.datetime.strptime(bday,"%d-%m-%y")
            bday=bday.strftime("%d-%m")
            if (today==bday) and year not in str(item["Lastwishedyear"]):
                sendEmail(item["Email"],"Hppy Birthday",item["Dialogue"])
                writeindex.append(index)
                print(writeindex)
##                
##    if writeindex != None:
##        for i in writeindex:
##            oldYear = df.loc[i, 'LastWishedYear']
##            df.loc[i, 'LastWishedYear'] = str(oldYear) + ", " + str(yearNow)
##
##    df.to_excel("autobirthday.xlsx", index=False)
##                      
                                             
