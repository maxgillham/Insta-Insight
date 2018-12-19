from selenium import webdriver

class InstagramScraper(object):

    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver/chromedriver')

    def navigate_to(self, url):
        self.driver.get(url)

    def get_account_photos(self, username):
        url = "https://www.instagram.com/{}".format(username)
        self.navigate_to(url)
        photos = self.driver.find_elements_by_class_name("KL4Bh")
        image_text = []
        for photo in photos:
            try:
                image = photo.find_element_by_tag_name("img")
                image_text.append(image)
            except:
                print("Failed")
        return image_text

