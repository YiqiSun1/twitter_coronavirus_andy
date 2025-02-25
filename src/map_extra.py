# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--output_folder',default='outputs')
args = parser.parse_args()

# imports
import os
import zipfile
import datetime 
import json
from collections import Counter,defaultdict

# load keywords
hashtags = [
    '#코로나바이러스',  # korean
    '#コロナウイルス',  # japanese
    '#冠状病毒',        # chinese
    '#covid2019',
    '#covid-2019',
    '#covid19',
    '#covid-19',
    '#coronavirus',
    '#corona',
    '#virus',
    '#flu',
    '#sick',
    '#cough',
    '#sneeze',
    '#hospital',
    '#nurse',
    '#doctor',
    ]

# initialize counters for language
counter_lang = defaultdict(lambda: Counter())

# initialize counters for country
counter_country = defaultdict(lambda: Counter())



# open the zipfile
with zipfile.ZipFile(args.input_path) as archive:

    # loop over every file within the zip file
    for i,filename in enumerate(archive.namelist()):
        print(datetime.datetime.now(),args.input_path,filename)

        # open the inner file
        with archive.open(filename) as f:

            # loop over each line in the inner file
            for line in f:

                # load the tweet as a python dictionary
                tweet = json.loads(line)

                # convert text to lower case
                text = tweet['text'].lower()

                # search hashtagsv
                for hashtag in hashtags:
                    lang = tweet['lang']
                    if 'place' in tweet and tweet['place'] is not None and tweet['place']['country_code'] is not None:
                         country = tweet['place']['country_code'] 
                    else:
                        country = 'unknown country'
                    if hashtag in text:
                        counter_lang[hashtag][lang] += 1
                        counter_country[hashtag][country] += 1
                        counter_lang['_all'][lang] += 1
                        counter_country['all'][country] += 1

# open the outputfile
try:
    os.makedirs(args.output_folder)
except FileExistsError:
    pass
output_path_base = os.path.join(args.output_folder,os.path.basename(args.input_path))

output_path_lang = output_path_base+'.lang'
output_path_country = output_path_base+ '.country'
print('saving',output_path_lang)
print('saving',output_path_country)
with open(output_path_lang,'w') as f:
    f.write(json.dumps(counter_lang))
with open(output_path_country,'w') as f:
    f.write(json.dumps(counter_country))
(venv) lambda-server:~/twitter_coronavirus_andy (master *+%=) $ vim src/map.py 

 53         # open the inner file
 54         with archive.open(filename) as f:
 55 
 56             # loop over each line in the inner file
 57             for line in f:
 58 
 59                 # load the tweet as a python dictionary
 60                 tweet = json.loads(line)
 61 
 62                 # convert text to lower case
 63                 text = tweet['text'].lower()
 64 
 65                 # search hashtagsv
 66                 for hashtag in hashtags:
 67                     lang = tweet['lang']
 68                     if 'place' in tweet and tweet['place'] is not None and tweet['place']['country_code'] is not None:
 69                         country = tweet['place']['country_code']
 70                     else:
 71                         country = 'unknown country'
 72                     if hashtag in text:
                            counter_lang[hashtag][lang] += 1
 74                         counter_country[hashtag][country] += 1
 75                     counter_lang['_all'][lang] += 1
 76                     counter_country['all'][country] += 1
 77 
 78 # open the outputfile
 79 try:
 80     os.makedirs(args.output_folder)
 81 except FileExistsError:
 82     pass
 83 output_path_base = os.path.join(args.output_folder,os.path.basename(args.input_path))
 84 
 85 output_path_lang = output_path_base+'.lang'
 86 output_path_country = output_path_base+ '.country'
 87 print('saving',output_path_lang)
 88 print('saving',output_path_country)
 89 with open(output_path_lang,'w') as f:
 90     f.write(json.dumps(counter_lang))
 91 with open(output_path_country,'w') as f:
 92     f.write(json.dumps(counter_country))
