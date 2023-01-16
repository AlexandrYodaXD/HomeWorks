from random import choice
from bcolors import bcolors as bc
from bcolors import csigns as cs
from os import system
clear = lambda: system('cls')
board_indent = 10 # отступ слева при отрисовке игрового поля
# создание игрового поля
def make_board():
    return [[str((3 * i) + j + 1) for j in range(3)] for i in range(3)]
# отрисовка игрового поля "Крестики-Нолики"
def showBoardXO(board: list, score_: list, last_turn=None):
    clear()
    print(f'{bc.WHITE}Игра {bc.BOLD}"{bc.RED}КРЕСТИКИ{bc.WHITE}-{bc.BLUE}НОЛИКИ{bc.WHITE}"{bc.END} \
{bc.WHITE}by {bc.BOLD}Yoda{bc.RED}XD{bc.END}')
    print(f'{bc.ORANGE}{bc.UNDERLINE}Игрок: {score_[0]}{bc.END}    \
{bc.ORANGE}{bc.UNDERLINE}Ничья:{score_[2]}{bc.END}    \
{bc.ORANGE}{bc.UNDERLINE}Бот: {score_[1]}{bc.END}')
    print()
    for i in range(len(board)):
        string_ = (' ' * board_indent + ' ') + ' │ '.join(board[i]) + ' '
        coloringAndPrint(string_)
        if i in (0, 1):
            print(f'{bc.WHITE}{" " * board_indent}───┼───┼───{bc.END}')
    print()
    if last_turn != None:
        print(last_turn)
# отрисовка игрового поля "Алики-Ордики"
def showBoardEgg(board: list, score_: list, last_turn=None):
    clear()
    print(f'{bc.WHITE}Игра {bc.BOLD}"{bc.BLUE}АЛИКИ{bc.WHITE}-{bc.RED}ОРДИКИ{bc.WHITE}"{bc.END} \
{bc.WHITE}by {bc.BOLD}Yoda{bc.RED}XD{bc.END}')
    print(f'{bc.ORANGE}{bc.UNDERLINE}Игрок: {score_[0]}{bc.END}    \
{bc.ORANGE}{bc.UNDERLINE}Ничья:{score_[2]}{bc.END}    \
{bc.ORANGE}{bc.UNDERLINE}Бот: {score_[1]}{bc.END}')
    print()
    for i in range(len(board)):
        string_ = (' ' * board_indent + ' ') + ' │ '.join(board[i]) + ' '
        coloringAndPrint(string_)
        if i in (0, 1):
            print(f'{bc.WHITE}{" " * board_indent}───┼───┼───{bc.END}')
    print()
    if last_turn != None:
        print(last_turn)
# вспомогательная функция для отрисовки игрового поля, раскрашивает символы
def coloringAndPrint(text: str):
    num_set = set(str(x) for x in range(1, 10))
    for c in text:
            if c in num_set:
                cur_color = bc.GREEN
            elif c in ('X', 'H'):
                cur_color = bc.RED
            elif c in ('O', 'A'):
                cur_color = bc.BLUE
            else:
                cur_color = bc.END
            print(f"{cur_color}{c}{bc.END}", end='')
    print(f'{bc.END}')
# транскриптор координат
def numToCoord(n: str) -> list:
    if 1 <= n <= 9:
        x = (n - 1) // 3
        y = (n - 1) % 3
        return x, y
    else:
        raise ValueError('numToCoord в качестве аргументов принимает число от 1 до 9.')
# изменение и возврат счета, возврат строки с победителем
def check_winner(score_: list, p1_sign_: str, bot_sign_: str, winner_sign: str):
    if winner_sign == p1_sign_:
        score_[0] += 1
        return (score_, 'Игрок победил!')
    elif winner_sign == bot_sign_:
        score_[1] += 1
        return (score_, 'Железяка победила!')
    elif winner_sign == 'Draw':
        score_[2] += 1
        return (score_, 'Ничья!')
    else:
        return (score_, '')
# проверка конца игры, возврат победителя
def game_over_check(board: list):
    # проверка победителя в \ диагонали
    diag_set_1 = set(board[x][x] for x in range(len(board)))
    if len(diag_set_1) == 1:
        return board[0][0]
    # проверка победителя в | диагонали
    diag_set_2 = set(board[-x-1][x] for x in range(len(board)))
    if len(diag_set_2) == 1:
        return board[-1][0]
    # проверка победителя в строках
    for i in range(len(board)):
        if len(set(board[i])) == 1:
            return board[i][0]
        # проверка победителя в столбцах
        col_set = set()
        for j in range(len(board)):
            col_set.add(board[j][i])
        if len(col_set) == 1:
            return board[j][i]
    # проверка ничьей
    desk_set = set()
    num_set = set(str(x) for x in range(1, 10))
    for item in board:
        row_set  = set(item)
        desk_set.update(row_set)
    if not desk_set.intersection(num_set):
        return 'Draw'
    return None
