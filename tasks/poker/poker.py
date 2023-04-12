mas_value = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
mas_suit = ['C','S','D','H']
mas_value_T = mas_value[:9]
mas_mas = []
k = 0
for i in mas_value_T:
    mas_mas.append(mas_value[k:k+5])
    k = k+1
    
def consist_mas(lst, mas):
    for i in mas:
        if not lst.count(i) > 0:
            return 0
    return 1

def split_list(a_list):
    half = len(a_list)/2
    half = int(half)
    return a_list[:half], a_list[half:]
    
def High_Card(player):
    mas = []
    for i in reversed(mas_value):
            if i in player:
               mas.append(mas_value.index(i)+2)
    return mas       

def One_Pair(player):
    mas = []
    flag = 0
    k = 0
    for i in mas_value:
        if player.count(i) == 2:
            flag = 1
            k = mas_value.index(i)+2
    if flag:
        mas.append(k)
        mas2 = High_Card(player)
        for i in High_Card(player):
            if (i == k):
                mas2.remove(i)
        mas = mas + mas2    
    return flag, mas

def Two_Pairs(player):
    mas = []
    flag = 0
    k = [] 
    sum = 0
    for i in reversed(mas_value):
        if player.count(i) > 1:
            sum = sum + 1
            k.append(mas_value.index(i)+2)
    if sum == 2:
        flag = 1
    if flag:
        mas.append(k[0])
        mas.append(k[1])
        mas2 = High_Card(player)
        for i in High_Card(player):
            if (i == k[0] or i == k[1]):
                mas2.remove(i)
        mas = mas + mas2    
    return flag, mas

def Three_of_a_Kind(player):
    mas = []
    flag = 0
    k = 0
    for i in mas_value:
        if player.count(i) == 3:
            flag = 1
            k = mas_value.index(i)+2
    if flag:
        mas.append(k)
        mas2 = High_Card(player)
        for i in High_Card(player):
            if (i == k):
                mas2.remove(i)
        mas = mas + mas2    
    return flag, mas
    
def Straight(player):
    flag = 0
    mas = []
    for i in mas_mas:
        if consist_mas(player,i):
            flag = 1
            mas.append(High_Card(player)[0])
    return flag, mas
    
def Flush(player):
    flag = 0
    mas = []
    for i in mas_suit:
        if player.count(i) == 5:
            flag = 1
            mas = High_Card(player)
    return flag, mas

def Full_House(player):
    flag = 0
    mas = []
    if One_Pair(player)[0] and Three_of_a_Kind(player)[0]:
        flag = 1
        mas.append(Three_of_a_Kind(player)[1][0])
        mas.append(One_Pair(player)[1][0])
    return flag, mas

def Four_of_a_Kind(player):
    mas = []
    flag = 0
    k = 0
    for i in mas_value:
        if player.count(i) == 4:
            flag = 1
            k = mas_value.index(i)+2
    if flag:
        mas.append(k)
        mas2 = High_Card(player)
        for i in High_Card(player):
            if (i == k):
                mas2.remove(i)
        mas = mas + mas2    
    return flag, mas
    
def Straight_Flush(player):
    flag = 0
    mas = []
    if (Straight(player)[0] and Flush(player)[0]):
        flag = 1
        mas = mas + Straight(player)[1]
    return flag, mas

def Royal_Flush(player):
    flag = 0
    if (Straight_Flush(player)[0] and player.count('A')>0):
        flag = 1
    return flag
    
def level(player):
    if Royal_Flush(player) == 1:
        return 9
    if Straight_Flush(player)[0] == 1:
        return 8
    if Four_of_a_Kind(player)[0] == 1:
        return 7
    if Full_House(player)[0] == 1:
        return 6
    if Flush(player)[0] == 1:
        return 5
    if Straight(player)[0] == 1:
        return 4
    if Three_of_a_Kind(player)[0] == 1:
        return 3
    if Two_Pairs(player)[0] == 1:
        return 2
    if One_Pair(player)[0] == 1:
        return 1
    return 0
    
def versus(level, player1, player2):
    mas1 = []
    mas2 = []
    if level == 8:
        mas1 = Straight_Flush(player1)[1]
        mas2 = Straight_Flush(player2)[1]
    if level == 7:
        mas1 = Four_of_a_Kind(player1)[1]
        mas2 = Four_of_a_Kind(player2)[1]
    if level == 6:
        mas1 = Full_House(player1)[1]
        mas2 = Full_House(player2)[1]
    if level == 5:
        mas1 = Flush(player1)[1]
        mas2 = Flush(player2)[1]
    if level == 4:
        mas1 = Straight(player1)[1]
        mas2 = Straight(player2)[1]
    if level == 3:
        mas1 = Three_of_a_Kind(player1)[1]
        mas2 = Three_of_a_Kind(player2)[1]
    if level == 2:
        mas1 = Two_Pairs(player1)[1]
        mas2 = Two_Pairs(player2)[1]
    if level == 1:
        mas1 = One_Pair(player1)[1]
        mas2 = One_Pair(player2)[1]
    if level == 0:
        mas1 = High_Card(player1)
        mas2 = High_Card(player2)

    for k in range(len(mas1)):
        if mas1[k] > mas2[k]:
            return 1
        if mas2[k] > mas1[k]:
            return 0
            
def poker(game):
    half = len(game)/2
    half = int(half)
    player1 = game[:half]
    player2 = game[half:]
    #print(player1, level(player1), ' ',player2, level(player2))
    if (level(player1) > level(player2)):
        return 1
    if (level(player1) == level(player2)):
        return versus(level(player1), player1, player2)
    return 0 
    

k = 0
with open('poker.txt') as f:
    contents = f.readlines()
    
for i in contents:
    k = k + poker(i)

print("first player won ",k," times")


