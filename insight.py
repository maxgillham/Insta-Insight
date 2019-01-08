'''
Preprocessed data from utils.py will be called and operations to provide
contextual insight will be made in here
'''

from utils import *

import numpy as np
import sys

#from the photo description find commin
def common_photo_contents(contents):
    objts = []
    for i in contents: objts.extend(i.split(', '))
    counts = np.unique(objts, return_counts=True)
    return counts

if __name__ == '__main__':
    try:
        username = sys.argv[1]
        scraper = InstagramScraper()
        selenium_objects = scraper.get_account_photos(sys.argv[1])
        counts = common_photo_contents(parse_img_description(selenium_objects[:12]))
        print(counts)
    except:
        print('Must pass valid username as arguement to script')
