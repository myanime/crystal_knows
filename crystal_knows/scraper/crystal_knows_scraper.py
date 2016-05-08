import traceback
import time
from selenium import webdriver

class CrystalKnows:
    def __init__(self, data):
        #Login Details
        self.user_name = "maria.ivanova-msk@mail.ru"
        self.password = "test1234!"
        self.first_name = data['first_name']
        self.last_name =  data['last_name']
        self.data = data
        
    def scraper_crystal_knows(self):
        try:
            #Opens Browser
            driver = webdriver.Firefox()
            driver.get("https://www.crystalknows.com/users/sign_in")

            #Enters User Name
            login_box = driver.find_element_by_id('user_email')
            login_box.send_keys(self.user_name)

            #Enters Password
            password_box = driver.find_element_by_id('user_password')
            password_box.send_keys(self.password)

            #Clicks Submit Button
            submit = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div/div[4]/input')
            submit.click()

            #Log in Confirmation
            time.sleep(1)
            print "Log in Successful"

            #Open Advanced Search
            driver.get("https://www.crystalknows.com/people/advanced")

            #Input First Name
            first_name_box = driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div[1]/form/div/table/tbody/tr[1]/td[2]/input')
            first_name_box.send_keys(self.first_name)

            #Input Last Name
            last_name_box = driver.find_element_by_xpath('/html/body/div/div[5]/div/div[1]/form/div/table/tbody/tr[2]/td[2]/input')
            last_name_box.send_keys(self.last_name)

            #Click Search Button
            advanced_search_button = driver.find_element_by_xpath('/html/body/div/div[5]/div/div[1]/form/div/table/tbody/tr[6]/td[2]/button')
            advanced_search_button.click()

            #Search Confirmation
            print "Success Searching"
            time.sleep(1)

            #Returns FIRST search result
            #It is not difficult to follow the link and extract what is on the next pages, but without a pro account
            #there is nothing there to scrape. Could also scrape an array of all displayed data and do advanced searches.
            search_result = driver.find_element_by_css_selector('div.result-text').text

            #Updates the Response data
            self.data['about_person'] = search_result

            #Closes Browser
            driver.quit()
            
            return self.data
        except:
            #Closes Browser session
            driver.quit()
            
            #Returns Error message in JSON output
            self.data['about_person'] = "Error"

            #Server side traceback 
            traceback.print_exc()
            return self.data
def test():
    data = {'first_name': 'Taylor', 'last_name': 'Swift', 'about_person': ''}
    pop_star = CrystalKnows(data)
    pop_star.scraper_crystal_knows()
    print data['about_person']

