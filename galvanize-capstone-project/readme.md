
# galvanize-dsi-capstone
https://github.com/krishnatray/galvanize-dsi-capstone

## DocReach: Predicting physician specialty from text data

## Sushil K Sharma
---
## Overview
A large social media marketing firm wants to target doctors / physicians based on their practice area. For example, A marketing campaign to target Cardiologists for heart related news feed.

## Scope
The marketing firm wants to predict physicians under medical specialties based upon procedures performed over the past year

- Phase 1: Develop a binary classifier to predict Cardiologists
- Phase 2: Develop a multiclass classifier to predict top 5 Specialties

## Motivation


## Dataset
Data has been provided in the form of csv files:
> **procedures.csv** - contains a list of procedures doctors performed over the past year. The columns of this dataset are as follows:
physician_id unique physician identifier, joins to id in physicians.csv
procedure_code unique code representing a procedure
procedure description of the procedure performed (Text Column)
number_of_patients the number of patients the doctor performed that procedure on over the past year

> **physicians.csv** - contains a list of doctors and their unique specialty. Specialty is listed as "Unknown" for the doctors need to be classified.
physician_id unique physician identifier, joins to id in physicians.csv
Specialty: String e.g. Cardiologist

## Process
- Data Acquisition
- EDA
- Data Prep
- Model Selection
- Results

## Results
  Best model:             RandomForestClassifier
  Best threshold:         0.04
  Resulting profit:        $45.94
  Proportion positives:   0.80
               precision    recall  f1-score   support
  	False       0.74      0.85      0.79      1272
         True       0.82      0.68      0.75      1228
  avg / total       0.78      0.77      0.77      2500

Accuracy Score Train: 0.789
Accuracy Score Test: 0.7708

## Next Steps
TBD
