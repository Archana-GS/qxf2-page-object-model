"""
This class models the interview scheduler home page
The page consists of some texts, buttons, links
"""
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Interview_Scheduler_Home_Object:
    "Page object for the interview scheduler home page"

    # locators
    try_again_link = locators.try_again_link
    sign_in_link = locators.sign_in_link
    email_text = locators.email_text
    click_next = locators.click_next
    password_text = locators.password_text
    jobs_link = locators.jobs_link
    add_button = locators.add_button
    job_role = locators.job_role
    interviewers_text = locators.interviewers_text
    submit_button = locators.submit_button
    sort_arrow = locators.sort_arrow
    click_delete = locators.click_delete
    remove_button = locators.remove_button
    close_button = locators.close_button

    # Click try again link
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_try_again_link(self):
        "Click try again link"
        result_flag = self.click_element(self.try_again_link)
        return result_flag

    # Click sign in link
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_sign_in_link(self):
        "Click sign in link"
        result_flag = self.click_element(self.sign_in_link)
        return result_flag
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.email_text,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_next_button(self):
        "Click next button"
        result_flag = self.click_element(self.click_next)
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_password(self,password):
        "Set the password on the form"
        result_flag = self.set_text(self.password_text,password)
        self.conditional_write(result_flag,
            positive='Set the password to: %s'%password,
            negative='Failed to set the password in the form',
            level='debug')
        return result_flag

    # @Wrapit._exceptionHandler
    # @Wrapit._screenshot
    # def click_next_button(self):
    #     "Click next button"
    #     result_flag = self.click_element(self.click_next)
    #     return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_jobs_link(self):
        "Click jobs link"
        result_flag = self.click_element(self.jobs_link)
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_add_button(self):
        "Click add button"
        result_flag = self.click_element(self.add_button)
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_job(self,job):
        "Set the job role on the form"
        result_flag = self.set_text(self.job_role,job)
        self.conditional_write(result_flag,
            positive='Set the job role to: %s'%job,
            negative='Failed to set the job role in the form',
            level='debug')
        return result_flag

    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_interviewer(self,interviewer):
        "Set the interviewer on the form"
        result_flag = self.set_text(self.interviewers_text,interviewer)
        self.conditional_write(result_flag,
            positive='Set the interviewer to: %s'%interviewer,
            negative='Failed to set the interviewer in the form',
            level='debug')
        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_submit_button(self):
        "Click submit button"
        result_flag = self.click_element(self.submit_button)
        return result_flag
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def page_switch(self,OK):
        "Click ok button"
        result_flag = self.switch_page(self)
        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_up_arrow(self):
        "Click up arrow button"
        result_flag = self.click_element(self.sort_arrow)
        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_delete_button(self):
        "Click delete button"
        result_flag = self.click_element(self.click_delete)
        return result_flag
        
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_remove_button(self):
        "Click remove button"
        result_flag = self.click_element(self.remove_button)
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_close_button(self):
        "Click remove button"
        result_flag = self.click_element(self.close_button)
        return result_flag

    
    