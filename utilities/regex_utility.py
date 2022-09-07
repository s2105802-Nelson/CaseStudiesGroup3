import re
# This utility has:
#    Start of the file: Constants for commonly used regular expressions
#    Regular Expression Helper functions
"""
START: Reusable regular expression constants
"""
def regex_Email():
  return "^([a-zA-Z0-9_\\-\\.']+)@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.)|(([a-zA-Z0-9\\-]+\\.)+))([a-zA-Z]{2,10}|[0-9]{1,3})(\\]?)$"

def regex_Time24Hr():
	return "^[0-9]{2}:[0-9]{2}$"

#  AU Mobile Phones always 10 digits, or + then 11 digits
def regex_MobilePhoneAU():
	return r"^([+][0-9]{2}[0-9]{9})|([0-9]{10}|([0-9]{4}[ ]{1}[0-9]{3}[ ]{1}[0-9]{3})|([+][0-9]{2}[0-9]{3}[ ]{1}[0-9]{3}[ ]{1}[0-9]{3}))$"

#  NZ Mobile Phones
def regex_MobilePhoneNZ():
	return r"^([+][0-9]{2}[0-9]{6,9})|([0-9]{8,11}|([0-9]{3}[ ]{1}[0-9]{3}[ ]{1}[0-9]{2-5})|([+][0-9]{3}[ ]{1}[0-9]{3}[ ]{1}[0-9]{2-5}))$"
    
def regex_FileNameCsv():
	return r"^.+\.[cC][sS][vV]$"
    
def regex_FileNameText():
	return r"^.+\.[tT][xX][tT]$"
    
def regex_FileNameExcelAny():
	return r"^.+\.[xX][lL][sS]([xX])?$"
    
def regex_FileNameXls():
	return r"^.+\.[xX][lL][sS]$"
    
def regex_FileNameXlsx():
	return r"^.+\.[xX][lL][sS][xX]$"
    
def regex_FileNamePdf():
	return r"^.+\.[pP][dD][fF]$"
    
def regex_FileNameDoc():
	return r"^.+\.[dD][oO][cC]([xX])?$"
    
def regex_FileNameImages():
	return r"^.+\.(([jJ][pP]([eE])?[gG])|([pP][nN][gG])|([gG][iI][fF])|([bB][mM][pP]))$"
    
def regex_FileNameDocuments():
	return r"^.+\.(([pP][dD][fF])?[gG])|[xX][lL][sS]([xX])?|[dD][oO][cC]([xX])?|([tT][xX][tT])$"

def regex_ContainsUpperCase():
	return "[A-Z]"

def regex_ContainsLowerCase():
	return "[a-z]"

def regex_ContainsNumeric():
	return "[0-9]"

def regex_ContainsNonWordChar():
	return "\\W"

def regex_PunctuationSymbol():
	return r"[\'\"\?\!\(\)\.\;\:]"  

def regex_StringWithoutPunctuation():
	return r'[^\w\s]' 

# These simple versions do not enforce limits on numbers for day or year (so 35th day or year 8726 are allowed). Later, will create Strict versions
def regex_DateSimpleNums():
    return r'^\d{1,2}(/|-)\d{1,2}(/|-)(\d{2}|\d{4})$'

def regex_DateSimpleYMD():
    return r'^\d{4}(/|-)\d{2}(/|-)\d{2}$'    

def regex_DateSimpleMonthWords():
    numFirstPattern = r'^\d{1,2}(st|nd|rd|th)?\s(of\s)?(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|january|febuary|march|april|june|july|august|september|october|november|december),?\s((\'?)\d{2}|\d{4})$'
    monthFirstPattern = r'^(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|january|febuary|march|april|june|july|august|september|october|november|december)\s(\d{1,2}(st|nd|rd|th)?,?\s)?((\'?)\d{2}|\d{4})$'
    return numFirstPattern + "|" + monthFirstPattern

def regex_DateSimpleFull():    
    return regex_DateSimpleNums() + "|" + regex_DateSimpleYMD() + "|" + regex_DateSimpleMonthWords()

