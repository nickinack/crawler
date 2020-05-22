#Use RL to felicitate the crawling process
from config import *
from formula import *
from semantic_search import *
from csv_handling import *

def arg_max(action):
    global df
    global r
    global df
    global D
    global reward
    global candidate_set
    df[candidate_set.index(action)] = find_freq(action)
    for action1 in candidate_set:
        df[action1] = find_freq(action)
    '''r[candidate_set.index(action)] = calc_r(crawl(action))'''
    reward[candidate_set.index(action)] = calc_reward(df[candidate_set.index(action)],r[candidate_set.index(action)],D)
    csvfile = 'action_document.csv'
    with open(csvfile , 'r') as csv_file:
        for document in csv_file:
            for word in document:
                '''if(check_keyword(word)):
                        global candidate_set
                        candidate_set.append(keyword)
                    else:
                        update(df)
                        
                '''
    candidate_set.remove(action)
    q_table.remove(action)   #Doubt
    for action1 in candidate_set:
        reward[action1] = calc_reward(df[candidate_set.index(action1)] , r[candidate_set.index(action1)], D)
    for action1 in candidate_set:
        q_table[action1] = calc_q(action1 , r , total_records , reward , D , candidate_set , df)

    return np.argmax(q_table)




    

        
   
    
