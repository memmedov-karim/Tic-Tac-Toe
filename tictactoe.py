board = ["-","-","-",
        "-","-","-",
        "-","-","-",]
def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])
display_board()
while True:
    position1,choisen1 = map(str,input("Playe1-Choise your position:1 to 9,and choise: ").split())
    position2,choisen2 = map(str,input("Player2-Choise your position:1 to 9,and choise: ").split())
    if position1 == position2:
        position2 = int(input("Please Again: "))
    position1=int(position1)-1
    position2 = int(position2)-1
    board[position1] = choisen1
    board[position2] = choisen2
    display_board()
    if ((board[0]=="x" and board[1]=="x" and board[2]=="x") or 
            (board[3]=="x" and board[4]=="x" and board[5]=="x") or
            (board[6]=="x" and board[7]=="x" and board[8]=="x") or
            (board[0]=="x" and board[3]=="x" and board[6]=="x") or
            (board[1]=="x" and board[4]=="x" and board[7]=="x") or
            (board[2]=="x" and board[5]=="x" and board[8]=="x") or
            (board[0]=="x" and board[4]=="x" and board[8]=="x") or
            (board[2]=="x" and board[4]=="x" and board[6]=="x")):
        print("Player1 Winner")    
        break
    elif ((board[0]=="o" and board[1]=="o" and board[2]=="o") or 
            (board[3]=="o" and board[4]=="o" and board[5]=="o") or
            (board[6]=="o" and board[7]=="o" and board[8]=="o") or
            (board[0]=="o" and board[3]=="o" and board[6]=="o") or
            (board[1]=="o" and board[4]=="o" and board[7]=="o") or
            (board[2]=="o" and board[5]=="o" and board[8]=="o") or
            (board[0]=="o" and board[4]=="o" and board[8]=="o") or
            (board[2]=="o" and board[4]=="o" and board[6]=="o")):
        print("Player2 Winner")    
        break
        
    


             
