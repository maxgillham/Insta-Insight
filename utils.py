from selenium import webdriver
import sys

#This is the scraper class
class InstagramScraper(object):
    #init home page
    def __init__(self, username):
        self.home = "https://www.instagram.com/{}".format(username)
        self.driver = webdriver.Chrome('./chromedriver/chromedriver')
        self.secondary_driver = webdriver.Chrome('./chromedriver/chromedriver')
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
    def get_like_count(self):
        #open photos and return like count
        self.driver.get(self.home)
        self.secondary_driver.get(self.home)
        photos = self.secondary_driver.find_elements_by_class_name("_bz0w")
        like_count = []
        for photo in photos:
            self.driver.get(photo.find_element_by_tag_name('a').get_attribute('href'))
            likes = self.driver.find_elements_by_class_name("zV_Nj")
            try: like_count.append(likes[0].find_element_by_tag_name('span').text)
            except: like_count.append(0)
            self.driver.get(self.home)
        return like_count
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

if __name__ == '__main__':

    try:
        scraper = InstagramScraper(sys.argv[1])
        contents = scraper.get_photo_contents()
        print('\nContents ', parse_img_description(contents[:12]))
        like_count = scraper.get_like_count()
        print('\nLikes obtained', like_count)
        scraper.exit()
    except:
        print('Must pass valid username as arguement to script')
