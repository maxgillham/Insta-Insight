from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import sys
import time

#This is the scraper class
class InstagramScraper(object):
    #init home page
    def __init__(self, username):
        self.home = "https://www.instagram.com/{}".format(username)
        options = Options()
        options.headless = False
        self.driver = webdriver.Chrome('./chromedriver/chromedriver', chrome_options=options)
        self.secondary_driver = webdriver.Chrome('./chromedriver/chromedriver', chrome_options=options)
        return
    #This will return instagram's algorithms guess on the contents of
    #the photo
    def get_photo_contents(self):
        #navagate to homepage
        self.driver.get(self.home)
        photos = self.driver.find_elements_by_class_name("KL4Bh")
        photo_contents = []
        for photo in photos:
            try: photo_contents.append(photo.find_element_by_tag_name("img").get_attribute("alt"))
            except: print("Failed")
        return photo_contents
    #this method returns an interger list of the number of likes each photo obtains
    def get_like_count_and_captions(self):
        #open photos and return like count
        self.driver.get(self.home)
        self.secondary_driver.get(self.home)
        photos = self.secondary_driver.find_elements_by_class_name("_bz0w")
        like_count = []
        caption_list = []
        for photo in photos:
            self.driver.get(photo.find_element_by_tag_name('a').get_attribute('href'))
            likes = self.driver.find_elements_by_class_name("zV_Nj")
            try: like_count.append(likes[0].find_element_by_tag_name('span').text)
            except: like_count.append('0')
            captions = self.driver.find_elements_by_class_name("C4VMK")
            try: caption_list.append(captions[0].find_element_by_tag_name('span').text)
            except: caption_list.append('No Caption')
            self.driver.get(self.home)
        return like_count, caption_list
    #sign into account
    def sign_in(self, username, password):
        #navagate to sign in page
        self.driver.get("https://www.instagram.com/accounts/login/")
        #find form inputs, username and pass input
        username_form = self.driver.find_elements_by_css_selector("form input")[0]
        password_form = self.driver.find_elements_by_css_selector("form input")[1]
        #enter username, password and hit enter
        username_form.send_keys(username)
        password_form.send_keys(password)
        password_form.send_keys(Keys.ENTER)
        time.sleep(2)
        return
    #get list of followers
    def get_followers(self):
        self.driver.get(self.home)
        followers_page = self.driver.find_element_by_css_selector('ul li a')
        followers_page.click()
        names = self.driver.find_elements_by_class_name("wo9IH")
        followers = []
        for name in names:
            test = name.get_attribute('href')
            print(test)
        return
    #a method to close the webdriver
    def exit(self):
        self.driver.close()
        self.secondary_driver.close()
        return

#This method will parse the image contents description to disclude labels
def parse_img_description(image_text):
    parsed = []
    for text in image_text:
        if text: parsed.append(text.split(': ')[1])
    return parsed

#I want to generalize between selfies and group photos
photo_contents = {
    '1 person' : 'selfies',
    '2 people' : 'group photos',
    '3 people' : 'group photos',
    '4 people' : 'group photos',
    '5 people' : 'group photos',
    '6 people' : 'group photos'
}


if __name__ == "__main__":
    scraper = InstagramScraper(sys.argv[1])
    scraper.sign_in(sys.argv[1], sys.argv[2])
    scraper.get_followers()
