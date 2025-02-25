import matplotlib.pyplot as plt

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
#sorted_data = dict(sorted(items.items(), key=lambda x: x[1], reverse=True)[:10])
sort_data = items[0:10]
print(sort_data)

#for i,(k,v) in enumerate(items):
 #   print(k,':',v)
  #  if i == 11:
   #     break

#create a bar graph with x values: input and y values: value. Only need 10 values
languages, counts = zip(*sort_data)

plt.figure(figsize=(12, 6))
plt.bar(languages, counts, color='skyblue')
plt.title('Language Distribution')
plt.xlabel('Languages')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
save_directory = "/home/ysun26/twitter_coronavirus_andy/src"
filename = "language_distribution.png"
full_path = os.path.join(save_directory, filename)
plt.savefig('language_distribution.png', dpi=300)
