'''
Preprocessed data from utils.py will be called and operations to provide
contextual insight will be made in here
'''

from utils import *

import numpy as np
import sys
import re
import getpass

#from the photo description find common contents
def common_photo_contents(contents):
    objts = []
    for i in contents: objts.extend(i.split(', '))
    for i in range(len(objts)):
        if objts[i] in photo_contents: objts[i] = photo_contents[objts[i]]
    counts = np.unique(objts, return_counts=True)
    return counts

#sort photo description in terms of likes obtained for each photo
def content_sorted_by_likes(contents, likes):
    return [contents for _, contents in sorted(zip(likes, contents), reverse=True)]

#return contents of hashtags from captions of photos
def get_hashtags_from_captions(captions):
    hashtags = []
    for cap in captions: hashtags.extend(re.findall('#[^\s]+', cap))
    return hashtags

if __name__ == '__main__':
    try:
        username = input('Enter username: ')
        password = getpass.getpass('Enter password: ')
        scraper = InstagramScraper(username)
        contents = scraper.get_photo_contents()
        content_counts = common_photo_contents(parse_img_description(contents[:12]))
        like_count, caption_list = scraper.get_like_count_and_captions()
        top_content = content_sorted_by_likes(contents, like_count)
        hashtags = get_hashtags_from_captions(caption_list)
        print('Detected photo contents', content_counts[0])
        print('\nCommon content contains', content_counts[0][np.argmax(content_counts[1])])
        print('\nLikes obtained by each post', like_count)
        print('\nMost likes on photos containing', parse_img_description(top_content[:3]))
        print('\nHashtags used', hashtags)
        scraper.exit()
    except:
        print('Must pass valid username as arguement to script')
