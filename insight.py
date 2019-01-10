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
    for i in range(len(objts)):
        if objts[i] in photo_contents: objts[i] = photo_contents[objts[i]]
    counts = np.unique(objts, return_counts=True)
    return counts

if __name__ == '__main__':
    try:
        username = sys.argv[1]
        scraper = InstagramScraper()
        selenium_objects = scraper.get_account_photos(sys.argv[1])
        counts = common_photo_contents(parse_img_description(selenium_objects[:12]))
        max_ind = np.argmax(counts[1])
        print('Detected photo contents', counts[0])
        print('\nNumber of occurences in first 12 posts', counts[1])
        print('\nCommon content contains', counts[0][np.argmax(counts[1])])
    except:
        print('Must pass valid username as arguement to script')
