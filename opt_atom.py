#!/usr/bin/env python3
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options

#driver = webdriver.Chrome('/home/animesh/Downloads/chromedriver')


#driver.get('https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p702')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import re
import smtplib, ssl

count=0
count2=0
for i in range (3200,3215):

#driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
#driver.get("http://www.google.com")
#driver.get("//*[@id="receipt_number"]")
 chrome_options = Options()
 chrome_options.add_argument('--headless')
 chrome_options.add_argument('--no-sandbox')
 chrome_options.add_argument('--disable-dev-shm-usage')
 driver = webdriver.Chrome('/home/animesh/Downloads/chromedriver',chrome_options=chrome_options)

#driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
 driver.get("https://egov.uscis.gov/casestatus/landing.do")
#count=0
 #'//*[@id="landingForm"]/div/div[1]/div/div[1]/fieldset/div[2]/div[2]/input'
#for i in range (3000,3005):

 que = driver.find_element_by_xpath('//*[@id="receipt_number"]')
 que.send_keys("YSC209015"+ str(i))
 r_id = "YSC209015"+ str(i)
 time.sleep(3)
#que.send_keys(Keys.ARROW_DOWN)

 que=driver.find_element_by_xpath('//*[@id="landingForm"]/div/div[1]/div/div[1]/fieldset/div[2]/div[2]/input')
 value = que.click()
 time.sleep(3)
 content = driver.page_source

 driver.quit()

 with open('webpage.html', 'w') as f:

    f.write(content)

 with open('webpage.html','r') as f:
    mystatus = f.read()



 ''' x = re.search("Approved | Delivered | Mailed", mystatus)
 if x=='Approved' or 'Delivered' or 'Mailed':
    #send_simple_message()
    count = count+1
    #print(x)
    print("Approved")
 else:
    print("Received")
    count2=count2+1'''
#mystatus = "These are oranges and Aproved Deivered apples Mailed and pears, but not pinapples or .."
#count = 0
#x = re.search("Approved | Delivered | Mailed", mystatus)
#s = "These are oranges and Aproved Deivered apples Mailed and pears, but not pinapples or .."
 r = re.compile(r'\bApproved\b | \bDelivered\b | \bMailed\b', flags=re.I | re.X)
 value = r.findall(mystatus)
 #print(value)
#print(x)
 if 'Approved' in value  or 'Delivered' in value or 'Mailed' in value:
    #send_simple_message()
    count = count+1
    #print(x)
    print(r_id,"Approved ")
    #print(count)
    time.sleep(2)
 else:
    print(r_id,"Received")
    count2=count2+1
 
print("Total Approved = ",count)
print("Total Received = ",count2)
time.sleep(3)




def send_simple_message():


    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "animeshgupta720@gmail.com"
    password = ""
    receiver_email = "animeshgupta720@gmail.com"
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
        message="heello"
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

#if x=='Approved' or 'Delivered':
#    send_simple_message()
