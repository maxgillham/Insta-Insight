from selenium import webdriver
import time

class InstagramScraper(object):

    def start_up(self):
        self.driver = webdriver.Chrome('chromedriver/chromedriver')

    def navigate_to(self, url):
        self.driver.get(url)

    def shut_down(self):
        self.driver.close()

    def get_account_photos(self, username):
        self.start_up()
        url = "https://www.instagram.com/{}".format(username)
        self.navigate_to(url)
        photos = self.driver.find_elements_by_class_name("KL4Bh")
        image_text = []
        for photo in photos:
            try:
                image = photo.find_element_by_tag_name("img")
                image_text.append(image.get_attribute("alt"))
            except:
                print("Failed")
        self.shut_down()
        return image_text

