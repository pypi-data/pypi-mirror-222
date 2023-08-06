import pandas as pd
import numpy as np
from sklearn.experimental import enable_hist_gradient_boosting 
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import plotly.graph_objects as go
import os
from joblib import load, dump


def runRegen(data):
    filename = 'regenDataFame.model'

    class RegenModel(object):
        def __init__(self, raw_data_stream):
            # Parse DataFrame from raw data stream
            self.df = raw_data_stream

            # Assuming 'filename' is defined or obtained from elsewhere
            self.model_file = os.environ.get('MODEL_FILE', filename)
        # enter data as pandas dataframe
        def regen_dataframe(self,data):
            def impute_missing_values_Thesus(df_train, target_column,df_fill):
                target = df_fill[target_column]
                targetpred = df_train[target_column]
                merged_df = targetpred.copy()

                data_with_target = df_train[~merged_df.isnull()]
                data_to_impute = df_train[merged_df.isnull()]
                feature_columns = df_train.columns.drop(target_column)

                if data_to_impute.empty:
                    return df_fill

                X = data_with_target[feature_columns]
                y = data_with_target[target_column]

                model = HistGradientBoostingRegressor()
                model.fit(X, y)
                dump(model, open(self.model_file, 'wb'))

                imputed_values = model.predict(data_to_impute[feature_columns])
                df_fill.loc[target.isnull(), target_column] = imputed_values

                return df_fill

            def iterate_lse_Thesus(df_train,df_fill):
                for column in df_fill.columns:
                    df_fill = impute_missing_values_Thesus(df_train, column,df_fill)
                return df_fill
            
            def Theseus_nan(df, percentage, marked):
                num_rows, num_cols = df.shape
                nan_count = int(num_rows * percentage / 100)

                for column in df.columns:
                    available_indices = np.where(marked[column] == np.inf)[0]
                    if len(available_indices) < nan_count:
                        continue

                    random_indices = np.random.choice(available_indices, nan_count, replace=False)
                    marked.iloc[random_indices, df.columns.get_loc(column)] = np.nan

                return marked   

            def Thesus(df):
                percentage=5
                columns = df.columns
                index = df.index
                marked = pd.DataFrame(np.inf, index=index, columns=columns)

                iteration=int(100/percentage)

                for i in range(iteration):
                    if (iteration-1)==i:
                        marked = marked.replace(np.inf, np.nan) # edge case of catching all unchanged values for final instance
                    marked = Theseus_nan(df, percentage, marked)
                    marked = iterate_lse_Thesus(df,marked)

                return df      
            
            gen_df=Thesus(data)
            return gen_df
    def clean_columns(df, data_types):
        columns_to_remove = []
        for column in df.columns:
            if (df[column].dtype not in data_types):
                columns_to_remove.append(column)
        df = df.drop(columns=columns_to_remove)
        nan_percentages = df.isna().mean()
        columns_to_remove = nan_percentages[nan_percentages > .2].index
        df=df.drop(columns_to_remove, axis=1)
        df.drop(df.index[-1], inplace=True)
        return df
    regen_model = RegenModel(data)
    data = clean_columns(data, [np.number])
    return regen_model.regen_dataframe(data)
