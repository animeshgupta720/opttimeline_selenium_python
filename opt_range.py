#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import re
import smtplib, ssl
import getpass

path = input("Enter the path where chromedriver is installed:")
my_id = input("Enter your OPT application number:")
email = input("Enter your email: ")
email_password = getpass.getpass("Enter email password: ")
count=0
count2=0


def send_simple_message(my_id):


    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = email
    password = email_password
    receiver_email = email
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        message="Congratulations! Your case status" + " " + my_id + " " + "is approved."
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()



for i in range (3200,3215):

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #path = input("Enter the path where chromedrier is installed:")
    driver = webdriver.Chrome(path,options=chrome_options)
    #'/home/animesh/Downloads/chromedriver'
    driver.get("https://egov.uscis.gov/casestatus/landing.do")


    que = driver.find_element_by_xpath('//*[@id="receipt_number"]')
    r_id = "YSC209015"+ str(i)
    que.send_keys(r_id)
    time.sleep(3)

    que=driver.find_element_by_xpath('//*[@id="landingForm"]/div/div[1]/div/div[1]/fieldset/div[2]/div[2]/input')
    value = que.click()
    time.sleep(3)
    content = driver.page_source

    driver.quit()

    with open('webpage.html', 'w') as f:

     f.write(content)

    with open('webpage.html','r') as f:
     mystatus = f.read()



    r = re.compile(r'\bApproved\b | \bDelivered\b | \bMailed\b', flags=re.I | re.X)
    value = r.findall(mystatus)

    if 'Approved' in value  or 'Delivered' in value or 'Mailed' in value:
     if r_id==my_id:
      send_simple_message(my_id)
     #count = count+1
     #print(r_id,"Approved ")
      time.sleep(2)
     count = count+1
     print(r_id,"Approved ")
     time.sleep(2)

    else:
     print(r_id,"Received")
     count2=count2+1

print("Total Approved = ",count)
print("Total Received = ",count2)
time.sleep(3)
