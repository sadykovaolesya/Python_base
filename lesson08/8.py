import random

class GameLoto:

    def __init__(self,player,comp):
        self.player = player
        self.comp = comp

    def print_card(name,card):
        print('-' * 7 + name + '-' * 7 + '\n' + ' '.join(
            [str(elem) if i % 9 else str(elem) + '\n' for i, elem in enumerate(card, 1)]) + '-' * 22)

    def start(self):

        kegs = list(range(1, 90))
        random.shuffle(kegs)


        for i, keg in enumerate(kegs):

            print(f'New keg: {keg} (kegs left {len(kegs)-i})')

            GameLoto.print_card(self.player.name, self.player.card)
            GameLoto.print_card(self.comp.name, self.comp.card)
            a = input('Cross out: y/n')
            if a == 'y':
                if keg in self.player.card:
                    self.player.card[self.player.card.index(keg)] = '-'

                    res = [el for el in self.player.card if type(el) == type(1)]
                    if len(res)== 0:
                        print('You win')
                        break
                else:
                    print('You lose')
                    break
            if a == 'n':
                if  keg in self.player.card:
                    print('You lose')
                    break

            if keg in self.comp.card:
                self.comp.card[self.comp.card.index(keg)] = '-'
                res = [el for el in self.comp.card if type(el) == type(1)]
                if len(res) == 0:
                    print('You lose')
                    break



class Card:

    def __init__(self,name):
        self.name = name
        self.card = []
        tmp_n = []
        spase = list(range(1, 10))
        random.shuffle(spase)
        numbers = list(range(1,90))
        random.shuffle(numbers)
        for i in range(1,16):
            tmp_n.append(numbers[i])
            if i % 5 == 0:
                tmp_n.sort()
                for i in range(4):
                    tmp_n.insert(spase[i], ' ')
                random.shuffle(spase)
                self.card += tmp_n
                tmp_n = []


c = Card('User')
c1 = Card('Computer')

game = GameLoto(c,c1)
game.start()


