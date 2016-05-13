# GRADEPLOT Generates plots of student grades
    #
    # Usage: dataPlot(data)
    #
    # Input  FinalGrades   An array of the final grades the students will get. 
    # Can be calculated using computeFinalGrade 
    #
    # input  GradeMatrix  A NxM matrix where M is the number of assignments and N the numebr of students 
    # Author: Lars Hinge, s154349 2016      


def gradePlot(FinalGrades,GradeMatrix):
    CSV = GradeMatrix
    #make the barplot
    GradeAppearance = np.zeros(7) #Count how many times each grade was given
    for i in range(len(FinalGrades)):
        if (FinalGrades[i] == -3): #Count the -3's
            GradeAppearance[0]+=1
        if (FinalGrades[i] == 0): #Count the 00's
            GradeAppearance[1]+=1 
        if (FinalGrades[i] == 2): #etc.
            GradeAppearance[2]+=1
        if (FinalGrades[i] == 4):
            GradeAppearance[3]+=1        
        if (FinalGrades[i] == 7):
            GradeAppearance[4]+=1  
        if (FinalGrades[i] == 10):
            GradeAppearance[5]+=1
        if (FinalGrades[i] == 12):
            GradeAppearance[6]+=1
    plt.bar(range(7), GradeAppearance)
    # Set title and axis labels
    plt.title("Grade frequency")
    plt.xlabel("Grades")
    plt.ylabel("Occurance")
    # Set tick-labels
    plt.xticks(np.arange(7)+0.5, np.array(["-3","00","02","4","7","10","12"]))
    # Show plot
    plt.show()
    
    
    #make plot 2
    x = np.array([])
    for i in range(len(CSV[:,2])):#Create x-values so they fit with y-values
        x = np.append(x,(np.arange(len(CSV[1,:]))))
    
    y = (np.reshape(CSV, -1)) #reshape the gradematrix to be a line. It can now be plottet.
       
    for i in range(len(y)):#have the dots not stack
        y[i]+=np.random.uniform(-0.1,0.1)
        x[i]+=np.random.uniform(-0.1,0.1)
        
    #plot x,y and add label
    plt.plot(x,y, "ro", label = "Grade the students scored on the assignments")
    
    #Calculate the average grade on each assignment  
    MeanY = np.array([])  
    for i in range(len(CSV[2,:])):
        MeanY = np.append(MeanY,(np.mean(CSV[:,i])))
 
    #Draw line for the average grade on each assignment
    for i in range(len(CSV[2,:])): 
        plt.plot(np.array([i-0.4,i+0.4]),np.array([MeanY[i],MeanY[i]]),
                 label = "Average grade on Assignment {:.0f} ".format(round(i+1)))
       
        
    #set labels, tickrate, ticknames, limits and a legen for the whole plot
    plt.title("Average grades for assignments")
    plt.yticks(np.array([-3,0,2,4,7,10,12]), np.array(["-3","00","02","4","7","10","12"]))
    plt.xticks(np.arange(len(CSV[:,1])-2), np.arange(1, len(CSV[:,1])-2))
    plt.xlabel("Assignments")
    plt.ylabel("Grades")
    plt.xlim([-0.2,len(CSV[1,:])-0.8])
    plt.ylim([-4,13])
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    #show the plot
    plt.show() 
    CSV = GradeMatrix
    return
