# train.csv, test.csv
import pandas as pd
pd.set_option('display.max_columns', 15)

train_df = pd.read_csv('data/train.csv')
test_df = pd.read_csv('data/test.csv')

df = pd.concat([train_df, test_df])

# 결측치 확인
df.describe()
df.info()

df.isnull().sum(axis = 0)
df['Pclass'].value_counts(dropna = False)

class data_null:
    def __init__(self, dataframe):
        self.df = dataframe

    def count_null(self):
        return self.df.isnull().sum(axis = 0)

    def column_count(self, col):
        return self.df[col].value_counts(dropna = False)


df_analysis = data_null(df)

df_analysis.count_null()
df_analysis.column_count('Survived')

