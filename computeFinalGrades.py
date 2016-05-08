import numpy as np
from roundGrade import roundGrade	

def computeFinalGrades(grades):
	# intialization
	nStudent = len(grades[:, 0])
	nAssignment = len(grades[0, :])

	# case number of nAssignment = 1
	if (nAssignment == 1):
		gradesFinal = grades[:, 0].T

	else:
		gradesFinal = []

		# find mean of grades of each student
		for i in range(nStudent):
			# print (grades[i, :])
			if (-3 in grades[i, :]):
				meanGrade = -3
			else: 
				meanGrade = np.mean(grades[i, :])
				
			gradesFinal.append(meanGrade)

		# print("Mean grade before round", gradesFinal)
		# round grade using roundGrade.py
		gradesFinal = roundGrade(gradesFinal)	
	return gradesFinal