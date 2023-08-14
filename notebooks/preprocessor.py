
import numpy as np
from sklearn.preprocessing import StandardScaler

class Preprocessor : 
    def __init__ (self, df):
        self.df = df.copy()
        
    def del_ID (self) :
        self.df.drop(columns=['CustomerID', 'Gender', 'Age'	], inplace=True)
      
    def x_standardized  (self) :
        scaler = StandardScaler()
        columns_to_standardize = ['Annual Income (k$)', 'Spending Score (1-100)']
        self.df[columns_to_standardize] = scaler.fit_transform(self.df[columns_to_standardize])

    def x_normalized   (self) :
        scaler = MinMaxScaler()
        columns_to_standardize = ['Annual Income (k$)', 'Spending Score (1-100)']
        self.df[columns_to_standardize] = scaler.fit_transform(self.df[columns_to_standardize])

    def transform (self) : 
        self.del_ID()
        # self.replace_Gender()
        # self.x_standardized ()

        # self.x_normalized ()
        return self.df
