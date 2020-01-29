import csp
import time

def easy_map():
    variablelist = []
    variablelist.append(((0,0),(1,0)))
    variablelist.append(((0,1),(0,2)))
    variablelist.append(((1,1),))
    variablelist.append(((2,0),(2,1)))
    variablelist.append(((1,2),(2,2)))

    variabledict = {}
    variabledict[variablelist[0]] = (6,"*")
    variabledict[variablelist[1]] = (2,"/")
    variabledict[variablelist[2]] = (1,"none")
    variabledict[variablelist[3]] = (3,"/")
    variabledict[variablelist[4]] = (1,"-")

    return (3,tuple(variablelist),variabledict)


def exerc_map():
    vlist = []
    vdict = {}
    vlist.append(((0,0),(1,0)))
    vdict[vlist[0]] = (11,"+")
    vlist.append(((0,1),(0,2)))
    vdict[vlist[1]] = (2,"/")
    vlist.append(((1,1),(1,2)))
    vdict[vlist[2]] = (3,"-")
    vlist.append( ((0,3), (1,3)) )
    vdict[vlist[3]] = (20,"*")
    vlist.append( ((0,4), (0,5),(1,5),(2,5)) )
    vdict[vlist[4]] = (6, "*")
    vlist.append( ((1,4), (2,4)) )
    vdict[vlist[5]] = (3,"/")
    vlist.append(((2,0), (2,1),(3,0), (3,1)))
    vdict[vlist[6]] = (240,"*")

    vlist.append(((2,2),(2,3)))
    vdict[vlist[7]] = (6,"*")

    vlist.append(((4,0),(4,1)))
    vdict[vlist[8]] = (6,"*")

    vlist.append(((5,0), (5,1), (5,2)))
    vdict[vlist[9]] = (8,"+")

    vlist.append(((3,2),(4,2)))
    vdict[vlist[10]] = (6,"*")

    vlist.append(((5,3), (5,4)))
    vdict[vlist[11]] = (2,"/")

    vlist.append(((4,5), (5,5)))
    vdict[vlist[12]] = (9,"+")

    vlist.append(((3,3),(4,3),(4,4)))
    vdict[vlist[13]] = (7,"+")

    vlist.append(((3,4),(3,5)))
    vdict[vlist[14]] = (30, "*")

    return(6,tuple(vlist),vdict)   

def expert():
    vdict = {}
    vlist = [((0,0),(0,1),(0,2)), ((0,3),(1,2),(1,3)),((1,4),(0,4),(0,5)),
             ((1,6),(0,6),(0,7)), ((0,8),(1,7),(1,8)), ((1,0), (1,1), (2,0)),
             ((2,1),(2,2),(2,3)), ((2,4),(2,5),(1,5)),((2,6),(2,7),(3,7)),
             ((2,8),(3,8)),((3,0),(3,1),(3,2),(4,1)), ((3,3),(3,4)), ((4,4),(3,5),(4,5)),
             ((3,6),(4,6),(4,7)), ((4,8),(5,8),(6,8)), ((4,0),), ((4,2),(4,3)),
             ((5,0),(6,0)), ((5,1),(6,1)), ((5,2),(5,3)), ((5,5),(5,6),(5,7)),
             ((7,0),(8,0),(7,1)), ((6,2),(7,2)), ((8,1),(8,2)),((8,3),(8,4),(8,5)),
             ((8,6),(8,7)),((8,8),), ((7,3),(7,4)), ((6,3),(6,4),(5,4)),
             ((7,7),(7,8)),((6,6),(6,7),(7,6)), ((6,5),(7,5))]
    
    vdict[vlist[0]] = (24,"*")
    vdict[vlist[1]] = (18,"+")
    vdict[vlist[2]] = (126,"*")
    vdict[vlist[3]] = (17,"+")
    vdict[vlist[4]] = (21,"+")
    vdict[vlist[5]] = (9,"+")
    vdict[vlist[6]] = (14,"+")
    vdict[vlist[7]] = (40,"*")
    vdict[vlist[8]] = (504,"*")
    vdict[vlist[9]] = (8,"*")
    vdict[vlist[10]] = (81,"*")
    vdict[vlist[11]] = (2,"/")
    vdict[vlist[12]] = (23,"+")
    vdict[vlist[13]] = (30,"*")
    vdict[vlist[14]] = (14,"+")
    vdict[vlist[15]] = (2,"none")
    vdict[vlist[16]] = (3,"-")
    vdict[vlist[17]] = (4,"-")
    vdict[vlist[18]] = (1,"-")
    vdict[vlist[19]] = (72,"*")
    vdict[vlist[20]] = (36,"*")
    vdict[vlist[21]] = (336,"*")
    vdict[vlist[22]] = (2,"-")
    vdict[vlist[23]] = (6,"-")
    vdict[vlist[24]] = (17,"+")
    vdict[vlist[25]] = (4,"/")
    vdict[vlist[26]] = (6,"none")
    vdict[vlist[27]] = (6,"-")
    vdict[vlist[28]] = (15,"+")
    vdict[vlist[29]] = (1,"-")
    vdict[vlist[30]] = (10,"+")
    vdict[vlist[31]] = (1,"-")

    return (9,tuple(vlist),vdict)

    

