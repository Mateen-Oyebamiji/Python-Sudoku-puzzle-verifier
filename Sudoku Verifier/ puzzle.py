from sudoku import load_puzzle  
from sudoku import puzzle_to_string  
from sudoku import check_rows  
from sudoku import check_columns  
from sudoku import check_substring  

def game():

    filename=input("Enter filename:")
    p=load_puzzle(filename)
    print(load_puzzle(filename))
    

    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j]==0:
                p[i][j]= " "
            
        
    puzzle_to_string(p)
    x=[]
    more=True
    while more:
        move=list(input("Enter move, row/col/number(quit to exit):"))
        
        z=int(move[0])
        y=int(move[2])
        p[z][y]=(int(move[4]))
        for k in p:
            for l in k:
                if k==" ":
                    k=0
                    print(p)
                    if (check_rows(p)==[]  and check_columns(p)==[] and check_substring(p)==[]):
                        puzzle_to_string(p)
                        if k==0:
                            k=" "
                        puzzle_to_string(p)
                    else:
                        print("invalid try again")
        puzzle_to_string(p)
        

        if move=="quit":
            more=False

 
def main():
    sudoku=game()
    game()


if __name__ == "__main__":
    main()

