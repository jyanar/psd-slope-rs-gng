import seaborn
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn import linear_model
mpl.rcParams['figure.figsize'] = (16, 10)

df = pd.read_csv('../data/pipeline-full/ya-oa-full-linreg-30-45.csv')

oa = df[df.AGE >= 60]
oa = oa[oa.CLASS != 'SA']
ya = df[df.AGE <= 35.5] 

channels = ["AVG_OA_PSD_EYESC","AVG_OA_PSD_EYESO","AVG_YA_PSD_EYESC","AVG_YA_PSD_EYESO","AVG_PSD_EYESC","AVG_PSD_EYESO","A1_EYESC","A1_EYESO","A2_EYESC","A2_EYESO","A3_EYESC","A3_EYESO","A4_EYESC","A4_EYESO","A5_EYESC","A5_EYESO","A6_EYESC","A6_EYESO","A7_EYESC","A7_EYESO","A8_EYESC","A8_EYESO","A10_EYESC","A10_EYESO","A11_EYESC","A11_EYESO","A12_EYESC","A12_EYESO","A13_EYESC","A13_EYESO","A14_EYESC","A14_EYESO","A15_EYESC","A15_EYESO","A16_EYESC","A16_EYESO","A17_EYESC","A17_EYESO","A18_EYESC","A18_EYESO","A21_EYESC","A21_EYESO","A22_EYESC","A22_EYESO","A23_EYESC","A23_EYESO","A24_EYESC","A24_EYESO","A25_EYESC","A25_EYESO","A26_EYESC","A26_EYESO","A27_EYESC","A27_EYESO","A29_EYESC","A29_EYESO","A30_EYESC","A30_EYESO","A31_EYESC","A31_EYESO","B1_EYESC","B1_EYESO","B2_EYESC","B2_EYESO","B3_EYESC","B3_EYESO","B4_EYESC","B4_EYESO","B5_EYESC","B5_EYESO","B6_EYESC","B6_EYESO","B8_EYESC","B8_EYESO","B9_EYESC","B9_EYESO","B10_EYESC","B10_EYESO","B11_EYESC","B11_EYESO","B12_EYESC","B12_EYESO","B13_EYESC","B13_EYESO","B14_EYESC","B14_EYESO","B17_EYESC","B17_EYESO","B18_EYESC","B18_EYESO","B19_EYESC","B19_EYESO","B20_EYESC","B20_EYESO","B21_EYESC","B21_EYESO","B22_EYESC","B22_EYESO","B23_EYESC","B23_EYESO","B24_EYESC","B24_EYESO","B26_EYESC","B26_EYESO","B27_EYESC","B27_EYESO","B28_EYESC","B28_EYESO","B29_EYESC","B29_EYESO","B30_EYESC","B30_EYESO","FRONTAL_EYESC","FRONTAL_EYESO","LTEMPORAL_EYESC","LTEMPORAL_EYESO","CENTRAL_EYESC","CENTRAL_EYESO","RTEMPORAL_EYESC","RTEMPORAL_EYESO","OCCIPITAL_EYESC","OCCIPITAL_EYESO"]
for ch in channels:
    result = stats.ttest_ind(ya[ch], oa[ch], equal_var=False)
    if result[1] < 0.05:
        print("{}:\t{:.2f},\t{:.3f}".format(ch, result[0], result[1]))
