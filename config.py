import requests
import numpy as np
from bs4 import BeautifulSoup

url = (' ')   #url to be crawled
training_set = []  #set of actions already implemented
candidate_set = [] #set of actions to be implemented
initial_size = len(candidate_set) #initial search space
df = np.zeros((initial_size))   #document frequency
n_iter = 0  #number of iterations
domain_size = 0 #number of expected documents
reward = np.zeros(initial_size) #reward for a (state,action) pair ; can be updated inside the loop
q_table = np.zeros((n_iter , initial_size)) #q_table
r = np.zeros(initial_size) #Represents the number of documents acquired at the state st
records_st = np.zeros((initial_size)) #Represents the total number of records collected till the present state