def regex_DateDdMmYy():
    return r'^\d{1,2}(/|-)\d{1,2}(/|-)\d{2}$'
    
def regex_DateDdMmYyyy():
    return r'^\d{1,2}(/|-)\d{1,2}(/|-)\d{4}$'
    
def regex_DateDdMmmYy():
    return r'^\d{1,2}(/|-)[A-Za-z]{3}(/|-)\d{2}$'

def regex_DateDdMmmYyyy():
    return r'^\d{1,2}(/|-)[A-Za-z]{3}(/|-)\d{4}$'    

def regex_CurrencyOrPercent():
    return r'\$\d+(,\d+)?(\.\d{2})?$|^\d+(\.\d+)?\s?(\%|percent)'
    

"""
END: Reusable regular expression constants
"""

"""
START: Reusable Regular Expression functions
"""     

def re_is_match(pattern, input):
    return re.match(pattern, input)
    

def str_strip_punctuation(input):
  return re.sub(regex_StringWithoutPunctuation(), '', input)


def analyse_findall(pattern, stringToSearch):
    resultList = re.findall(pattern, stringToSearch)
    print("Regex: input [" + stringToSearch + "]")
    if len(resultList) > 0:        
        matchOutput = "  Match(es): "
        for result in resultList:
            if result:
                matchOutput = matchOutput + "['" + result + "']"               
            else:
                matchOutput = matchOutput + "[None]"
        print(matchOutput)        
    else:        
        print("  No matches.")

        
def analyse_findall_list(pattern, listOfStrings):
    for item in listOfStrings:
        analyse_findall(pattern, item)


def analyse_match(pattern, stringToSearch):
    result = re.match(pattern, stringToSearch)
    if result:
        print("Regex: match [" + stringToSearch + "]")        
        if (len(result.groups()) == 0):
            print("  No Groups found.")
        else:
            grpOutput = "  Groups "
            for grpStr in result.groups():
                if grpStr != None:
                    grpOutput = grpOutput + "['" + grpStr + "']"
                else:
                    grpOutput = grpOutput + "[None]"
            print(grpOutput)
    else:        
        print("Regex: no match [" + stringToSearch + "]")

def analyse_match_list(pattern, listOfStrings):
    for item in listOfStrings:
        analyse_match(pattern, item)


"""
END: Reusable Regular Expression functions
"""        

"""
START: Testing functiosn from RMIT labs
"""
def test_Regex(pattern, matches, skips):
    count = 0
    
    for m in matches:
        if re.match(pattern, m):
            count +=1
            print( "\""+m+"\""," is matched successfully!")
        else:
            print ('Failed to match ',"\""+m+"\"")
    for s in skips:
        if not re.match(pattern, s):
            count += 1
            print( "\""+s+"\""," is skipped successfully!")
        else:
            print('Failed to skip ', "\""+s+"\"")
    print()
    if count == len(matches)+len(skips):
        print("Your defined pattern has fulfilled all requirements.")
    else:
        print("Your defined pattern has fulfilled",count, "out of", len(matches)+len(skips), "requirements.")


# define another test function, so that it tests whether we capture the capture group successfully too.
def test_CaptureRegex(pattern, matches, skips,cap_groups = []):
    count = 0
    
    for i in range(0,len(matches)):
        result = re.match(pattern, matches[i])
        if result:
            count +=1
            print( "\""+matches[i]+"\""," is matched successfully!",end='\t')
            if cap_groups != [] and list(result.groups())!= cap_groups[i]: # the task requires capture groups
                count -=1
                print("But,",cap_groups[i]," are not capture properly")
            else: 
                print()
        else:
            print ('Failed to match ',"\""+matches[i]+"\"")
    for s in skips:
        if not re.match(pattern, s):
            count += 1
            print( "\""+s+"\""," is skipped successfully!")
        else:
            print('Failed to skip ', "\""+s+"\"")
    print()
    if count == len(matches)+len(skips):
        print("Your defined pattern has fulfilled all requirements.")
    else:
        print("Your defined pattern has fulfilled",count, "out of", len(matches)+len(skips), "requirements.")
    

"""
END: Testing functiosn from RMIT labs
"""        
