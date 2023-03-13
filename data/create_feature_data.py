import numpy as np
from biosppy.signals import ecg
import sys
np.set_printoptions(threshold=sys.maxsize)

#R - I
#Q - I
#P - II
X_single_lead_loaded = np.load("X_single_lead.npy", allow_pickle=True)
X_second_lead_loaded = np.load("X_second_lead.npy", allow_pickle=True)
X_test = np.load("loaded_data/X_test.npy", allow_pickle=True)

X_feature_data = []

X_single_lead_loaded = X_test[:, :, 0]
X_second_lead_loaded = X_test[:, :, 1]

for i in range(1):
    features = []
    single_lead = X_single_lead_loaded[i].tolist()
    second_lead = X_second_lead_loaded[i].tolist()

    #R peaks
    R_peaks_indices = ecg.ASI_segmenter(single_lead, sampling_rate=100.0)[0]
    R_peaks = [0 for j in range(1000)] #np.zeros((1, 1000))
    for r in R_peaks_indices:
        R_peaks[r] = 1

    features.append(R_peaks)

    #Q peaks
    ecg_proc = ecg.ecg(single_lead, sampling_rate=100.0, show=True)
    if (ecg_proc == None):
        continue
    ts, filtered, rpeaks, templates_ts, templates, heart_rate_ts, heart_rate = ecg_proc

    Q_indices, Q_start_indices = ecg.getQPositions(ecg_proc)
    Q_start_positions = [0 for j in range(1000)] #np.zeros((1, 1000))
    for q in Q_start_indices:
        Q_start_positions[q] = 1
    # Q_start_positions[Q_start_indices] = 1

    features.append(Q_start_positions)

    #P peaks
    P_indices, P_start_indices, P_end_indices = ecg.getPPositions(ecg_proc)
    P_start_positions = [0 for j in range(1000)] #np.zeros((1, 1000))
    for p in P_start_indices:
        P_start_positions[p] = 1
    # P_start_positions[P_start_indices] = 1

    P_end_positions = [0 for j in range(1000)] #np.zeros((1, 1000))
    for p in P_end_indices:
        P_end_positions[p] = 1
    # P_end_positions[P_end_indices] = 1

    features.append(P_start_positions)
    features.append(P_end_positions)

    features = np.array(features)

    X_feature_data.append(features)


# np.save("X_feature_data.npy", X_feature_data)
X_feature_data_loaded = np.load("X_feature_data.npy", allow_pickle=True)
print(X_feature_data_loaded[0])
print(X_feature_data_loaded.shape)

Y_test = np.load("loaded_data/Y_test.npy", allow_pickle=True)
print(Y_test.shape)
print(Y_test)




