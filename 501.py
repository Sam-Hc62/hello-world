def main():
    point1 = 501
    point2 = 501
    def point_tally1():
        nonlocal point1
        while True:
            a = input('\nPlayer 1 score...')
            if not a.isdigit():
                continue
            a = int(a)
            if a < 0:
                continue
            elif a > 180:
                print('BUST!')
                break
            else:
                point1 = point1 - a 
                if -10 < point1 and point1 < 1 :
                    print('Player 1 wins!')
                    exit
                elif point1 < -10 :
                    print('BUST!')
                    point1 = point1 + a
                    return point1
                else:
                    return point1
    
    def point_tally2():
        nonlocal point2
        while True:
            b = input('\nPlayer 2 score...')
            if not b.isdigit():
                continue
            b = int(b)
            if b < 0:
                continue
            elif b > 180:
                print('BUST!')
                break
            else:
                point2 = point2 - b
                if -10 < point2 and point2 < 1 :
                    print('player 2 Wins!')
                    exit
                elif point2 < -10 :
                    print('BUST!')
                    point2 = point2 + b
                    return point2

                else:
                    return point2
                     
                
                
    def scoreboard():
        name1 = input('Player 1 name?...').title()
        name2 = input('Player 2 name?...').title()
        while True:
            print(f"\n ---------------------\n|{name1:<10}|{name2:<10}|\n|----------|----------|\n|{point1:<10}|{point2:<10}|\n ---------------------\n")
            q = input('Which player is playing?\nEnter: (1) or (2) ...')
            if not q.isdigit():
                continue
            q = int(q)
            if q == 1:
                point_tally1()
            elif q == 2:
                point_tally2()
            else:
                continue
    scoreboard()
main()