#Common locator file for all locators

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for Interview Scheduler Application - interview scheduler main page(interview_scheduler_main_page.py)

try_again_link = "xpath,//a[normalize-space()='Try again']"
sign_in_link = "xpath,//a[normalize-space()='Sign in']"
email_text ="xpath,//input[@id='identifierId']"
click_next = "xpath,//span[contains(text(),'Next')]"
password_text = "xpath,//input[@name='password']"
jobs_link = "xpath,//a[normalize-space()='Jobs']"
add_button = "xpath,//input[@id='add']"
job_role = "xpath,//input[@id='role']"
interviewers_text = "xpath,//input[@id='interviewers']"
submit_button = "xpath,//button[@id='submit']"
sort_arrow = "xpath,//th[@aria-label='ID: activate to sort column descending']"
click_delete = "xpath,//button[@data-jobrole='Manual Tester20']"
remove_button = "xpath,//button[@id='remove-button']"
cancel_button = "xpath,//button[normalize-space()='Cancel']"
close_button = "xpath,//button[normalize-space()='Close']"