# получение возможных ходов
def getPossibleTurns(board_: list) -> tuple:
    return tuple((i, j) for i in range(len(board_)) for j in range(len(board_[i])) if board_[i][j].isdigit())
# получение выигрышных ходов
def getWinnableTurns(board_: list, p1_sign_: str, bot_sign_: str, for_who: str) -> list:
    player_winnable_turns = []
    if for_who == 'p1':
        s1 = p1_sign_
        s2 = bot_sign_
    elif for_who == 'bot':
        s1 = bot_sign_
        s2 = p1_sign_
    # проверка выигрышных позиций игрока в строках
    for i in range(len(board_)):
        row = board_[i]
        if row.count(s1) == 2 and row.count(s2) != 1:
            pos = [x for x in row if x.isdigit()][0] # поиск свободной клетки
            assert len(pos) == 1, 'pos больше 1'
            pos = row.index(pos)
            player_winnable_turns.append((i, pos))
    # проверка выигрышных позиций игрока в столбцах
    for i in range(len(board_)):
        col = []
        for j in range(len(board_[i])):
            col.append(board_[j][i])
        if col.count(s1) == 2 and col.count(s2) != 1:
            pos = [x for x in col if x.isdigit()][0] # поиск свободной клетки
            assert len(pos) == 1, 'pos больше 1'
            pos = col.index(pos)
            player_winnable_turns.append((pos, i))
    # проверка выигрышных позиций игрока в \ диагонали
    diag_1 = [board_[x][x] for x in range(len(board_))]
    if diag_1.count(s1) == 2 and diag_1.count(s2) != 1:
        pos = [x for x in diag_1 if x.isdigit()][0] # поиск свободной клетки
        assert len(pos) == 1, 'pos больше 1'
        pos = diag_1.index(pos)
        player_winnable_turns.append((pos, pos))
        print('diag1', (pos, pos))
    # проверка выигрышных позиций игрока в | диагонали
    diag_2 = [board_[-x-1][x] for x in range(len(board_))]
    if diag_2.count(s1) == 2 and diag_2.count(s2) != 1:
        pos = [x for x in diag_2 if x.isdigit()][0] # поиск свободной клетки
        assert len(pos) == 1, 'pos больше 1'
        pos = diag_2.index(pos)
        player_winnable_turns.append((-pos + len(board_) - 1, pos))
    
    return player_winnable_turns
# получение хода для бота
def get_bot_turn(board_: list, p1_sign_: str, bot_sign_: str, difficult_: str):
    possible_turns = getPossibleTurns(board_)
    player_winnable_turns = getWinnableTurns(board_, p1_sign_, bot_sign_, 'p1')
    bot_winnable_turns = getWinnableTurns(board_, p1_sign_, bot_sign_, 'bot')
    if difficult_ == 'Easy':
        bot_turn = choice(possible_turns)
        x, y = bot_turn
        return x, y
    elif difficult_ in ('Normal','Hard'):
        if bot_winnable_turns:
            bot_turn = choice(bot_winnable_turns)
            x, y = bot_turn
            return x, y
        elif player_winnable_turns:
            bot_turn = choice(player_winnable_turns)
            x, y = bot_turn
            return x, y
        elif difficult_ == 'Hard' and board_[1][1] == '5' and len(possible_turns) > 7:
            return 1, 1
        elif difficult_ == 'Hard' and \
            ((board_[0][0] and board_[2][2]) == p1_sign_ or (board_[0][2] and board_[2][0]) == p1_sign_):
                temp = choice([x for x in [board_[1][0], board_[0][1], board_[1][0], board_[1][1]] if x.isdigit()])
                return numToCoord(int(temp))
        elif difficult_ == 'Hard' and len(possible_turns) > 5:
            temp = choice([x for x in [board_[0][0], board_[0][2], board_[2][0], board_[2][2]] if x.isdigit()])
            return numToCoord(int(temp))
        else:
            bot_turn = choice(possible_turns)
            x, y = bot_turn
            return x, y
# получение хода для игрока
def get_player_turn(board_: list, p1_sign_: str):
    possible_turns = getPossibleTurns(board_)
    player_1_turn = input(f'Введи номер клетки на которую поставишь {cs[p1_sign_]} >: ').strip()
    if not player_1_turn.isdigit():
        print(f'{bc.ORANGE}Ты должен указать номер клетки для хода в виде цифры.{bc.END}')
        return None
    elif not (1 <= int(player_1_turn) <= 9):
        print(f'{bc.ORANGE}Ты указал несуществующую клетку для хода, введи номер свободной клетки.{bc.END}')
        return None
    else:
        x, y = numToCoord(int(player_1_turn))
        if (x, y) not in possible_turns:
            print(f'{bc.ORANGE}Ты указал уже занятую клетку, выбери другую.{bc.END}')
            return None
        else:
            return x, y