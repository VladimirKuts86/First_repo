from random import randint, choice

class Hero():
    def __init__(self):
        self.health = 100 # полоска здоровья бойцов
        self.stars = 0 # звёзды, которые набираются для суперудара
        self.punch = 10 # удар рукой
        self.kick = 20 # удар ногой
        self.kick_in_jump = int(self.kick * 0.75) # удар ногой в прыжке 
        self.super_punch_1 = 25 # супер_удар_1
        self.super_punch_2 = 30 # супер_удар_2
        self.block = False # блок
        self.jump_back = False # отпрыгнуть
        self.player_name = '' # название бойца определённого для игрока
        self.npc_name = '' # название бойца определённого для компьютера
        self.players_choice = randint(0, 1) # рандомайзером выбираем какой боец достанется игроку, а какой компьютеру
        self.players_priority = randint(0, 1) # рандомайзером определяем игрок или компьютер будет ходить первым

    def players_move_priority(self):
        if self.players_choice == 0: # закрепляем за игроком и компьютером выпавших бойцов 
            self.player = chebu
            self.npc = labubu
            self.player_name += 'Чебурашка'
            self.npc_name += 'Лабубу'
        else:
            self.player = labubu
            self.npc = chebu
            self.npc_name += 'Чебурашка'
            self.player_name += 'Лабубу'
        if self.players_priority == 0: # закрепляем очередность ходов за игроком и компьютером
            self.players_move = True
            print(f'Вы ходите первым, вам выпал боец "{self.player_name}".',
                  f'Вашим противником будет "{self.npc_name}".')
        else:
            self.players_move = False
            print(f'Ваш противник ходит первым, ему выпал "{self.npc_name}".',
                  f'Вам выпал "{self.player_name}".')

    def punch_method(self, other_player):
        if self.block == True:
            self.health -= int(self.punch / 2)
        elif self.jump_back == True:
            self.health -= int(self.punch / 3)
        else:
            self.health -= self.punch

    def kick_method(self, other_player):
        if self.block == True:
            self.health -= int(self.kick / 2)
        elif self.jump_back == True:
            self.health -= int(self.kick / 3)
        else:
            self.health -= self.kick

    def kick_in_jump_method(self, other_player):
        if self.block == True:
            self.health -= int(self.kick_in_jump / 2)
        elif self.jump_back == True:
            self.health -= int(self.kick_in_jump / 3)
        else:
            self.health -= self.kick_in_jump

    def block(self):
        pass

    def fighting(self):
        npc_move = [self.punch_method, self.kick_method, self.kick_in_jump_method]
        npc_block = []
        if not self.players_move:
            self.move = choice(npc_move)
        else:
            print(f'Введите цифру соответствующую команде для бойца: 1. Удар рукой - "ур"\n'
                  f'\t\t\t\t\t\t 2. Удар ногой - "ун"\n'
                  f'\t\t\t\t\t\t 3. Удар ногой в прыжке - "унп"\n')
            x = input('Место для ввода команды: ')
            if x != 1 or x != 2 or x != 3:
                print(f'Вы ввели неправильную команду, ваш боец пропускает ход!')
                self.players_move = False
            else:
                self.move = choice(npc_move)


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
    chebu.players_move_priority()
    chebu.fighting()
    





chebu = Hero()
labubu = Hero()
fighting_game([chebu, labubu])


