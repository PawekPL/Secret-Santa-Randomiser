import selenium.webdriver.firefox as ffx
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config as c
import smtplib, ssl
import email

#setting a new password for the email, so that no one knows who got who

email = "your_hotmail_email@hotmail.com"
password = 'password'
new_password = c.randpass


driver = ffx.webdriver.WebDriver()
driver.get(url="https://account.live.com/password/Change?mkt=en-GB&refd=account.microsoft.com&refp=profile&fref=profile.banner.change-password")
element = driver.find_element_by_id("i0116")
element.send_keys(email)
button = driver.find_element_by_id("idSIButton9")
button.click()
time.sleep(0.5)
element = driver.find_element_by_id("i0118")
element.send_keys(password)

time.sleep(1)
button = driver.find_element_by_id("idSIButton9")

button.click()
verify = driver.find_element_by_id('idDiv_SAOTCS_Proofs')
verify.click()

time.sleep(0.5)
verifym = driver.find_element_by_id('idTxtBx_SAOTCS_ProofConfirmation')
verifym.send_keys('backup_email_in_case_everything_gets_broken@personal.com')
verify = driver.find_element_by_id('idSubmit_SAOTCS_SendCode')
verify.click()

time.sleep(1)
verifym = driver.find_element_by_id('idTxtBx_SAOTCC_OTC')
verifym.send_keys(input('Enter code from your backup adress: '))
verify = driver.find_element_by_id('idSubmit_SAOTCC_Continue')
verify.click()
                  
time.sleep(2)
cur_pass = driver.find_element_by_id('iCurPassword')
cur_pass.send_keys(password)
new_pass = driver.find_element_by_id('iPassword')
new_pass.send_keys(new_password)
conf_pass = driver.find_element_by_id('iRetypePassword')
conf_pass.send_keys(new_password)

time.sleep(0.5)
submit = driver.find_element_by_id('UpdatePasswordAction')
submit.click()

driver.quit()
print('Password has been changed')


# sending emails to everyone 

port = 587

mail = smtplib.SMTP("smtp.office365.com",port)
mail.ehlo()
mail.starttls()
mail.login(email,new_password)
print('Logged in')
try:
    matches = c.name_match()
except:
    try:
    time.sleep(15) # a break so that the seed for the generator changes
    matches = c.name_match()
    except:
        try:
        time.sleep(15) # a break so that the seed for the generator changes
        matches = c.name_match()
        except:
            try:
            time.sleep(15) # a break so that the seed for the generator changes
            matches = c.name_match()
            except:
                print('''The function name_match doesn't seem to be working correctly,
check if you saved the config.py file and if the number of people > 1.
If neither of those were your solutions (you are very lucky cause this is rare af, msg me on github if it actually happens)
wait for a few minutes and try again.
'''

print('Names have been matched')
try:
    for match in matches: 
        msg = """
        You are a secret santa to: 






                                %s
        """ % (match[0])

        mail.sendmail(from_addr=email,to_addrs=match[1],msg=msg)
    print('Emails have been sent')
except:
    print('Don\'t forget to authenticate your hotmail adress first')
mail.close()

print('''
Check your email to see who you are a Secret santa to.
(The email might be in the SPAM folder)
''')

