'''
Load parameters for estimating the model only on men over 50 from the HRS,
treating each period as a year.
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
data_file = '../Data/Estimation/HRSallAnnual.txt'
source_name = 'HRS' # Name of dataset
figure_label = 'HRSover50a' # Text string to use as prefix for figure filenames
sex_list = [1]    # Only men in this dataset
T_max = 21        # Maximum number of periods for each individual
weight_col = 1    # Column of the data with observation weight
age_col = 3       # Column of the data with age
sex_col = 2       # Column of the data with male dummy
data_init_col = 4 # Column where data starts
measure_count = 1 # Number of measures in data per period
category_counts = [5]  # Number of categorical responses for each measure (list)
measure_names = ['SRHS'] # Abbreviation for each measure in data (list)
age_min = 50.0    # Minimum age in the data
age_max = 115.0   # Maximum age in the data
age_incr = 1.0    # Age increment in years
wave_length = 2   # Number of periods between actual data collection waves

# Define a test parameter vector
current_param_vec = np.array([ 
    2.0624432993,  # 0 Mort0
    0.0,  # 1 MortSex
    1.44884353656,  # 2 MortHealth1
    0.89118897035,  # 3 MortHealth2
    -2.60761172115,  # 4 MortHealth3
    0.0,  # 5 MortHealth4
    -4.67182254176,  # 6 MortAge1
    21.0686811018,  # 7 MortAge2
    -130.010334291,  # 8 MortAge3
    0.0,  # 9 MortAge4
    -5.33322973677,  # 10 MortHealthAge
    0.0,  # 11 MortSexAge
    3.38785926829,  # 12 Corr0
    1.14652235237,  # 13 CorrAge1
    0.0,  # 14 CorrAge2
    0.0,  # 15 CorrAge3
    0.0,  # 16 CorrAge4
    3.18804841317,  # 17 Health0
    0.0,  # 18 HealthSex
    0.602198653088,  # 19 HealthAge1
    -2.29478749458,  # 20 HealthAge2
    0.0,  # 21 HealthAge3
    0.0,  # 22 HealthAge4
    0.0,  # 23 HealthAgeSex
    8.0679311744,  # 24 xInitMean
    4.50880636012,  # 25 xInitStd
    0.440453479051,  # 26 SRHS_Coeff
    1.65435727867,  # 27 SRHS_Cut2
    1.74385395531,  # 28 SRHS_Cut3
    1.99630968667,  # 29 SRHS_Cut4
]) 

which_indices = np.array([0,2,3,4,6,7,8,10,12,13,17,19,20,24,25,26,27,28,29]) 
#which_indices = np.array([0,2,3,4,6,7,8,10])
#which_indices = np.array([12,13])
#which_indices = np.array([17,19,20])


# 102729.989914