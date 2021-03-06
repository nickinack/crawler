#Handle csv's used
from config import *
import pandas as pd
import pandas as pd
import csv
import re

#function to create headers for the action set
def add_columns(candidate_set , initial_size):
    csvfile = 'action_document.csv'
    with open(csvfile , 'w', newline = '') as csv_file:
        writer = csv.DictWriter(csv_file , fieldnames = candidate_set)
        writer.writeheader()

#function to append the document list
def append_columns(action , document, candidate_set):
    csvfile = 'action_document.csv'
    with open(csvfile , 'a', newline = '') as csv_file:
        writer = csv.writer(csv_file)
        idx = candidate_set.index(action)
        writer.writerow([''] * (idx) + [document])
#function  to find document frequency
def find_freq(keyword):
    df_s = 0
    csvfile = 'action_document.csv'
    iter = 0
    with open(csvfile) as csv_file:
        for document in csv_file:
            if iter == 0:
                iter = iter + 1
                continue
            document = document.replace(',' , '')
            document = document.split()
            print(document)
            if keyword in document:
                df_s = df_s + 1

    return df_s

def update(new_action):
    global candidate_set
    candidate_set.append(new_action)
    global initial_size
    initial_size = initial_size + 1
    global df
    df.append(0)
    global reward
    reward.append(0)
    global q_table
    q_table.append(0)
    global r
    r.append(0)
    global records_st
    records_st.append(0)
    csvfile = 'action_document.csv'
    info = []
    with open(csvfile , 'r') as csv_file:
        reader = csv.reader(csv_file , delimiter = ',')
        iter = 0
        for element in reader:
            if iter == 0:
                iter = iter + 1
                element.append(new_action)
            info.append(element)
    print(info)
    writer = csv.writer(open(csvfile , 'w' , newline = "") , delimiter = ',')
    for element in info:
        writer.writerow(element)


            
        


