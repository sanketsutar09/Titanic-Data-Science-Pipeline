import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
from scipy.stats import f_oneway

df= pd.read_csv('D:/INTERNSHIP/TitanicDataset_cleaned.csv')
print(df)