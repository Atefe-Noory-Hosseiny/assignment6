def show():                   
    for row in game_board:
        for col in row:
            print(col,end=" ")     
        print()    

def chek_game():
    if game_board[0][0] =="o" and game_board[0][1]=="o" and game_board[0][2]=="o":
        print("player1 win")
        quit()
    elif game_board[1][0] =="o" and game_board[1][1]=="o" and game_board[1][2]=="o":
        print("player1 win")
        quit()
    elif game_board[2][0] =="o" and game_board[2][1]=="o" and game_board[2][2]=="o":
        print("player1 win")
        quit()
    elif game_board[0][0] =="o" and game_board[1][0]=="o" and game_board[2][0]=="o":
        print("player1 win")
        quit()
    elif game_board[0][1] =="o" and game_board[1][1]=="o" and game_board[2][1]=="o":
        print("player1 win")
        quit()
    elif game_board[0][2] =="o" and game_board[1][2]=="o" and game_board[2][2]=="o":
        print("player1 win")
        quit()
    elif game_board[0][0] =="o" and game_board[1][1]=="o" and game_board[2][2]=="o":
        print("player1 win")
        quit()
    elif game_board[0][2] =="o" and game_board[1][1]=="o" and game_board[2][0]=="o":
        print("player1 win")
        quit()

    elif game_board[0][0] =="x" and game_board[0][1]=="x" and game_board[0][2]=="x":
        print("player2 win")
        quit()
    elif game_board[1][0] =="x" and game_board[1][1]=="x" and game_board[1][2]=="x":
        print("player2 win")
        quit()
    elif game_board[2][0] =="x" and game_board[2][1]=="x" and game_board[2][2]=="x":
        print("player2 win")
        quit()
    elif game_board[0][0] =="x" and game_board[1][0]=="x" and game_board[2][0]=="x":
        print("player2 win")
        quit()
    elif game_board[0][1] =="x" and game_board[1][1]=="x" and game_board[2][1]=="x":
        print("player2 win")
        quit()
    elif game_board[0][2] =="x" and game_board[1][2]=="x" and game_board[2][2]=="x":
        print("player2 win")
        quit()
    elif game_board[0][0] =="x" and game_board[1][1]=="x" and game_board[2][2]=="x":
        print("player2 win")
        quit()
    elif game_board[0][2] =="x" and game_board[1][1]=="x" and game_board[2][0]=="x":
        print("player2 win")
        quit()

game_board=[["-","-","-"],      
            ["-","-","-"],      
            ["-","-","-"]]
show()

while True:        
    #player1 =>o
    print("player1")
    while True:
        row=int(input("enter row: "))     
        col=int(input("enter col: "))
        if 0<= row <=2 and 0<= col <=2:
            if game_board[row][col]=="-":        
                game_board[row][col]="o"
                show()
                chek_game()
                break 
            else:
                print("ye khone dige entekhab kon")    
        else:
            print("bein 0 va 2 entekhab konid")
    #player2 => x
    print("player2")
    while True:
        row=int(input("enter row: "))
        col=int(input("enter col: "))
        if 0<= row <=2 and 0<= col <=2:
            if game_board[row][col]=="-":      
                game_board[row][col]="x"
                show()
                chek_game()
                break 
            else:
                print("ye khone dige entekhab kon")
        else:
            print("bein 0 va 2 entekhab konid")
                
                
        