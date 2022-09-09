"""
This is an example automated test weather shopper Home page
Our automated test will do the following:
    #Open Weathershopper.
    #Click the qxf2 sevices link.
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.text_field_conf as conf
import conf.testrail_caseid_conf as testrail_file
import pytest


@pytest.mark.GUI
def test_interview_scheduler_home(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object and click the qxf2 sevices link.
        test_obj = PageFactory.get_page_object("interview scheduler main page")
        #Set start_time with current time
        start_time = int(time.time())
        test_obj.turn_on_highlight()
        email = conf.email
        password = conf.password
        job = conf.job
        interviewer = conf.interviewer 
        # window = conf.window

        # Click the qxf2 sevices link
        click_try_again = test_obj.click_try_again_link()
        test_obj.log_result(click_try_again,
                            positive="Able to click link\n",
                            negative="Not able to click link\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        click_sign_in = test_obj.click_sign_in_link()
        test_obj.log_result(click_sign_in,
                            positive="Able to click link\n",
                            negative="Not able to click link\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        click_email = test_obj.set_email(email)
        test_obj.log_result(click_email,
                            positive="Able to click link\n",
                            negative="Not able to click link\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        next_button = test_obj.click_next_button()
        test_obj.log_result(next_button,
                            positive="Able to click link\n",
                            negative="Not able to click link\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        click_password = test_obj.set_password(password)
        test_obj.log_result(click_password,
                            positive="Able to click link\n",
                            negative="Not able to click link\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        next_button = test_obj.click_next_button()
        test_obj.log_result(next_button,
                            positive="Able to click link\n",
                            negative="Not able to click link\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        job_link = test_obj.click_jobs_link()
        test_obj.log_result(job_link,
                            positive="Able to click link\n",
                            negative="Not able to click link\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        up_arrow = test_obj.click_up_arrow()
        test_obj.log_result(up_arrow,
                            positive="Able to click link\n",
                            negative="Not able to click link\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        delete_link = test_obj.click_delete_button()
        test_obj.log_result(delete_link,
                            positive="Able to click link\n",
                            negative="Not able to click link\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        remove = test_obj.click_remove_button()
        test_obj.log_result(remove,
                            positive="Able to click link\n",
                            negative="Not able to click link\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        close = test_obj.click_close_button()
        test_obj.log_result(close,
                            positive="Able to click link\n",
                            negative="Not able to click link\n")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        # Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__

#---START OF SCRIPT
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()

    #Run the test only if the options provided are valid
    if options_obj.check_options(options):
        test_obj = PageFactory.get_page_object("Zero",base_url=options.url)

        #Setup and register a driver
        test_obj.register_driver(options.remote_flag,options.os_name,options.os_version,options.browser,options.browser_version,options.remote_project_name,options.remote_build_name)

        #Setup TestRail reporting
        if options.testrail_flag.lower()=='y':
            if options.test_run_id is None:
                test_obj.write('\033[91m'+"\n\nTestRail Integration Exception: It looks like you are trying to use TestRail Integration without providing test run id. \nPlease provide a valid test run id along with test run command using -R flag and try again. for eg: pytest -X Y -R 100\n"+'\033[0m')
                options.testrail_flag = 'N'
            if options.test_run_id is not None:
                test_obj.register_testrail()
                test_obj.set_test_run_id(options.test_run_id)

        if options.tesults_flag.lower()=='y':
            test_obj.register_tesults()

        test_interview_scheduler_home(test_obj)

        #teardowm
        test_obj.wait(5)
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        #print(option_obj.print_usage())