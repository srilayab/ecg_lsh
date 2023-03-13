import pandas as pd
import numpy as np
import wfdb
import ast

#taken from: https://physionet.org/content/ptb-xl/1.0.3/

def load_raw_data(df, sampling_rate, path):
    if sampling_rate == 100:
        data = [wfdb.rdsamp(path + "/" + f) for f in df.filename_lr]
    else:
        data = [wfdb.rdsamp(path + "/" + f) for f in df.filename_hr]
    data = np.array([signal for signal, meta in data])
    return data

path = 'ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3'
sampling_rate=100

# load and convert annotation data
Y = pd.read_csv(path + '/ptbxl_database.csv', index_col='ecg_id')
np.save("loaded_data/Y.npy", Y)
print("Y")
Y.scp_codes = Y.scp_codes.apply(lambda x: ast.literal_eval(x))
np.save("loaded_data/Y_scp_codes.npy", Y.scp_codes)
print("Y.scp_code")
# Load raw signal data
X = load_raw_data(Y, sampling_rate, path)
np.save("loaded_data/X.npy", X)
print("X")

# Load scp_statements.csv for diagnostic aggregation
agg_df = pd.read_csv(path + '/scp_statements.csv', index_col=0)
agg_df = agg_df[agg_df.diagnostic == 1]
np.save("loaded_data/agg_df.npy", agg_df)
print("agg_df")

def aggregate_diagnostic(y_dic):
    tmp = []
    for key in y_dic.keys():
        if key in agg_df.index:
            tmp.append(agg_df.loc[key].diagnostic_class)
    return list(set(tmp))

# Apply diagnostic superclass
Y['diagnostic_superclass'] = Y.scp_codes.apply(aggregate_diagnostic)
np.save("loaded_data/Y_diagnostic_superclass.npy", Y['diagnostic_superclass'])
print("Y2")

# Split data into train and test
test_fold = 10
# Train
X_train = X[np.where(Y.strat_fold != test_fold)]
np.save("loaded_data/X_train.npy", X_train)
print("X_train")
y_train = Y[(Y.strat_fold != test_fold)].diagnostic_superclass
np.save("loaded_data/y_train.npy", y_train)
print("y_train")
# Test
X_test = X[np.where(Y.strat_fold == test_fold)]
np.save("loaded_data/X_test.npy", X_test)
print("X_test")
y_test = Y[Y.strat_fold == test_fold].diagnostic_superclass
np.save("loaded_data/y_test.npy", y_test)
print("y_test")
