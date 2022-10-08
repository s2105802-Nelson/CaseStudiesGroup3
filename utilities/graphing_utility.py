import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def graphBasicSingleLine(dfInput, xCol, yCol, title, xLabel, ylabel, useMarkers=False):
    plt.title(title)
    xaxis = dfInput[xCol]
    yaxis = dfInput[yCol]

    plt.xlabel(xLabel)
    plt.ylabel(ylabel)
    marker = ''
    if useMarkers:
        marker = '.'

    pltOutput = plt.plot(xaxis, yaxis, marker=marker)
    return pltOutput 


def graphBasicTwoSeries(dfInput, xCol, series1Col, series2Col, title, xLabel, series1Label, series2Label, useMarkers=False):
    plt.title(title)
    xaxis = dfInput[xCol]
    series1 = dfInput[series1Col]
    series2 = dfInput[series2Col]

    plt.xlabel(xLabel)
    marker1 = ''
    marker2 = ''
    if useMarkers:
        marker1 = '.'
        marker2 = 'x'

    plt.plot(xaxis, series1, c='#0000FF', marker=marker1, markersize=8, label=series1Label) 
    plt.plot(xaxis, series2, c='#00FF00', marker=marker2, markersize=8, label=series2Label) 
    return plt 


# Do a basic Group By Count on the dataframe then return a basic matplotlib bar plot (which you can do a plt.show() on)
def graphBasicBarDistribution(dfInput, categoricalCol):
    # Do a Group By Count on the categorical values
    dfGroupByCount = dfInput.groupby(categoricalCol).agg(ResultCount = (categoricalCol, 'size')).sort_values(categoricalCol, ascending = True)
    dfGroupByCount = dfGroupByCount.reset_index(level=0)

    # Create the distribution plot as a bar plot
    plt.title(categoricalCol + " - Count of Values")
    plt.bar(dfGroupByCount[categoricalCol], dfGroupByCount["ResultCount"], label='ResultCount')
    plt.legend()
    return plt


# For a Text column: Visualise how many records have text, are empty strings, or are NA
def graphBasicEmptyTextDistribution(dfInput, textCol):
    countNA = dfInput[dfInput[textCol].isna()].shape[0]
    countEmpty = dfInput[dfInput[textCol].str.strip() == ""].shape[0]
    countHasText = dfInput[dfInput[textCol].str.strip() != ""].shape[0]

    dfTextData = [ ["Is NA", countNA], ["No Text", countEmpty], ["Has Text", countHasText] ]
    dfTextCounts = pd.DataFrame(data = dfTextData, columns=["TextStatus", "Count"])
    
    plt.title(textCol + " - Count by Text Status")
    bars = plt.bar(dfTextCounts["TextStatus"], dfTextCounts["Count"], label='Count')
    plt.bar_label(bars)
    return plt    


# For a general data column: Visualise how many records are NA or not
def graphBasicNADistribution(dfInput, targetCol):
    countNA = dfInput[dfInput[targetCol].isna()].shape[0]
    countNotNA = dfInput[dfInput[targetCol].notna()].shape[0]

    dfData = [ ["Is NA", countNA], ["Not NA", countNotNA] ]
    dfNACounts = pd.DataFrame(data = dfData, columns=["NA Status", "Count"])
    
    plt.title(targetCol + " - Count by Text Status")
    bars = plt.bar(dfNACounts["NA Status"], dfNACounts["Count"], label='Count')
    plt.bar_label(bars)
    return plt        


def graphBasicConditionDistribution(dfInput, mskCondition, conditionTitle=""):
    countYes = dfInput[mskCondition].shape[0]
    countNo = dfInput[~mskCondition].shape[0]

    dfData = [ ["Yes", countYes], ["No", countNo] ]
    dfNACounts = pd.DataFrame(data = dfData, columns=["Result", "Count"])
    
    if conditionTitle != "":
        plt.title(conditionTitle)

    bars = plt.bar(dfNACounts["Result"], dfNACounts["Count"], label='Count')
    plt.bar_label(bars)
    return plt            


def wordCloudForTextColumn(dfInput, textColumn, maxWords=5000, imgWidth=1000, imgHeight=600):
    # Clean out empties
    dfForWordCloud = dfInput[dfInput[textColumn].str.strip() != ""]
    dfForWordCloud = dfForWordCloud[dfForWordCloud[textColumn].notna()]

    lstText = list(dfForWordCloud[textColumn])

    # Join all the texts together.
    long_string = ','.join(lstText)
    # Create a WordCloud object
    wordcloud = WordCloud(background_color="white", max_words=maxWords, contour_width=3, contour_color='steelblue', width=imgWidth, height=imgHeight)
    # Generate a word cloud
    wordcloud.generate(long_string)
    # Visualize the word cloud
    return wordcloud.to_image()

    
################################
### START: Learning Curve for ML Evaluation Helpers
################################

# Set your proportion of the train/test split. If you're doing 5x k folds, this will therefore be 20%
# this means that the splits will be at 20% intervals of the size
def getTrainSizesForLearningCurve(dfInput, testSize=0.2, propSplitsOnTrainSize = 0.2):
  if dfInput is None:
    return []  

  dfLen = dfInput.shape[0]
  if dfLen == 1:
    return [ 1 ]
  elif dfLen == 2:
    return [ 1, 2 ]
    
  # Initialize the list of sizes, always start with 1 record
  train_sizes = [ 1 ]
  maxTrainRecords = dfLen * (1-testSize)

  propStepper = propSplitsOnTrainSize
  while propStepper < 1:
      train_sizes.append(int(maxTrainRecords * propStepper))
      propStepper = propStepper + propSplitsOnTrainSize      

  # append the max number of records
  train_sizes.append(int(maxTrainRecords))
  
  return train_sizes


def graphLearningCurve(train_sizes, train_errors_mean, validation_errors_mean):
    # Use the max error from the splits as the limit of the Y Axis
    maxY = validation_errors_mean.max()
    if train_errors_mean.max() > maxY:
        # This shouldn't happen 
        maxY = train_errors_mean.max() 

    plt.style.use('seaborn')
    plt.plot(train_sizes, train_errors_mean, label = 'Training error')
    plt.plot(train_sizes, validation_errors_mean, label = 'Validation error')
    plt.ylabel('MSE', fontsize = 14)
    plt.xlabel('Training set size', fontsize = 14)
    plt.title('Learning curves for a regression model', fontsize = 18, y = 1.03)
    plt.legend()
    plt.ylim(0,maxY)
    return plt
    
################################
### END: Learning Curve for ML Evaluation Helpers
################################