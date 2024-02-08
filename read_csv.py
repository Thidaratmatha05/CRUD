import pandas as pd
file_path = 'หนองคาย.csv'
df = pd.read_csv(file_path, header=None)
print(df) 