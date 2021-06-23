from riotwatcher import LolWatcher, ApiError
import pandas as pd

names = []
for i in range(5):
    names.append(input().split(' ')[0])

api_key = 'RGAPI-cf9dd47f-04ac-448f-a031-8215ecb67722'#Replace this with your API
watcher = LolWatcher(api_key)
my_region = 'oc1'

total=0
no=0

for i in range(5):
    me = watcher.summoner.by_name(my_region, names[i])
    my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
    try:
        win_rate = (my_ranked_stats[0]['wins']/(my_ranked_stats[0]['losses']+my_ranked_stats[0]['wins']))   
        total = total + win_rate
        no = no + 1
        print(names[i],"has a win rate of",win_rate*100,"%")
    except IndexError:
        print(names[i],"has not yet played ranked")

print(" ")
print("The Average win rate is",(total/no)*100,"%")
