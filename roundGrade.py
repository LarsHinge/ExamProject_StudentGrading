import numpy as np
# round a vector of grade to 7-scale grade
def roundGrade(grades):
	# 7-scale grade
	scale = [-3, 0, 2, 4, 7, 10, 12]
	
	for i in range(len(grades)):
		minD = 100
		gradeToScale = -1
		
		# find the closest grade in 7-scale
		for j in range(len(scale)):
			if (abs(grades[i] - scale[j]) <= minD):
				minD = grades[i] - scale[j]
				gradeToScale = scale[j]
		grades[i] = gradeToScale

	gradesRounded = grades
	return gradesRounded