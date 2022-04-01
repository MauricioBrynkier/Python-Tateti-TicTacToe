import os

def display_board(choice,pos,player_1):
    
    
    if choice in range(1,10):
        if not player_1:
            pos[int(choice)-1] ='X'
            
        else:
            pos[int(choice)-1] ='O'
            
    
    print("       |       |")
    print(f"   {pos[0]}   |   {pos[1]}   |   {pos[2]}")
    print("       |       |")
    print("-----------------------")
    print("       |       |")
    print(f"   {pos[3]}   |   {pos[4]}   |   {pos[5]}")
    print("       |       |")
    print("-----------------------")
    print("       |       |")
    print(f"   {pos[6]}   |   {pos[7]}   |   {pos[8]}")
    print("       |       |")
    
    return pos


def win_condition(pos):
    
    if pos[0] == pos[1] == pos[2]:
        return True
    if pos[3] == pos[4] == pos[5]:
        return True
    if pos[6] == pos[7] == pos[8]:
        return True
    if pos[0] == pos[3] == pos[6]:
        return True
    if pos[1] == pos[4] == pos[7]:
        return True
    if pos[2] == pos[5] == pos[8]:
        return True
    if pos[0] == pos[4] == pos[8]:
        return True
    if pos[2] == pos[4] == pos[6]:
        return True
    
    return False

def game_logic():
    
    
    player_1 = True
    choice = ''
    pos = ['1','2','3','4','5','6','7','8','9']
    
    display_board(choice,pos,player_1)
    
    while not win_condition(pos):
        
        while choice not in range(1,10):
            
            if player_1:
                
                choice = int(input('Que el jugador 1 elija una posicion del 1 al 9: '))
                           
                if choice not in range(1,10):
                    print('posicion erronea, por favor vuelve a intentarlo')
                
                else:
                    player_1 = False
                             
                             
            else:
                choice = int(input('Que el jugador 2 elija una posicion del 1 al 9: '))
                             
                if choice not in range(1,10):
                    print('posicion erronea, por favor vuelve a intentarlo')
                else:
                    player_1 = True
        
        os.system('cls')
        pos = display_board(choice,pos,player_1)
        choice = ''
                             
                
                
    if player_1:
        print('Felicidades Jugador 2')
                             
    else:
        print('Felicidades Jugador 1')



game_logic()