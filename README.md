# RMIT Case Studies Group 3 

## Predicting Foot Traffic Numbers from Weather and other Social Data in the City of Melbourne

Every customer-serving, bricks-and-mortar business faces the challenge of stock management and resource utilisation. Bigfoot looks to help with these problems by giving indications of active population in the City of Melbourne via foot traffic number predictions. 

This repository contains Python Notebooks on the data analysis and research for the modelling of Foot Traffic Number predictions in the City of Melbourne. The following is some brief information on the contents of this repository and where to find the most relevant code for the modelling.

### Project Information

For full explanation of the purpose of this project and the modelling, a full version of the related Project Report, **CaseStudiesGroup3.FinalReport.pdf** is included in the root of the repository.

### Aim of the Project Modelling

In brief, two models were built for two different problems, which were:

1) To predict the aggregated City of Melbourne foot traffic predictions, and 
2) To predict foot traffic numbers at specific street locations within the CBD.

In order to do this, data spanning from January 2013 to July 2022 was sourced then used for the modelling.

### Data

For modelling of Foot Traffic numbers, a number of separate data sources were found and used. For a full explanation of the data sourced and the original locations of the data, see the Data section of **CaseStudiesGroup3.FinalReport.pdf**.

The source data files, along with other data files downloaded and analysed, are all stored in the **/data_files_raw/** directory. As such, not all files in this directory were used.

In order to clean and transform data files into single unified datasets that could easily be used in machine learning for the two models.

*For the aggregated Melbourne modelling*
See/run the notebook file **08.CreateFootTrafficDataLarge.ipynb**. This file takes the relevant source data files from with /data_files_raw/, does the appropriate cleaning and transformations, then merges the data all together and writes it out to the most up to date full data file. Find this file at **/data_files/FootTrafficWeatherMelb3_20130101_20220701.csv**

*For the street specific locations modelling*
See/run the notebook file **10.CreateFootTrafficByStreet.ipynb**. This file takes the relevant source data files from with /data_files_raw/, does the appropriate cleaning and transformations, then merges the data all together and writes it out to the most up to date full data file. Find this file at **/data_files/FT_Street_Melb_20130101_20220701.csv**

### Best performing models

Azure models are generated using the Microsoft Azure platform. The models generated have been exported from the platform and saved into the **/azure-models/** folder.

*For aggregated Melbourne modelling, the best performing models were:*
First was the Azure Automated Time Series Forecasting, Second Best was XGBoost Regression. For the Azure model, find it in **/azure-models/All_TimeSeriesForecast_Model_AutoMLfe937bc6c40.zip**. For the XGBoost Regression experiment, See/run the notebook file **09b.RegressionXGBoostV3.ipynb**.

*For specific street location modelling, the best performing models were:* 
First was XGBoost Regression, Second Best was the Azure Automated Regression. For the XGBoost Regression experiment, See/run the notebook file **11a.StreetXGboostV1.ipynb**. For the Azure model, find it in **/azure-models/Streets_Regression_Model_AutoML760872fe140.zip**.

### Research, Exploratory Data Analysis and other files

During the course of the project, a number of other Jupyter Notebooks were created for different experiments, and they should all be viewable and accessible in the root directory for review. These include modelling experiments with ARIMA (/ARIMA.ipynb) and Scikit-learn Lasso and Ridge (/LASSO_RIDGE_REGRESSION.ipynb). 






