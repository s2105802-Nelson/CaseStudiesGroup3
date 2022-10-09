import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# from __future__ import division
# from itertools import chain


################################
### START: Basic Stats and Data Explore Helper Functions
################################

### Works for a Series (dataframe column), not testing with a list or np array yet
def print_stats_and_outliers(variableData, variableName, variableNiceName, showPlots=True):
  variableRecordCount = len(variableData)
  variableMin = np.min(variableData)
  variableMax = np.max(variableData)
  variableMissing = variableData.isnull().sum()
  variableMean = np.mean(variableData)
  variableMedian = np.median(variableData)
  variableSD = np.std(variableData)
  variableQ1 = np.nanquantile(variableData, 0.25)
  variableQ3 = np.nanquantile(variableData, .75)
  variableIQR = variableQ3 - variableQ1
  variableLowerFence = variableQ1 - (1.5 * variableIQR)
  variableUpperFence = variableQ3 + (1.5 * variableIQR)  
    
  variableZeros = len(variableData[variableData == 0])
  variableLowerOutliers = len(variableData[variableData < variableLowerFence])
  variableUpperOutliers = len(variableData[variableData > variableUpperFence])

  print("Basic Summary Statistics of " + variableNiceName + " - " + variableName + ":")
  print("  Records: " + str(variableRecordCount))
  print("  Null Records: " + str(variableMissing) + "   Zero Records: " + str(variableZeros))
  print("  Min: " + str(variableMin) + "   Max: " + str(variableMax))
  print("  Mean: " + str(variableMean) + "   Median: " + str(variableMedian))
  print("  Standard Deviation:" + str(variableSD))
  print("Quantile Statistics:")
  print("  Q1: " + str(variableQ1) + "   Q3: " + str(variableQ3) + "   IQR: " + str(variableIQR))
  print("  Lower Fence: " + str(variableLowerFence) + "   Upper Fence: " + str(variableUpperFence))
  print("Outlier Counts:")
  print("  Lower Outliers: " + str(variableLowerOutliers) + "   Upper Outliers: " + str(variableUpperOutliers))  
  print("  Total Outliers: " + str(variableLowerOutliers + variableUpperOutliers))

  if showPlots:
    # look at a histogram and a boxplot of this data, to view distribution and look for possible outliers    
    variableData.plot(kind='hist',bins=20)
    plt.title(variableNiceName + " Histogram")
    plt.xlabel(variableNiceName)    

    fig2, ax2 = plt.subplots()
    ax2.set_title(variableNiceName + " Boxplot")
    plt.boxplot(variableData, labels=[variableNiceName])
    plt.show()

    # Do another histogram of the data, filtering out zeroes
    variableData[variableData > 0].plot(kind='hist',bins=20)
    plt.title(variableNiceName + " Histogram No Zeroes")
    plt.xlabel(variableNiceName)
    plt.show()

  # print(paste("Number of Detected Outliers: ", length(bp$out), sep=" "))  


# Calculate upper and lower fence, then null out entries in the column according to those fences
def auto_rm_outliers(dataframe, column_name):  
  dfCopy = dataframe.copy()
  
  variableQ1 = np.nanquantile(dfCopy[column_name], 0.25)
  variableQ3 = np.nanquantile(dfCopy[column_name], .75)
  variableIQR = variableQ3 - variableQ1
  variableLowerFence = variableQ1 - (1.5 * variableIQR)
  variableUpperFence = variableQ3 + (1.5 * variableIQR)  

  dfCopy[column_name] = dfCopy[column_name].apply(lambda x: np.NaN if x > variableUpperFence or x < variableLowerFence else x)
  return dfCopy


def null_out_zeros(dataframe, column_name):  
  dfCopy = dataframe.copy()  
  dfCopy[column_name] = dfCopy[column_name].apply(lambda x: np.NaN if x == 0 else x)
  return dfCopy

      
################################
### END: Basic Statisitcs Helper Functions
################################


