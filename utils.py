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

        #open photos and return like count
        open_photos = driver.find_elements_by_class_name("_bz0w")
        links = []
        for photo in open_photos:
            links.append(photo.find_element_by_tag_name('a').get_attribute('href'))
        driver.close()
        return image_text, links

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
        scraper = InstagramScraper()
        contents, links = scraper.get_account_photos(sys.argv[1])
        print(contents)
        print('\n\n\nparsed as ', parse_img_description(contents[:12]))
        print('\n\n\nWith the following links', links)
    except:
        print('Must pass valid username as arguement to script')
