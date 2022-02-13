# Name : Jayant Chaudhary
#Email : jay03102001@gmail.com

#global Variables : 

count = 0
opcodeList = "[add"
print("Enter N : ")
N = int(input())
for i in range(N):
    opcodeList = opcodeList + " : ?"
opcodeList = opcodeList + " : mul ]"

#assignmentList : 
assignList1 = "[a=rd"
for i in range(N):
    assignList1 = assignList1 + " : ?"
assignList1 = assignList1 + " : ?]"

assignList2 = "[a=rs; b=rs2"
for i in range(N):
    assignList2 = assignList2 + " : ?"
assignList2 = assignList2 + " : ?]"

def print1():
    """ 
        print1() function is used to generate all the coverpoints for RAW, WAW hazards
        Parameters
        ----------
    """

    coverpoint = opcodeList + " :: " + assignList1 + " :: " +"[?" 
    
    #generate RAW coverpoints:
    print("\nRAW Coverpoints (both consuming and non consuming)")
    print("--------------------------------------------------------------------------------------------------")
    for i in range(N+1):
        generateStrings(N,0,i,coverpoint,0)
    
    #generate WAW strings:
    print("\n","WAW Coverpoints (both consuming and non consuming)")
    print("--------------------------------------------------------------------------------------------------")
    for i in range(N+1):
        generateStrings(N,0,i,coverpoint,1)

def print2():
    """
        print2 function is used to generate the WAR coverpoints
        Parameters
        ----------
    """
    coverpoint = opcodeList + " :: " + assignList2 + " :: " + "[?"

    print("\nWAR Coverpoints (both consuming and non consuming)")
    print("--------------------------------------------------------------------------------------------------")
    for i in range(N+1):
        generateStrings(N,0,i,coverpoint,2)

def generateStrings(N,index,k,coverpoint,hazard):
    """
        genrateStrings functions generates the condition list for all the coverpoints. It generates all the nCk 
        ( n! / ((n-k)! * k!) ) combinations for consuming instructions out of N instructions between add and mul 
        instructions


        Parameters
        ----------
        N : int
            The total number of instructions between add and mul
        index : int 
            Instruction to process for the conditionlist (To be considered consuming or not)
        k : int
            The number of instruction to be considered consuming, (k in nCk)
        coverpoint : string
                     coverpoint string along with the opcode list and assign list
        hazard : int
                 identifies the type of Hazard , 
                 0 : RAW   
                 1 : WAW
                 2 : WAR
    """

    if(index == N):
        if(hazard == 0):
             coverpoint = coverpoint + " : rs1==a or rs2==a]" 
        if(hazard == 1):
            coverpoint = coverpoint + " : rd==a]"
        if(hazard == 2):
            coverpoint = coverpoint + " : rd==a or rd==b]"
        if(k == 0):
            print(coverpoint)
            global count
            count = count + 1
        return

    coverpoint1 = coverpoint + " : rs1 == a or rs2 == a"
    coverpoint2 = coverpoint + " : rs1 != a and rs2 != a"
    if(k > 0):
        generateStrings(N,index+1,k-1, coverpoint1, hazard)
    generateStrings(N,index+1,k,coverpoint2,hazard)

print1()
print2()
print("\nTotal coverpoint count is :" ,count)
