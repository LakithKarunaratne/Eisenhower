"""
Author : Lakith Karunaratne
Title : Eisenhower Productivity Matrix
"""

###### IMPORT MODULES #######
import time
# print (time.strftime("%d/%m/%Y %I:%M%p")) # Standard Time Format for the App

# TODO : The program needs to store 5 types of items
# TODO : the storage will need to be made more efficient
# --------------------------------------------------
#     Unsorted Storage
# --------------------------------------------------
UnsortedItems = []

# --------------------------------------------------
#     Important - Urgent Storage
# --------------------------------------------------
ImportantUrgentItems = []
# --------------------------------------------------
#     Not Important - Urgent Storage
# --------------------------------------------------
NotImportantUrgentItems = []

# --------------------------------------------------
#     Important - Not Urgent Storage
# --------------------------------------------------
ImportantNotUrgentItems = []

# --------------------------------------------------
#     Not Important - Not Urgent Storage
# --------------------------------------------------
NotImportantNotUrgentItems = []

# TODO : Functional Changes to be done on the Card

# --------------------------------------------------
#     Task : Add
# --------------------------------------------------


# --------------------------------------------------
#     Task : Edit
# --------------------------------------------------


# --------------------------------------------------
#     Task : Delete
# --------------------------------------------------


# --------------------------------------------------
#     Task : Move
# --------------------------------------------------


# --------------------------------------------------
#     Task : Change State - Done / Incomplete
# --------------------------------------------------

# TODO : Each task must be a self contained object

# --------------------------------------------------
#     Task : Instance
#     Task : Date Added
#     Task : Date Modified
#     Task : Date Completed
#     Task : Task State - Done / Incomplete

# Default Format : %d/%m/%Y %I:%M%p

# --------------------------------------------------
class Task:
      def __init__(self, taskName):
            self.taskName = taskName
            self.taskComplete = False     # all new tasks are incomplete
            self.dateAdded = time.strftime("%d/%m/%Y %I:%M%p") # current time
            self.lastModified = ""
            self.dateCompleted = ""
            return

      def get_taskName(self):
            return self.taskName
      
      def get_taskStatus(self):
            if self.taskComplete is True:
                  return "Task Complete"
            else:
                  return "Task Incomplete"
      
      def get_dateAdded(self):
            return self.dateAdded
      
      def get_lastModified(self):
            return self.lastModified
      
      def get_dateCompleted(self):
            if self.taskComplete is True:
                  return self.dateCompleted
            else:
                  return "task incomplete"
      