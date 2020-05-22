import requests
import numpy as np
from bs4 import BeautifulSoup

global url
url = 'abebooks.com'   #url to be crawled
global training_set
training_set = []  #set of actions already implemented
global candidate_set
candidate_set = [] #set of actions to be implemented
global initial_size
initial_size = len(candidate_set) #initial search space
global df
df = list(np.zeros(initial_size))   #document frequency
global n_iter
n_iter = 1  #number of iterations
global D
D = 0 #number of expected documents
global reward
reward =list(np.zeros(initial_size)) #reward for a (state,action) pair ; can be updated inside the loop
global q_table
q_table = list(np.zeros((initial_size))) #q_table
global r
r = list(np.zeros(initial_size)) #Represents the number of documents acquired at the state st
global total_records
total_records = 0

