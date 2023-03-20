import random
import math





def generateLevel(n, items):
    level = [['.'] * n for _ in range(n)]


    def distribute(item, quantity):
        print(f"distributing {quantity} {item}s")
        while quantity > 0:
            r, c = random.randint(0, n - 1), random.randint(0, n - 1)
            if level[r][c] == '.':
                level[r][c] = item
                quantity -= 1
        print('finished distribution')  

    for item in items:
        distribute(item, items[item])
    
    return level

    
def printLevel(level):
    for i, row in enumerate(level):
        print(f"  {' -  ' * len(level)}   ") if i != 0 else print(f"  {' =  ' * len(level)}   ")
        print(f"|| {' | '.join(row)} ||")
    print(' ', ' =  ' * len(level))


def playerMoveTo(level, x, y):
    if 0 <= x < len(level) and 0 <= y < len(level):
        if level[y][x] == '.':
            level[player_y][player_x] = '.'
            level[y][x] = 'P'
            return True
        else:
            return False
        
    else:
        return False

def locateCharacter(level, c):
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == c:
                return [i, j]
        


def main():
    print('Welcome to candle game')
    CELLS = 10
    LIGHT_DECAY = 5
    DIFFICULTY = 1

    global player_x
    global player_y



    ITEMS  = {
        'c' : 5,
        't' : 5,
        'f' : 4,
        'd' : 2,
        'T' : 1,
        'P' : 1
    }



    level = generateLevel(CELLS, ITEMS)
    player_y, player_x = locateCharacter(level, 'P')

    while True:
        printLevel(level)
        player_move = input('enter a move: ')
        match player_move:
            case 'w':
                if playerMoveTo(level, player_x, player_y - 1):
                    player_y -= 1
            case 'a':
                playerMoveTo(level, player_x - 1, player_y)
                player_x -= 1
            case 's':
                playerMoveTo(level, player_x, player_y + 1)
                player_y += 1
            case 'd':
                playerMoveTo(level, player_x + 1, player_y)
            case _:
                player_move = input('please enter a valid move')


main()



