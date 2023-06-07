import random

def generate_8_queens()->list:
    coords = []
    for i in range(8):
        coord = (random.randint(1,8), random.randint(1,8))
        coords.append(coord)
    return coords

def check_8_queens(coords: list)->bool:
    correct = True
    for i in range(len(coords)):
        one = coords[i]
        for j in range(i + 1, len(coords)):
            two = coords[j]
            if one[0] == two[0] or one[1] == two[1] or abs(one[0]-two[0]) == abs(one[1]- two[1]):
                print(one, two)
                correct = False
                break
    return correct

def find_correct_position()->list:
    res = []
    count_try = 0
    max_tries = 10
    while len(res) <= 4 and count_try < max_tries:
        coords = generate_8_queens()
        print(len(res), count_try)
        if check_8_queens(coords):
            res.append(coords)
        count_try = count_try + 1
    return res

def print_coords(list_coords):
    for coords in list_coords:
        print(coords)
    
if __name__ == '__main__':
    coords = [(1,2),(2,4),(3,6),(4,8),(5,3),(6,1),(7,7),(8,5)]
    print(check_8_queens(coords))
    """ list_coords = find_correct_position()
    print_coords(list_coords) """

""" n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
            break

if correct:
    print('YES')
else:
    print('NO') 
 """


""" B=[['*']*8 for i in range (8)]
 
def board(B):
    print('  a b c d e f g h')
    print('  ---------------')
    for i in range(8):
        print(str(8 - i), end = ' ')
        [print(B[i][j], end = ' ') for j in range(8)]
        print(str(8 - i))
    print('  ---------------')
    print('  a b c d e f g h')
 
board(B) """