from selenium import webdriver
import sys

#This is the scraper class
class InstagramScraper(object):
    #This will return instagram's algorithms guess on the contents of
    #the photo
    def get_account_photos(self, username):
        driver = webdriver.Chrome('./chromedriver/chromedriver')
        url = "https://www.instagram.com/{}".format(username)
        driver.get(url)
        photos = driver.find_elements_by_class_name("KL4Bh")
        image_text = []
        for photo in photos:
            try:
                image = photo.find_element_by_tag_name("img")
                image_text.append(image.get_attribute("alt"))
            except:
                print("Failed")
        driver.close()
        return image_text

#This method will parse the image contents description to disclude labels
def parse_img_description(image_text):
    parsed = []
    for text in image_text:
        if text: parsed.append(text.split(': ')[1])
    return parsed

if __name__ == '__main__':
    scraper = InstagramScraper()
    selenium_objects = scraper.get_account_photos(sys.argv[1])
    print(selenium_objects, '\n\n\nof length', len(selenium_objects))
    print('\n\n\nparsed as ', parse_img_description(selenium_objects[:12]))