def hard():
    vdict = {}
    vlist = [((0,0),(1,0)), ((1,1),(0,1),(0,2)),((0,3),(0,4)),
             ((1,2),),((1,3),(2,3)),((1,4),(2,4)),((2,0),(3,0)),
             ((2,1),(3,1)),((2,2),(3,2)),((3,3),(3,4)),
             ((4,0),(4,1),(4,2)),((4,3),(4,4))]
    
    vdict[vlist[0]] = (1,"-")
    vdict[vlist[1]] = (20,"*")
    vdict[vlist[2]] = (7,"+")
    vdict[vlist[3]] = (3,"none")
    vdict[vlist[4]] = (3,"-")
    vdict[vlist[5]] = (2,"/")
    vdict[vlist[6]] = (4,"-")
    vdict[vlist[7]] = (1,"-")
    vdict[vlist[8]] = (2,"/")
    vdict[vlist[9]] = (2,"-")
    vdict[vlist[10]] = (11,"+")
    vdict[vlist[11]] = (4,"+")

    return (5,tuple(vlist),vdict)



def AllValues(result,n,k,cage,operation):
    #n is the value range
    numset = list(range(1,n+1))
    AllValuesRec(result,numset,[],n,k,cage,operation)

def AllValuesRec(result,numset,mylist, n,k,cage,operation):
    #prune unnecessary values 
    if (k == 0):
        #prune the ones with the same values in the same vertical or horizontal line
        list_of_pairs = [(i,j) for i in range(len(cage)) for j in range(i+1,len(cage))]
        for pair in list_of_pairs:
            if(cage[pair[0]][0]==cage[pair[1]][0] or cage[pair[0]][1]==cage[pair[1]][1]):
                if(mylist[pair[0]]==mylist[pair[1]]):
                    return
        #prune the ones that do not give the target value for a particular cage
        if (operation[1]=="none"):
            if mylist[0]!=operation[0]:
                return
        elif(operation[1]=="+"):
            suma = 0
            for element in mylist:
                suma += element
            if suma!=operation[0]:
                return
        elif(operation[1]=="*"):
            prod = 1
            for element in mylist:
                prod *= element
            if prod != operation[0]:
                return
        elif(operation[1]=="/"):
            if max(mylist)/min(mylist) != operation[0]:
                return
        elif(operation[1]=="-"):
            if max(mylist)-min(mylist) != operation[0]:
                return
        else:
            print("Fatal error")
            return

                                    
        result.append(tuple(mylist))#append to the main list
        return

    for i in range(n):
        newList = list(mylist)
        newList.append(numset[i])
        AllValuesRec(result,numset,newList, n, k-1,cage,operation)


