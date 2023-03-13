# ecg_lsh

### Locality Sensitive Hashing (LSH) for Electrocardiogram (ECG) signals

This repo contains code for finding the k nearest neighbors of an ECG signal using locality sensitive hashing.
Data is taken from the PTB-XL dataset (https://physionet.org/content/ptb-xl/1.0.3/).  

#### Motivation
Finding the nearest neighbors of an ECG signal can aid in diagnostics and classification. 
Generally, medical signals can be quite large and finding exact distances can be time-consuming and inefficient.  
LSH can be an alternative to finding nearest neighbors more quickly.
