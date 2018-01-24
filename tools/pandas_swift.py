import pandas as pd

# ref: https://stackoverflow.com/a/41709869/3302757
# https://github.com/pandas-dev/pandas/issues/9229
def pd_mutate(df,target_col,partition_cols,order_by_cols):

 return df.join(df.groupby(partition_cols)[target_col].first(), on = partition_cols,rsuffix="first_")
