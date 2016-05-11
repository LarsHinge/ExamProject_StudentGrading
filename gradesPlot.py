import matplotlib.pyplot as plt

def gradePlot(GMatrix,SMatrix):
    #Number of assignments:
    NumberOfAssignments = len(GMatrix[0,:])
    #The grades:
    GA1 = GMatrix[:,0]#assignment1
    GA2 = GMatrix[:,1]#assignment2
    GA3 = GMatrix[:,2]#assignment3
    
    
    
    
    #count numbers of times each grade was given
    x = np.reshape(GMatrix,-1)
    a = sorted(x.tolist())
    b = {x:a.count(x) for x in a}
    d = b.values()
    print(d)
    print(b)
    print(a)
       # Figure: Number of bacteria
    # Make bar plot
    #plt.bar(range(7), d)
    
    # Set title and axis labels
    #plt.title("Number of bacteria")
    #plt.xlabel("Grades")
    #plt.ylabel("Occurance")
    
    # Set tick-labels
    #plt.xticks(np.arange(7)+0.5, np.array(["-3","00","02","4","7","10","12"]), rotation=10)
    
    # Show plot
    #plt.show()
