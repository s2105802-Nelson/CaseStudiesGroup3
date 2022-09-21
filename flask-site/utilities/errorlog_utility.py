'''
Reminder on how to use:
from utilities import errorlog_utility as errorlog

# Initialize the error log
functionName = "my_function()"
logger = errorlog.ErrorLog(True, "file_prefix") # can pass in a different relative folder path

# Process
try:
    logger.log_message(functionName + " started.")

    error = False
    if error == True:    
    	logger.log_error("Error occurred.")
except:
    logger.log_exception()
    raise
finally:
    logger.log_message(functionName + " function ended.")
    logger.write_logs()   

'''

from datetime import datetime
import os
import traceback
from pathlib import Path

class ErrorLog:
  # Properties and default values
  enableDebugFile = True
  debugFileName = ""
  debugFolderPath = "debug/"

  # initialize a list of log messages, to allow queueing of logs and one write as default
  debugLogs = list()

  # Constructor
  def __init__(self, enableDebugging, fileNamePrefix, folderPath="debug/"):
    self.enableDebugFile = enableDebugging
    self.debugFileName = fileNamePrefix + "." + datetime.now().strftime("%Y%m%d.%H%M%S") + ".log"
    self.debugFolderPath = folderPath

  def ensureDebugFolderPath(self):
    if self.enableDebugFile:
      # Make sure the path ends with a '/'
      if self.debugFolderPath.endswith("/") == False & self.debugFolderPath.endswith("\\") == False:
        self.debugFolderPath += "/"
      # Create the debug folder, if it doesn't already exist
      if not os.path.exists(self.debugFolderPath):
        Path(self.debugFolderPath).mkdir(parents=True,exist_ok=True)      

  '''
  START Log Functions - where you add log messages to a list, and call write_logs at the end
  this is the one to use most of the time so you only have one write operation
  '''
  def log_message(self, message):
    if self.enableDebugFile:
      self.debugLogs.append(datetime.now().strftime("%Y-%m-%d.%H:%M:%S") + " Message: " + message)

  def log_error(self, message):
    if self.enableDebugFile:
      self.debugLogs.append(datetime.now().strftime("%Y-%m-%d.%H:%M:%S") + " Error: " + message)

  def log_exception(self):
    if self.enableDebugFile:
      message = datetime.now().strftime("%Y-%m-%d.%H:%M:%S") + "Exception: Exception occurred! \n"
      message += traceback.format_exc() + "\n"
      self.debugLogs.append(message)

  def log_break_line(self):
    if self.enableDebugFile:
      self.debugLogs.append("\n")

  def write_logs(self):
    if self.enableDebugFile:            
      # write the log messages to a debug file, either new or append
      self.ensureDebugFolderPath()
      with open(self.debugFolderPath + self.debugFileName,'a') as out_file:
        for log in self.debugLogs:        
          out_file.write(log + '\n')
        out_file.write('\n\n')  

      # clear the debug logs, in case we end up writing again
      self.debugLogs.clear()
  
  '''
  END Log Functions
  '''

  '''
  START Write Functions - logging that writes to file immediately
  '''
  def write_message(self, message):
    if self.enableDebugFile:
      self.write_log_line(datetime.now().strftime("%Y-%m-%d.%H:%M:%S") + " Message: " + message)

  def write_error(self, message):
    if self.enableDebugFile:
      self.write_log_line(datetime.now().strftime("%Y-%m-%d.%H:%M:%S") + " Error: " + message)

  def write_exception(self):
    if self.enableDebugFile:
      message = datetime.now().strftime("%Y-%m-%d.%H:%M:%S") + "Exception: Exception occurred! \n"
      message += traceback.format_exc() + "\n"
      self.write_log_line(message)

  def write_break_line(self):
    if self.enableDebugFile:
      self.write_log_line("\n")

  def write_log_line(self, logLine):
    if self.enableDebugFile:
      # write the line to file
      self.ensureDebugFolderPath()
      with open(self.debugFolderPath + self.debugFileName,'a') as out_file:          
        out_file.write(logLine + '\n')
  '''
  END Write Functions
  '''
