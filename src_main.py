# Import the necessary libraries
from src_functions import ConversionFunctions
import pandas as pd
import numpy as np


# Read the csv file from dataset folder as a dataframe 'orig_dataset'
orig_dataset = pd.read_csv(r"dataset/SciTec_code_problem_data.csv",
                      names=["Unix epoch (ms)", "Latitude (deg)", "Longitude (deg)","Altitude (km)"])

# Call function
ecef_dataset = ConversionFunctions.lla_to_ecef(orig_dataset)

# Shift columns down from ecef_dataset and save as new dataframe 'ecef_shifted'
ecef_shifted = ecef_dataset.shift(1).copy()

# Find euclidean distance between ecef_dataset and ecef_shifted and store as 'euc_dist_dataset'
euc_dist_dataset = (ecef_dataset['X (m)'] - ecef_shifted['X (m)'])**2 + (ecef_dataset['Y (m)'] - ecef_shifted['Y (m)'])**2 + (ecef_dataset['Z (m)'] - ecef_shifted['Z (m)'])**2
euc_dist_dataset = np.sqrt(euc_dist_dataset)

# Find difference in consecutive time points for delta time calculation
delta_time = ecef_dataset['Unix epoch (ms)'] - ecef_shifted['Unix epoch (ms)']
delta_time_df = pd.DataFrame({'Unix epoch delta (ms)':delta_time})

# Find the velocities between consecutive time points
vel_df = euc_dist_dataset/delta_time
ecef_velocity = pd.DataFrame({'ECEF Velocities':vel_df})

# Combine dataframes of time and velocity
time = ecef_dataset['Unix epoch (ms)']
vel_result = pd.concat([time, ecef_velocity], axis=1, ignore_index=False)

# Show velocities and convert to csv output to results folder
vel_result.to_csv(r'~/Desktop/PycharmProjects/SciTec_Solution/results/ECEF Velocities.csv')

# Combine dataframe of enix epoch, x, y, z, and ecef veleocities for next analysis
df = pd.concat([ecef_dataset, ecef_velocity], axis=1, ignore_index=False)


# velocity function called at these specified times, value is stored as 'velocity'
velocity = ConversionFunctions.velocity(1532334000, 1532335268, df)
print(velocity)  # stdout

