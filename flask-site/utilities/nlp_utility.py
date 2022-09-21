
#from __future__ import division
from itertools import chain
from utilities import data_basic_utility as databasic

import nltk

################################
### START: NLP Helper Functions
################################

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


def text_corpus_stats(tokenisedReasons):
    # we put all the tokens in the corpus in a single list
    words = list(chain.from_iterable(tokenisedReasons))

    # convert list of words/tokens to a set, i.e. giving a set of unique words 
    vocab = set(words) 
    lexical_diversity = len(vocab)/len(words)

    # print stats for the words and vocabulary
    print( "Vocabulary size: ",                      len(vocab) )
    print( "Total number of tokens: ",               len(words) )
    print( "Lexical diversity: ",                    lexical_diversity)
    print( "Total number of reasons:",               len(tokenisedReasons) )
    lens =                                           [ len(reason) for reason in tokenisedReasons ]

    # print stats for the document lengths
    print( "Average document length:",               np.mean(lens) )
    print( "Maximum document length:",               np.max(lens) )
    print( "Minimum document length:",               np.min(lens) )
    print( "Standard deviation of document length:", np.std(lens) )


def print_token_stats(lstInputs, allWords, vocabulary):
    lexical_diversity = len(vocabulary)/len(allWords)
    lens = [len(token_list) for token_list in lstInputs]
    
    print("Statistics for List of Text Inputs:")
    print("  Total number of tokens: ", len(allWords))
    print("  Vocabulary size: ",len(vocabulary))
    print("  Lexical diversity: ", lexical_diversity)
    print("  Total number of lists:", len(lstInputs))
    print("  Average description tokens length:", np.mean(lens))
    print("  Minimum description tokens length:", np.min(lens))
    print("  Maximum description tokens length:", np.max(lens))
    print("  Standard deviation of document length:", np.std(lens))
    

################################
### END: NLP Helper Functions
################################


################################
### Start: POS Tagging Helper Functions
################################

# For a given text block for POS Tags for each word in User Comments
def createPosTagsForText(textValue):
    textValue = databasic.ensureIsString(textValue)        
    wordTokens = databasic.wordTokeniseSingleParagraph(textValue)

    # position tagging 
    return nltk.pos_tag(wordTokens)


# For a dataframe, create a new column containing all the words and POS Tags for a given input text column
def createPosTagsColForDataFrame(dfInput, sourceCol, posTagCol):
    dfInput[posTagCol] = dfInput.apply(lambda x: createPosTagsForText(x[sourceCol]), axis=1)
    return dfInput
