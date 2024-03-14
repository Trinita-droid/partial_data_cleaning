# organising CSV dataset as a df table using the pandas read_csv() method. read_csv() can read the txt files as well
import pandas as pd
file_loc2 = "C:/Users/TJO1COB/Downloads/Lending-company.csv"
to_csv = pd.read_csv(file_loc2)
print(to_csv)
print(type(to_csv))

# setting index columns (based on 0-indexing for other params start from 1st row); header param takes the given number and assigns it as the col names to rest of data then the rows after that are displayed under,skip rows will skip the rows for the number given.
ind_cols = pd.read_csv(file_loc2,index_col=3,skipfooter=2,header=4,skiprows=1)
print("ind_cols : \n", ind_cols)