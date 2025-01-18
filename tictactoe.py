#TIC TAC TOE
li=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def takeinput():
    while True:
        r=int(input('Enter row: '))
        c=int(input('Enter column: '))
        if r<0 or r>3 or c<0 or c>3:
            print('Invalid input')
            continue
        else:
            break
    return r,c

    
def drawboard():
    print()
    for i in range(3):
        for j in range(3):
            sign=li[i][j]
            if j==0:
                print('  '+sign+'  ',end='')
            else:
                print('| '+sign+'  ',end='')
        if i!=2:
            print()
            print('----------------')
    print()
def checkrows():
    for i in li:
        if i[0] == 'X' and i[1]=='X' and i[2] == 'X':
            return True
        elif i[0] == 'O' and i[1]=='O' and i[2] =='O':
            return True
    return False
def checkcolumns():
    for i in range(3):
        if li[0][i] == 'X' and li[1][i] == 'X' and li[2][i]=='X':
            return True
        elif li[0][i] == 'O' and li[1][i] == 'O' and li[2][i]=='O':
            return True
    return False
def checkdiagonals():
    if li[0][0]=='X' and li[1][1]=='X' and li[2][2]=='X' or li[0][0]=='O' and li[1][1]=='O' and li[2][2]=='O':
        return True
    if li[0][2]=='X' and li[1][1]=='X' and li[2][0]=='X' or li[0][1]=='O' and li[1][1]=='O' and li[2][0]=='O':
        return True
    return False
    
def playgame(p1,p2,s1,s2):
    print("The game Begins:")
    turn = 0
    while(True):
        if turn == 0:
            print(p1+":")
            r,c=takeinput()
            if li[r][c]!=' ':
               print("Position already occupied")
               continue
            else:
                li[r][c]=s1
            turn=1
        else:
            print(p2+":")
            r,c=takeinput()
            if li[r][c]!=' ':
                print("Position already occupied")
                continue
            else:
                li[r][c]=s2
            turn=0
        drawboard()
        f1=checkrows()
        f2=checkcolumns()
        f3=checkdiagonals()
        if f1 and f2 and f3:
            print("Match is a TIE")
            break
        if f1 or f2 or f3:
            if turn == 0:
                print(p1+" wins")
            else:
                print(p2+' wins')
            break
        
 
p1=input("Player 1 name: ")
p2=input("Player 2 name: ")
print("Your Board is Ready...")
drawboard()
s1=''
s2=''
x=input("\nChoose sign( 'X' or 'O') for player1: ")
if x=='X':
    s1='X'
    s2='O'
elif x=='O':
    s1='X'
    s2='O'   
else:
   print("Invalid choice")
   print('The Game will Exit....')
   exit(0)
print(p1,":",s1)
print(p2,":",s2)
print("The game will begin:")
playgame(p1,p2,s1,s2)



    

