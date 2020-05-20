import requests
import numpy as np
from bs4 import BeautifulSoup

url = (' ')   #url to be crawled
training_set = []  #set of actions already implemented
candidate_set = [] #set of actions to be implemented
initial_size = len(candidate_set) #initial search space
df = np.zeros((0,initial_size))   #document frequency
n_iter = 0  #number of iterations
domain_size = 0 #number of expected documents
reward = 0 #reward for a (state,action) pair ; can be updated inside the loop
q_table = np.zeros((n_iter , initial_size)) #q_table


