from scipy.spatial import distance
from scipy.interpolate import interp1d
import pandas as pd
import numpy as np

class ConversionFunctions:
    # Function for conversion of LLA to ECEF coordinate system
    @staticmethod
    def lla_to_ecef(input_df):
        # input: A dataframe that contains 4 columns

        # error message if LLA dataset does not include proper titles

        # Selecting the rows of the dataframe for determining the constants in this function
        time = input_df.iloc[:, 0]
        latitude = input_df.iloc[:, 1]
        longitude = input_df.iloc[:, 2]
        altitude = input_df.iloc[:, 3]

        # Converting the values to correct units
        t = time  # no conversion (ms)
        phi = (latitude * np.pi) / 180  # degrees to radians
        lam = (longitude * np.pi) / 180  # degrees radians
        h = altitude  # km

        # WGS84 parameters (m):
        a = 6378137.0
        b = 6356752.31424518  # b= a*(1-f)
        f = (1 / 298.257223563)
        e1 = np.sqrt(((a ** 2) - (b ** 2)) / (a ** 2))

        # Conversion to ecef in meters
        N = a / np.sqrt(1 - ((e1) ** 2) * np.sin(phi) * np.sin(phi))
        x = (N + h) * np.cos(phi) * np.cos(lam)
        y = (N + h) * np.cos(phi) * np.sin(lam)
        z = ((b ** 2 / a ** 2) * N + h) * np.sin(phi)

        # Formating the output
        df_out = pd.DataFrame()  # creates a df
        df_out['Unix epoch (ms)'] = time  # saves times
        df_out['X (m)'] = x  # saves X
        df_out['Y (m)'] = y  # saves Y
        df_out['Z (m)'] = z  # saves Z

        return df_out  # output

    # function for calculating velocity
    @staticmethod
    def velocity(time1, time2, df):
        # inputs: time1 and time2, two time points that exist within the range of the dataset
        # outputs: calculated velocity value

        # Use interpolate function to find functions for x,y, and z (interpolated values)
        x_interp = interp1d(df['Unix epoch (ms)'], df['X (m)'])
        y_interp = interp1d(df['Unix epoch (ms)'], df['Y (m)'])
        z_interp = interp1d(df['Unix epoch (ms)'], df['Z (m)'])

        posA = [x_interp(time1), y_interp(time1), z_interp(time1)]  # store interpolated values of x1,y1,z1 as position A
        posB = [x_interp(time2), y_interp(time2), z_interp(time2)]  # store interpolated values of x2,y2,z2 as position B
        dist = distance.euclidean(posA, posB)  # Calculate the euclidean distance between posA and posB
        time_delta = np.abs(time2 - time1)  # Calculate absolute value of time2-time1 to find duration
        velocity = dist / time_delta  # calculate velocity with interpolated positions and the given time

        return velocity
