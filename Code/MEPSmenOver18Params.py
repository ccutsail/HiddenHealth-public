'''
Load parameters for estimating the model on men in the MEPS.
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
sex_list = [1]    # Only men in this dataset
T_max = 5         # Maximum number of periods for each individual
weight_col = 2    # Column of the data with observation weight
age_col = 4       # Column of the data with age
sex_col = 3       # Column of the data with male dummy
data_init_col = 5 # Column where data starts
measure_count = 1 # Number of measures in data per period
category_counts = [5] # Number of categorical responses for each measure (list)
measure_names = ['SRHS'] # Abbreviation for each measure in data (list)
age_min = 18.0    # Minimum age in the data
age_max = 87.0    # Maximum age in the data
age_incr = 0.5    # Age increment in years
wave_length = 1   # Number of periods between actual data collection waves

# Define a test parameter vector
current_param_vec = np.array([ 
    2.48794980354,  # 0 Mort0
    0.0,  # 1 MortSex
    0.723823176721,  # 2 MortHealth1
    2.46554993362,  # 3 MortHealth2
    -5.98140734322,  # 4 MortHealth3
    0.0,  # 5 MortHealth4
    1.01991753197,  # 6 MortAge1
    -12.5280908984,  # 7 MortAge2
    16.927961843,  # 8 MortAge3
    0.0,  # 9 MortAge4
    6.05482707436,  # 10 MortHealthAge
    0.0,  # 11 MortSexAge
    2.49951180713,  # 12 Corr0
    2.2776682388,  # 13 CorrAge1
    2.01373030827,  # 14 CorrAge2
    -28.9726903042,  # 15 CorrAge3
    0.0,  # 16 CorrAge4
    7.75095802806,  # 17 Health0
    0.0,  # 18 HealthSex
    1.41741444582,  # 19 HealthAge1
    -2.85600252333,  # 20 HealthAge2
    2.10940168127,  # 21 HealthAge3
    -0.696098123864,  # 22 HealthAge4
    0.0,  # 23 HealthAgeSex
    9.72337856249,  # 24 xInitMean
    2.91153983994,  # 25 xInitStd
    0.51322016921,  # 26 SRHS_Coeff
    1.55024048242,  # 27 SRHS_Cut2
    1.79388250661,  # 28 SRHS_Cut3
    1.63843263155,  # 29 SRHS_Cut4
]) 

which_indices = np.array([0,2,3,4,6,7,8,10,12,13,14,15,17,19,20,21,22,24,25,26,27,28,29])
#which_indices = np.array([0,2,3,4,6,7,8,10])
#which_indices = np.array([12,13,14,15])
#which_indices = np.array([17,19,20,21,22])

596870.042348