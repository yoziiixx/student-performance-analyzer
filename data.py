import numpy as np

class Data:

    def __init__(self,names,subjects):
        self.__name = np.array(names)
        self.__subject = np.array(subjects)
        self.__grade = np.full((self.__name.size, self.__subject.size), np.nan)


    def index(self,name,subject):
        try:
            row = np.where(self.__name == name)[0][0]
            col = np.where(self.__subject == subject)[0][0]
        except IndexError:
            raise ValueError("Student or subject doesn't exist")
        return row, col


    def enterGrade(self, name, subject, grade):
        try:
            if not 0<= grade <= 100:
                raise ValueError("Garde should be between 0 and 100")
            row, col = self.index(name, subject)
            self.__grade[row, col] = grade
        except ValueError as e:
            print(e)
        return self.__grade

    def studentAverage(self):
        average = np.nanmean(self.__grade, axis = 1)
        return average

    def subjectAverage(self):
        average = np.nanmean(self.__grade, axis = 0)
        return average

    def studentHighestGrade(self):
        highest = np.nanmax(self.__grade, axis = 1)
        return highest

    def studentLowestGrade(self):
        lowest = np.nanmin(self.__grade, axis = 1)
        return lowest

    def classAverage(self):
        average = np.nanmean(self.__grade)
        return average

    def studentComplete(self):
        return ~np.isnan(self.__grade).any(axis = 1)

    def studentStatus(self):
        statuses = []
        for row in self.__grade:
            if np.isnan(row).any():
                statuses.append("Incomplete")
            elif row.mean() >= 60:
                statuses.append("Pass")
            else :
                statuses.append("Fail")
        return statuses

    def studentRanking(self):
        complete = self.studentComplete()
        averages = np.mean(self.__grade[complete], axis = 1)
        order = np.argsort(averages)[::-1]
        return self.__name[complete][order], averages[order]

    def getNames(self):
        return self.__name.copy()

    def getSubjects(self):
        return self.__subject.copy()

    def getGrades(self):
        return self.__grade.copy()
















