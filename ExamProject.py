#Program for grading students
# coments
#
#
#
#imports here

def Information(matrix):
    #find number of assignments
    NoA = len(matrix.iloc[0,:])-2
    #find number of students
    NoS = len(matrix.iloc[:,0])
    return("Your {:f} students had to each hand in {:f} assignments".format(NoS, NoA))    
    
def getInput(FileName):
    # Import data using input from user and dataLoad funktion
    CSV = pd.read_csv(FileName)
    
    print("---------------------------------------------------------------")
    print(Information(CSV))
    print("---------------------------------------------------------------")
    return(CSV)


def findGradeMatrix(FileName):
    completeCSV = pd.read_csv(FileName)
    gradeMatrix = np.loadtxt(open(FileName,"rb"),delimiter=",",skiprows=1, usecols=range(2,len(completeCSV.iloc[3,:])))
    return(gradeMatrix)

def findStudentMatrix(CSV):
    studentMatrix = CSV.iloc[:,[0,1]]
    return(studentMatrix)

def main():
    FileName = (input(("Enter name of comma-separated-values file in .CSV (don't write '.csv') format containing the sudentIDs, names and grades of your students:" ))+'.csv')
    CSV = getInput(FileName)
    GradeMatrix = findGradeMatrix(FileName)
    StudentMatrix = findStudentMatrix(CSV)
    print(CSV)
    menu = {} #Main Menu options
    menu['']=""
    menu[' ']="Main Menue:"
    menu['   ']=""
    menu['1']="Load New Data."
    menu['2']="Check for data errors."
    menu['3']="Generate Plot"
    menu['4']="Display list of grades"
    menu['5']="Quit."
    
    while True: #Sorting and printing mainmenu
        options=sorted(menu.keys())
        for entry in options: 
            print(entry, menu[entry])
        
        selection=input("Please Select Number: ") #get menu option from input
   
        if selection == '1': 
            FileName = (input(("Enter name of new comma-separated-values file in .CSV (don't write '.csv') format containing the sudentIDs, names and grades of your students:" ))+'.csv')
            CSV = getInput(FileName)
            GradeMatrix = findGradeMatrix(FileName)
            StudentMatrix = findStudentMatrix(CSV)
            print(CSV) 
        elif selection == '2': 
            print(gradeErrors(CSV))
        elif selection == '3': 
            #create plots
            gradePlot(GradeMatrix,StudentMatrix)
        elif selection == '4':
            print("List of grades:")
            print(GradeMatrix)
            print("The grades the students recieve:")
            print(computeFinalGrades(GradeMatrix))
        elif selection =='5': #end
            print("Good bye!")
            break
        else: 
            print("Unknown Option Selected! Please enter a menu number between 1 and 4 or exit on 5") 


if(__name__=="__main__"):
    main()






