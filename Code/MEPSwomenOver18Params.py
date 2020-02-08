'''
Load parameters for estimating the model only on women in the MEPS.
'''
import numpy as np
import os
file_name = os.path.basename(__file__)
dot_i = file_name.find('.')
param_file_name = file_name[:dot_i]
eval_count = 0

# Specify parameters for the continuous state grid
x_min = -12.
x_max = 28.
x_count = 200

# Define parameters for loading in the data file
data_file = '../Data/Estimation/MEPSall.txt'
source_name = 'MEPS' # Name of dataset
figure_label = 'MEPSover18' # Text string to use as prefix for figure filenames
sex_list = [0]    # Only women in this dataset
T_max = 5         # Maximum number of periods for each individual
weight_col = 2    # Column of the data with observation weight
age_col = 4       # Column of the data with age
sex_col = 3       # Column of the data with male dummy
data_init_col = 5 # Column where data starts
measure_count = 1 # Number of measures in data per period
category_counts = [5]  # Number of categorical responses for each measure (list)
measure_names = ['SRHS'] # Abbreviation for each measure in data (list)
age_min = 18.0    # Minimum age in the data
age_max = 87.0    # Maximum age in the data
age_incr = 0.5    # Age increment in years
wave_length = 1   # Number of periods between actual data collection waves

# Define a test parameter vector
current_param_vec = np.array([ 
    2.68901648153,  # 0 Mort0
    0.0,  # 1 MortSex
    1.20162968501,  # 2 MortHealth1
    1.96981372973,  # 3 MortHealth2
    -5.03995275858,  # 4 MortHealth3
    0.0,  # 5 MortHealth4
    0.100864501896,  # 6 MortAge1
    -6.13916304163,  # 7 MortAge2
    0.575592442681,  # 8 MortAge3
    0.0,  # 9 MortAge4
    -1.00231858661,  # 10 MortHealthAge
    0.0,  # 11 MortSexAge
    2.46522846111,  # 12 Corr0
    4.98872587475,  # 13 CorrAge1
    -18.1946834571,  # 14 CorrAge2
    26.4189792466,  # 15 CorrAge3
    0.0,  # 16 CorrAge4
    7.61635532343,  # 17 Health0
    0.0,  # 18 HealthSex
    1.34008436419,  # 19 HealthAge1
    -2.67990484956,  # 20 HealthAge2
    2.01988898116,  # 21 HealthAge3
    -0.666650867425,  # 22 HealthAge4
    0.0,  # 23 HealthAgeSex
    9.40202310728,  # 24 xInitMean
    3.16590923928,  # 25 xInitStd
    0.501991238363,  # 26 SRHS_Coeff
    1.59665457092,  # 27 SRHS_Cut2
    1.79193177763,  # 28 SRHS_Cut3
    1.72269228697,  # 29 SRHS_Cut4
]) 

which_indices = np.array([0,2,3,4,6,7,8,10,12,13,14,15,17,19,20,21,22,24,25,26,27,28,29]) 
#which_indices = np.array([0,2,3,4,6,7,8,10])
#which_indices = np.array([17,19,20,21,22])
#which_indices = np.array([27,28,29])

# 697701.872621