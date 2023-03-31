'''
COMP 1405 - Fall 2020
Assignment #3

Name: Bola-oyebamiji Abdul-mateen
ID:101198311
Comments:
'''


#------------------------------------------------------------------#
# provided function - do NOT remove or change
def load_puzzle(filename):
    ''' Reads a sudoku puzzle from the text file 'filename' in the current directory. 
        Returns a list of lists of integers that represents the game.
            load_puzzle(filename:str) -> str[str[int]]
        Empty cells in the game are denoted by 0s in the file (and the output list)
    '''
    puzzle = [] 
    with open(filename, "r") as f:
        for line in f:
            puzzle.append( [int(val) for val in line.split(",")] )
    return puzzle




#------------------------------------------------------------------#
def puzzle_to_string(p):
    print((p[0])[0],(p[0])[1],(p[0])[2],"|",(p[0])[3],(p[0])[4],(p[0])[5],"|",(p[0])[6],(p[0])[7],(p[0])[8])
    print((p[1])[0],(p[1])[1],(p[1])[2],"|",(p[1])[3],(p[1])[4],(p[1])[5],"|",(p[1])[6],(p[1])[7],(p[1])[8])
    print((p[2])[0],(p[2])[1],(p[2])[2],"|",(p[2])[3],(p[2])[4],(p[2])[5],"|",(p[2])[6],(p[2])[7],(p[2])[8])
    print("------+-------+------")
    print((p[3])[0],(p[3])[1],(p[3])[2],"|",(p[3])[3],(p[3])[4],(p[3])[5],"|",(p[3])[6],(p[3])[7],(p[3])[8])
    print((p[4])[0],(p[4])[1],(p[4])[2],"|",(p[4])[3],(p[4])[4],(p[4])[5],"|",(p[4])[6],(p[4])[7],(p[4])[8])
    print((p[5])[0],(p[5])[1],(p[5])[2],"|",(p[5])[3],(p[5])[4],(p[5])[5],"|",(p[5])[6],(p[5])[7],(p[5])[8])
    print("------+-------+------")
    print((p[6])[0],(p[6])[1],(p[6])[2],"|",(p[6])[3],(p[6])[4],(p[6])[5],"|",(p[6])[6],(p[6])[7],(p[6])[8])
    print((p[7])[0],(p[7])[1],(p[7])[2],"|",(p[7])[3],(p[7])[4],(p[7])[5],"|",(p[7])[6],(p[7])[7],(p[7])[8])
    print((p[8])[0],(p[8])[1],(p[8])[2],"|",(p[8])[3],(p[8])[4],(p[8])[5],"|",(p[8])[6],(p[8])[7],(p[8])[8])

#------------------------------------------------------------------#
# check rows function
def check_rows(puzzle):
    ''' read through the string from the load puzzle function to check if the
        rows are valid, if they are it returns an empty string, if they aren't 
        it returns a string with the index of the invalid list
    '''
    n_valid=[]

    for sublist in puzzle:
        for val in sublist:
            if sublist.count(0)> 8:
                n_valid.append(puzzle.index(sublist)+1)
            elif  val > 9:
                n_valid.append(puzzle.index(sublist)+1)
            elif sublist.count(val) > 1 and val !=0:
                n_valid.append(puzzle.index(sublist)+1)
            else:
                pass   
    return(n_valid)

# your functions go here!



#------------------------------------------------------------------#
#check column function helper
def helper2(puzzle):
    ''' this helper function identifies  and returns the columns in the puzzle string
    '''
    row_size=len(puzzle[1])
    colist=[]
    for i in range(row_size):
        col=[]
        for j in puzzle:
            col.append(j[i])
        colist.append(col)
    return colist

#check column function
def check_columns(puzzle):
    ''' this goes through the columns and checks if they're valid using the helper function
        and the method used in the check rows function
    '''   
    n_valid=[]
    col_puzzle=helper2(puzzle)

    for sublist in col_puzzle:
        for val in sublist:
            if sublist.count(0)> 8:
                n_valid.append(col_puzzle.index(sublist)+1)
            elif  val >9:
                n_valid.append(col_puzzle.index(sublist)+1)
            elif sublist.count(val) > 1 and val !=0:
                n_valid.append(col_puzzle.index(sublist)+1)
            else:
                pass   
    return(n_valid)


#------------------------------------------------------------------#
#helper for check_subgrid
def helper3(puzzle):
    ''' a function made to return the list of substrings
    '''
    p=puzzle
    worklist=[[p[0][0:3],p[1][0:3],p[2][0:3]], [p[0][3:6],p[1][3:6],p[2][3:6]], [p[0][6:len(p)],p[1][6:len(p)],p[2][6:len(p)]],[p[3][0:3],p[4][0:3],p[5][0:3]],[p[3][3:6],p[4][3:6],p[5][3:6]],[p[3][6:len(p)],p[4][6:len(p)],p[5][6:len(p)]],[p[6][0:3],p[7][0:3],p[8][0:3]],[p[6][3:6],p[7][3:6],p[8][3:6]],[p[6][6:len(p)],p[7][6:len(p)],p[8][6:len(p)]]]
    final_list=[]
    for i in worklist:
         
        i[0].extend(i[1])
        i[0].extend(i[2])
        i[1]=""
        i[2]= ""
        final_list.append(i[0])
    return (final_list)

def check_substring(puzzle):
    ''' read through the list from the  helper3 function to check if the
        substrings  are valid, if they are it returns an empty string, if they aren't 
        it returns a string with the index of the invalid list
    '''
    n_valid=[]
    subpuzzle=helper3(puzzle)

    for sublist in subpuzzle:
        for val in sublist:
            if sublist.count(0)> 8:
                n_valid.append(subpuzzle.index(sublist)+1)
            elif  val >9:
                n_valid.append(subpuzzle.index(sublist)+1)
            elif sublist.count(val) > 1 and val !=0:
                n_valid.append(subpuzzle.index(sublist)+1)
            else:
                pass   
    return(n_valid)

#------------------------------------------------------------------#
# Your "program" is driven by the main method
# Modify as needed to test your functions
def main():
    puzzle = load_puzzle('puzzle1.csv')
    print(puzzle)



#------------------------------------------------------------------#
# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()

puzzle = load_puzzle('puzzle1.csv')
 


 

puzzle_to_string(puzzle)
print(check_rows(puzzle))
print(check_columns(puzzle))
print(check_substring(puzzle))


def printpuzzle(x):
    for row in x:
        for col in row:
            print(col,end=" ")
             
        print("|")    
    
 

 

             
 


def helper(x):
    nvalid=[]
   
    for i in x:
        if i !=0:
            if x.count(i)>1:
                nvalid.append(x.index(i))
    print(nvalid) 

    

 

 

    
         
         
            


helper3(puzzle)