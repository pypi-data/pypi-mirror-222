import pandas as pd
import numpy as np
from sklearn.experimental import enable_hist_gradient_boosting 
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import plotly.graph_objects as go
import os
from joblib import load,dump


def runMissing(data):
    filename = 'missingVals.model'

    class MissingValModel(object):
        def __init__(self, raw_data_stream):
            df = raw_data_stream 

            self.data = df

        # enter data as pandas dataframe
        def fill_dataframe(self,data):
            def clean_columns(df, data_types, substrings):
                columns_to_remove = []

                for column in df.columns:
                    if (df[column].dtype not in data_types) or (any(substring in column for substring in substrings)):
                        columns_to_remove.append(column)

                df = df.drop(columns=columns_to_remove)

                nan_percentages = df.isna().mean()
                columns_to_remove = nan_percentages[nan_percentages > .2].index
                df=df.drop(columns=columns_to_remove, axis=1)
                df.drop(df.index[-1], inplace=True)
                return df


            df=clean_columns(data,['int', 'float64'],['Id','Return'])

            def impute_missing_values(df, target_column):
                target = df[target_column]

                data_with_target = df[~target.isnull()]
                data_to_impute = df[target.isnull()]

                feature_columns = df.columns.drop(target_column)

                if data_to_impute.empty:
                    print(f"No missing values in column '{target_column}'. Skipping imputation.")
                    return df


                X = data_with_target[feature_columns]
                y = data_with_target[target_column]



                model = HistGradientBoostingRegressor()


                model.fit(X, y)


                imputed_values = model.predict(data_to_impute[feature_columns])


                df.loc[target.isnull(), target_column] = imputed_values


                return df

            def iterate_lse(fill):
                for column in fill.columns:
                    fill = impute_missing_values(fill, column)
                return fill

            df = iterate_lse(df)
            return df

    missing_val_model = MissingValModel(data)
    filled_df = missing_val_model.fill_dataframe(missing_val_model.data)
    dump(filled_df, filename)
    return filled_df
