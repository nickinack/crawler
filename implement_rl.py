#Use RL to felicitate the crawling process
from config import *
from formula import *
from csv_handling import *

def arg_max(action):
    global df
    global r
    global df
    global D
    global reward
    global candidate_set
    df[candidate_set.index(action)] = find_freq(action)
    r[candidate_set.index(action)] = calc_r(crawl(action))
    reward[candidate_set.index(action)] = calc_reward(df,r,D)
    csvfile = 'action_document.csv'
    with open(csvfile , 'r') as csv_file:
        for document in csv_file:
            '''if(check_keyword()):
                global candidate_set
                candidate_set.append(keyword)
                '''
   
    