################################
### START: Confusion Matrix Helpers
################################

# Returns a string report on a confusion matrix, only for a binary categorisation (i.e. a 2x2 matrix)
# pass in a result from a confusion_matrix() 
def confusionMatrixBinaryReport(cm, showFullStats=False):
  cmReport = "Confusion Matrix:\n"
  cmReport += str(cm) + "\n\n"

  tp = cm[0, 0]
  tn = cm[1, 1]
  fp = cm[1, 0]
  fn = cm[0, 1]
  total = tp + tn + fp + fn

  cmReport += "  Total Records: " + str(total) + "\n"
  cmReport += "  Correct Predictions: " + str(tp + tn) + "\n"
  cmReport += "  Incorrect Predictions: " + str(fp + fn) + "\n"  
  cmReport += "  Accuracy Rate (Proportion of Correct predictions): " + str((tp + tn) / total) + "\n\n"

  precision = tp / (tp + fp)
  recall = tp / (tp + fn)
  cmReport += "  Precision (When predicting Positive, how many were actually Positive): " + str(precision) + "\n"  
  cmReport += "  Recall/Sensitivity (How many predicted Positive were actually Positive): " + str(recall) + "\n"

  if showFullStats:
    cmReport += "\n  Negative Predictive Value (When predicting Negative, how many were actually Negative): " + str(tn / (tn + fn)) + "\n"
    cmReport += "  Specificity (How many predicted Negative were actually Negative): " + str(tn / (tn + fp)) + "\n"
    cmReport += "  F1-Score ( F = 2 * ([Precision * Recall] / [Precision + Recall]) ): " + str(2 * ( (precision*recall) / (precision+recall))) + "\n"

  return cmReport


################################
### END: Confusion Matrix Helpers
################################


################################
### START: Data Transformation Helpers
################################


def doLog10Transform(val):
  if np.isnan(val):
    return np.NaN
  elif val == 0:
    return 0    
  else:
    return np.log10(val)


def log10TransformDfCol(df, colName):
  df[colName] = df.apply(lambda x: doLog10Transform(x[colName]), axis=1)
  return df


def scaleStandardSingle(dataframeCol):
  scaler = StandardScaler()
  dataframeCol = scaler.fit_transform(dataframeCol)
  return dataframeCol


def scaleMinMaxSingle(dataframeCol):
  scaler = MinMaxScaler()
  dataframeCol = scaler.fit_transform(dataframeCol)
  return dataframeCol


def scaleStandardMultiple(df, feature_cols):
  scaler = StandardScaler()
  dfScaled = scaler.fit_transform(df[feature_cols])
  return dfScaled    
      

def scaleMinMaxMultiple(df, feature_cols):
  scaler = MinMaxScaler()
  dfScaled = scaler.fit_transform(df[feature_cols])
  return dfScaled    
      
      
################################
### END: Data Transformation Helpers
################################


################################
### START: NDCG For Ranking Helper Functions
################################


def dcg_at_k(r, k):
    r = np.asfarray(r)[:k]
    if r.size:
        #print(f"dcg_at_k {str(r.size)}")
        return np.sum(np.subtract(np.power(2, r), 1) / np.log2(np.arange(2, r.size + 2)))
    return 0


def ndcg_at_k(r, k):
    idcg = dcg_at_k(sorted(r, reverse=True), k)
    #print(f"ndcg_at_k {str(idcg)}")
    if not idcg:
        return 1         

    #rint(f"ndcg_at_k returning {str(dcg_at_k(r, k))} / {str(idcg)} = {str(dcg_at_k(r, k) / idcg)}")
    return dcg_at_k(r, k) / idcg


def ndcg_for_dataset(df, k=10):  
  relevances = df.groupby("Query ID")
  ndcg = relevances.apply(lambda x: ndcg_at_k(x["Label"], k)).mean()
  return ndcg

################################
### END: NDCG For Ranking Helper Functions
################################

