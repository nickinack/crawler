#Calculate formulas for reward , q_value , R(state , action):
from config import *
from csv_handling import *
import numpy as np


def calc_reward(df , r, D):
    rew = (np.absolute(r) - df)/D
    return rew



def calc_q(action,r,total_record_input,reward,D,candidate_set,df):
    index = candidate_set.index(action)
    q_value = reward[index]
    value = 0 #Formula application
    maxi = -10**10
    for element in candidate_set:
        if element != action:
            idx = candidate_set.index(element)
            value = reward[idx]
            value = value + (df[idx]/D)
            value = value - ((total_records_input * r[element])/(D**2))
            if value > maxi:
                value = maxi

    q_value = q_value + maxi
    return q_value

def calc_r(output_list):
    global total_records
    total_records = total_records + len(output_list)
    return len(output_list)