class kenken(csp.CSP):

    def __init__(self,map):
        # create the list of variables
        self.size, variables, self.var_dict = map
        self.nconstraintscal = 0

        #create the domain dict
        domain = {}
        for variable in variables:
            result = []
            length = len(variable)
            AllValues(result,self.size,length,variable,self.var_dict[variable])
            domain[variable] = result
        neighbors = {}

        #create the neighbor dict
        for variable in variables:
            neighbor_temp = []
            for variable2 in variables:
                if (variable2!=variable):

                    pairs = [(coordinate1,coordinate2) for coordinate1 in variable for coordinate2 in variable2]
                    for pair in pairs:
                        if(pair[0][0]==pair[1][0] or pair[0][1]==pair[1][1]):
                            neighbor_temp.append(variable2)
            
            neighbors[variable] = neighbor_temp
        csp.CSP.__init__(self,variables,domain,neighbors,self.Kenken_Constraints)

    def Kenken_Constraints(self,A,a,B,b):
        #increment the times constrain function was called
            self.nconstraintscal +=1
            list_of_pairs = [(i,j) for i in range(len(A)) for j in range(len(B))]
            
            for pair in list_of_pairs:
                if(A[pair[0]][0]==B[pair[1]][0] or A[pair[0]][1]==B[pair[1]][1]):
                    if a[pair[0]]==b[pair[1]]:
                        return False
            
            return True
    
    def display(self,result):
        problem = [[0]*self.size for i in range(self.size)]
        solution = [[0]*self.size for i in range(self.size)]

        #put the values on the problem matrix
        for key,value in self.var_dict.items():
            for coord in key:
                if value[1] != "none":
                    problem[coord[0]][coord[1]] =  str(value[0])+value[1]
                else:
                    problem[coord[0]][coord[1]] =  str(value[0])

        #put the values on the solution matrix
        for key, value in result.items():
            for i in range(len(key)):
                solution[key[i][0]][key[i][1]] = value[i]

        print("The cages of the problem:\n")
        for line in problem:
            for item in line:
                print(item,end="\t")
            print("")
        print("\nThe solution:\n")
        for line in solution:
            for item in line:
                print(item,end = "\t")
            print("")


start_time = time.time()
print("1.3x3 ~ Easy")
print("2.5x5 ~ Hard")
print("3.6x6 ~ Exercise's map")
print("4.9x9 ~ Expert")
nb = input("Select the map you want to solve: ")

number = int(nb)

print("1.BT")
print("2.BT+MRV")
print("3.FC")
print("4.FC+MRV")
print("5.MAC")
print("6.MIN_CONFLICT")
nb = input("Select the algorithm you want to solve it with: ")
number1 = int(nb)

start_time = time.time()
if(number==1):
    a=kenken(easy_map())
elif(number==2):
    a=kenken((hard()))
elif(number ==3):
    a=kenken(exerc_map())
else:
    a=kenken(expert())


if (number1 == 1):
    b = csp.backtracking_search(a)
elif (number1 == 2):
    b = csp.backtracking_search(a,select_unassigned_variable=csp.mrv)
elif (number1 == 3):
    b = csp.backtracking_search(a, inference=csp.forward_checking)
elif(number1 ==4):
    b = csp.backtracking_search(a,select_unassigned_variable=csp.mrv, inference=csp.forward_checking)
elif(number1 ==5):
    b = csp.backtracking_search(a,inference=csp.mac)
else:
    b= csp.min_conflicts(a)

if(b is not None):
    a.display(b)
else:
    print("No solutions found")

elapsed_time = time.time()-start_time
print("\nNumber of assignments:",a.nassigns)
print("Number of Constraint calls:",a.nconstraintscal)
print("Time to solve:",elapsed_time,"seconds")

