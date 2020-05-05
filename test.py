import base64
import json
import requests
import numpy as np
import pickle
import os
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)



all_lineups = pickle.load(open('all_lineups.pkl', 'rb'))
lineups1 = dict()
lineups2 = dict()
for i in all_lineups:
    print('splitting, id = ', i)
    if(i % 2 == 0):
        lineups1[i] = all_lineups[i]
    else:
        lineups2[i] = all_lineups[i]

pickle.dump(lineups1, open('lineups1.pkl', 'wb'))
pickle.dump(lineups2, open('lineups2.pkl', 'wb'))