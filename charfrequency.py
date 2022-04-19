import collections
import os
import re
from matplotlib import pyplot as plt

def text_to_char_dict(origText):
    #remove special characters, numbers and make lowercase
    cleanText = re.sub('[^A-Za-z]+', '', str(origText).lower()) 
    letterFreq = collections.Counter(cleanText)
    sortedFreq = dict(sorted(letterFreq.items(),key = lambda i: i[0], reverse=True))
    return sortedFreq

def text_to_char_dict_tests():
    test_dict = text_to_char_dict('a1z~![29Ab')
    assert test_dict['a'] == 2 #Passes if it detects upper and lower A
    assert len(test_dict) == 3 #should only detect 3 characters - a, z, b

if __name__ =='__main__':
    text_to_char_dict_tests()
    dirname = os.path.abspath('')
    filename = 'resumetest.txt'
    fullpath = os.path.join(dirname, filename)

    with open(fullpath,"r", encoding='utf-8') as f:
        origText = f.readlines()
        char_dict = text_to_char_dict(origText)
  
    plt.figure(figsize=(10,10))
    plt.barh(list(char_dict.keys()), char_dict.values(), color='b')
    plt.suptitle("Frequency vs. Character from {}".format(filename),fontsize=24)
    plt.annotate('Source: {}'.format(fullpath),
                xy = (1.0, -0.1),
                xycoords='axes fraction',
                ha='right',
                va="center",
                fontsize=10)

    plt.xlabel("Frequency")
    plt.ylabel("Character")
    #plt.show()
    plt.savefig("char_freq_chart.png", dpi=100)
  