"""
Author : Lakith Karunaratne
Title : Eisenhower Productivity Matrix
Module : Task Card

Description:


"""
import time

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
        """
        This is the Card that is created when adding a task

        Contains :
                Task Instance ID
                Task Name
                Task Status
                Date / Time Added
                Date / Time Last Modified
                Date / Time Completed
        """
        self.taskInstance = "" # TODO : ID number generated to identify the contents
        self.taskName = taskName
        self.taskComplete = False     # all new tasks are incomplete
        self.dateAdded = time.strftime("%d/%m/%Y %I:%M%p") # current time
        self.lastModified = ""
        self.dateCompleted = ""
        return


    """
    Primary Builtins
    """
    def printTask(self):
        """ Returns a prettfied output with all the detais of the card """
        return -1

    """
    Primary Accessors
    """
    def get_dateAdded(self):
        """
        """
        return self.dateAdded

    def get_dateCompleted(self):
            """
            """
            if self.taskComplete is True:
                  return self.dateCompleted
            else:
                  return "task incomplete"
            
    
    def get_lastModified(self):
        """
        """
        return self.lastModified
    

    def get_taskName(self):
        """
        returns the task name
        """
        return self.taskName
      

    def get_taskStatus(self):
        """
        """
        if self.taskComplete is True:
                return "Task Complete"
        else:
                return "Task Incomplete"
      
      
      
    
    
    
    """
    Primary Mutators
    """

if __name__ == "__main__":
    # this is the code test area

    task1 = Task("the first task")
    print("task name ",task1.taskName)
    print("date added ",task1.dateAdded)
    print("last modified ",task1.lastModified)
    print("date completed ",task1.dateCompleted)
    print("task complete status: ",task1.taskComplete)
    print("auto gen code ",task1.taskInstance,'\n')

    print("## Testing Accessors ##")
    print("Task Name: ",task1.get_taskName)
    print("Date Added",task1.get_dateAdded)
    print("Date Completed: ",task1.get_dateCompleted)
    print("Last Modified",task1.get_lastModified)
    print("Task Status:",task1.get_taskStatus)

    pass