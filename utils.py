from selenium import webdriver


class InstagramScraper(object):

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

if __name__ == '__main__':
    scraper = InstagramScraper()
    selenium_objects = scraper.get_account_photos('maxgillham')
    print(selenium_objects)
