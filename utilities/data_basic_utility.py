from datetime import datetime
from dateutil.relativedelta import relativedelta
import regex as re
from itertools import chain
import os
import pathlib as Path

def get_random_seed(additional_randomizer=0):
  return datetime.now().year + datetime.now().month + datetime.now().day + \
    datetime.now().hour  + datetime.now().minute  + datetime.now().second  + datetime.now().microsecond  
  

###########################
### File helpers
###########################
def ensureFolderPath(folderPath):
  # Make sure the path ends with a '/'
  if folderPath.endswith("/") == False & folderPath.endswith("\\") == False:
    folderPath += "/"
  # Create the folder, if it doesn't already exist
  if not os.path.exists(folderPath):
    Path(folderPath).mkdir(parents=True,exist_ok=True)     


# This appears to be a pretty basic, fast version of mass file load from folder
def basicFileLoadToList(targetFolder, targetFileExt="txt"):
  files = Path.Path(targetFolder).glob('*.' + targetFileExt)
  fileData = []  
  for file in files:
    with file.open() as f:
      fileData.append(f.read())  
  return fileData


###########################
### List, String and other data structure helpers (not Dataframes, that's in dataframe_utility.py)
###########################
def listOfStringsPeek(listStrings, head=5, maxChars=250):
  if listStrings == None:
    print("List is null.")
  elif len(listStrings) == 0:
    print("List is empty.")
  else:
    # Peek at some of the data
    for i in range(head):
      if listStrings[i] == None:
        print(str(i) + ": [NULL]")
      else:
        substringLen = len(listStrings[i])
        if (substringLen > maxChars):
          substringLen = maxChars  
        print(str(i) + ": [" + str(listStrings[i][0 : substringLen]) + "]")


def listHead(listStrings, head=5):
  listOfStringsPeek(listStrings, head, 1024)        


# Given a list of numbers, compile the list into a strong. Optionally print the string
def numArrayToString(numArray, sep=" ", print=False):
  strOutput = ""
  for entry in numArray:
    if strOutput != "":
      strOutput += sep
    strOutput += str(entry)
  if print==True:
    print("Array: " + strOutput)    
  return strOutput  


def padStringToLength(input, padChar, length):
    if len(input) < length:
        for i in range(len(input), length):
            input = padChar + input

    return input
      


###########################
### Binary Word Search functions
###########################
def bsearch_string (target_word, word_list_sorted):
  return bsearch_string_recurse(target_word, word_list_sorted, 0, len(word_list_sorted)-1)


def bsearch_string_recurse (target_word, word_list_sorted, start, end):
  # check condition
  if end < start:
    # Element is not found in the array
    return -1    
  else:
    # retrieve the middle of the set, this is the item we're going to examine    
    mid = start + (end - start)//2
    if word_list_sorted[mid] == target_word:
      # Found, return the index of the item
      return mid
    elif word_list_sorted[mid] > target_word:      
      # Not found, Continue searching the next lower section
      return bsearch_string_recurse(target_word, word_list_sorted, start, mid-1)    
    else:
      # Not found, Continue searching the next upper section
      return bsearch_string_recurse(target_word, word_list_sorted, mid+1, end)


# Given a list of word tokens, and a sorted word list, it loops through all the tokens and filters that token out
# if that word isn't in the sorted word list, using the binary search method
def filter_by_words_bsearch(word_tokens, word_list_sorted):  
  filtered_tokens = list(filter(lambda x: bsearch_string(x, word_list_sorted) == -1, word_tokens))
  return filtered_tokens     

  
###########################
### NLP Helper functions
###########################
def createWordsAndVocabForTokenLists(lstTokens):
  words = list(chain.from_iterable(lstTokens)) # we put all the tokens across our dataset in a single list
  vocab = set(words) # compute the vocabulary by converting the list of words/tokens to a set, i.e., giving a set of unique words
  return (words, vocab)


class numKeyValuePair:
  # Properties
  key = None
  value = None

  # Constructor
  def __init__(self):
    key = None
    value = None

  def __init__(self, numKey, numValue):
    key = numKey
    value = numValue    



###########################
### Data Convert Utility Helper functions
###########################

def ensureIsString(input, autoTrim = True):
  if input is None:
    return ""
  elif isinstance(input, str) == False:
    input = str(input)

  if autoTrim:
    input = input.strip()

  return input      


def getStartOfMonth(inputDateStr, dateFormat="%d/%m/%Y"):
  if inputDateStr is None:
    inputDate = datetime.now
  else:
    inputDate = datetime.strptime(inputDateStr, format=dateFormat)
  return datetime(inputDate.year, inputDate.month, 1)   


def getEndOfMonth(inputDate=None):
  if inputDate is None:
    inputDate = datetime.now
  endOfMonth = datetime(inputDate.year, inputDate.month, 1) + relativedelta(months=1) - relativedelta(seconds=1)
  return endOfMonth

  
def getStartOfNextMonth(inputDate=None):
  if inputDate is None:
    inputDate = datetime.now
  return datetime(inputDate.year, inputDate.month, 1) + relativedelta(months=1)


def getEndOfLastMonth(inputDate=None):
  if inputDate is None:
    inputDate = datetime.now
  endOfMonth = datetime(inputDate.year, inputDate.month, 1) - relativedelta(seconds=1)
  return endOfMonth  


def getStartOfDay(inputDate=None):
  if inputDate is None:
    inputDate = datetime.now
  return datetime(inputDate.year, inputDate.month, inputDate.day, 0, 0, 0)   


def getEndOfDay(inputDate=None):
  if inputDate is None:
    inputDate = datetime.now
  return datetime(inputDate.year, inputDate.month, inputDate.day, 23, 59, 59)     