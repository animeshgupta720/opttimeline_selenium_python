
### opttimeline_selenium_python
This project makes use of selenium module to perform webscraping on the USCIS website to check the OPT case status.

### Prerequisites:
```
1. Install the following Python modules:

- selenium - pip3 install selenium
- smtplib - pip3 install smtplib

2. Clone the project using  - *git clone https://github.com/animeshgupta720/opttimeline_selenium_python.git*

3. Install and test chromedriver using the following link - https://chromedriver.storage.googleapis.com/index.html?path=2.42/
```
Now you can run the script for two things - 1. to get just your own application status emailed 2. to get your own as well as a
few other application status' printed on CLI.

### Running the script to get only your application status:

When you execute the script *opt_atom.py*, it will prompt for the following inputs:

1. Path where chromedriver is installed
2. Your OPT application #
3. Your email
4. Your password (Don't worry your password is stored in local memory and sent for authentication over an encrypted channel 
using SMTPS)

Well, the *opt_atom.py* script will work fine if you run it manually; however, if you want the script to be run automatically
in a periodic manner, you will have to use **CRON**.

An example of a CRON job is mentioned below:

**30 * * * *  cd /home/animesh && /usr/bin/python3 opt_atom.py >> /home/animesh/log.txt 2>&1**

The above CRON job will execute every 30th minute of every hour in a day. 

**Note:** If you want to set the script to execute periodically, then hard code the following inputs in the script:

1. Make the path where chromedriver is installed static in your script 
2. Your OPT application #
3. Your email
4. Your password input (Make sure that this script is not shared with anyone as you've hardcoded your password here)

### Running the script to get your application status along with a few others sent close to your receipt date:

Open the script and go to line #51 and #64 and make the following changes:

#51 - Replace the range based on the range for which you want the data.
#64 - Replace "YSC209015" with the first nine letters in your application id.

For example, if your application id is this  - YSC2090163312; then make the following modifications to the opt_range.py file:

-  Replace "for i in range(3200,3215)" to "for i in range(3300,3315)".

-  Replace YSC209015 to YSC209016.

# Output

Now run the script to see an output like this:

```
Enter the path where chromedriver is installed:/Users/agupta4/Downloads/chromedriver
Enter your OPT application number:YSC2090153214
Enter your email: animeshgupta720@gmail.com
Enter email password:

YSC2090153200 Approved
YSC2090153201 Approved 
YSC2090153202 Approved 
YSC2090153203 Received
YSC2090153204 Approved 
YSC2090153205 Approved 
YSC2090153206 Approved 
YSC2090153207 Received
YSC2090153208 Received
YSC2090153209 Approved 
YSC2090153210 Approved 
YSC2090153211 Received
YSC2090153212 Received
YSC2090153213 Received
YSC2090153214 Received

```





