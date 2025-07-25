from random import randint, choice

class Hero():
    def __init__(self):
        self.health = 100 # полоска здоровья бойцов
        self.punch = 10 # удар рукой
        self.kick = 20 # удар ногой
        self.block = False # блок

    def punch_method(self, other_player):
        if not self.block:
            other_player.health -= self.punch
        else:
            other_player.health -= int(self.punch / 2)

    def kick_method(self, other_player):
        if not self.block:
            other_player.health -= self.kick
        else:
            other_player.health -= int(self.kick / 2)



def fighting_game(players_list):
    print(
          f'\n'
          f'\t       {chr(1421)} ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ {chr(1421)}\n'
          f'\t       ∷                                              ⋏  ⋏     ∷\n'
          f'\t       ∷   c(℺ᴥ℺)ᴐ                                   (ᵒ▾▿ᵒ)    ∷\n'
          f'\t       ∷   /|   |\\/   ДОБРО ПОЖАЛОВАТЬ НА ТУРНИР   \\/|    |\\   ∷\n'
          f'\t       ∷   \\|___|        {chr(128074)} "БИТВА УШАСТЫХ"{chr(128074)}        |____|/   ∷\n'
          f'\t       ∷     | |                                      |  |     ∷\n'   
          f'\t       ∷                                                       ∷\n'
          f'\t       {chr(1421)} ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ {chr(1421)}\n'
          f'Вам предстоит поучаствовать в битве между двумя меховыми и ушастыми - Чебурашкой и Лабубу!\n'
          f'{''.join('☰' for i in range(90))}\n\n'
          f'Вот правила этого файтинга: 1. Рандомайзер определит кто первый ходит(вы или компьютер), а так же какой персонаж из двух достанется вам, а какой компьютеру.\n'
          f'\t\t\t    2. Если первый ход выпал вам, то нужно будет ввести команду для бойца (подсказки по доступным командам будут на экране).\n'
          f'\t\t\t    3. После того, как вы введёте команду, рандомайзер выберет защитную команду для бойца управляемого компьютером.\n'
          f'\t\t\t    4. Здоровье вашего оппонента уменьшится в зависимости от того, насколько удачная или неудачная реакция выпадет у компьютера.\n'
          f'\t\t\t    5. Теперь ход переходит к компьютеру - команду для его атаки выберет рандомайзер.\n'
          f'\t\t\t    6. Вам же надо будет ввести команду для защиты от его атаки (подсказки по доступным командам будут на экране).\n'
          f'\t\t\t    7. И так далее. Ходы будут переходить по очереди между вами и компьютером, до тех пор пока у кого-то из вас полоска здоровья не стнет равна 0.\n'
          )
    players_choice = choice(['Чебурашка', 'Лабубу'])
    print(players_choice)
    players_turn = choice([True, False])
    print(players_turn)
    block_choice = choice(['Блок', 'Контрудар', ''])
    if players_turn:
        print(f'Введите цифру соответствующую команде для бойца: 1. Удар рукой - "ур"\n'
              f'\t\t\t\t\t\t 2. Удар ногой - "ун"\n'
              f'\t\t\t\t\t\t 3. Удар ногой в прыжке - "унп"\n')
        x = input('Место для ввода команды: ')
        if x == '1' or x == '2':
            if x == '1':
                if players_choice == 'Чебурашка':
                    chebu.punch_method(labubu)
                else:
                    labubu.punch_method(chebu)
            elif x == '2':
                if players_choice == 'Чебурашка':
                    chebu.kick_method(labubu)
                else:
                    labubu.kick_method(chebu)
        else:
            print(f'Вы ввели неправильную команду, ваш боец пропускает ход!')
        players_turn = False



chebu = Hero()
labubu = Hero()
# chebu.punch_method(labubu)
# chebu.kick_method(labubu)
print(labubu.health)
print(chebu.health)
fighting_game([chebu, labubu])