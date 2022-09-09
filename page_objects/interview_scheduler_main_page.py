"""
This class models the Selenium main page.
URL: weathershopper-pythonanywhere
The page consists of a buttons, texts, links 
"""
from .Base_Page import Base_Page
from .interview_scheduler_home_object import Interview_Scheduler_Home_Object

class Interview_Scheduler_Main_Page(Base_Page,Interview_Scheduler_Home_Object):
    def start(self):
        url='/home'
        self.open(url)


