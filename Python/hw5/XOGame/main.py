from logic import *
clear() # очистка консоли перед началом

# рабочие переменные
board = make_board() # игровое поле 3х3
score = [0, 0, 0] # [player_score, draw_score, bot_score]
# параметры #################################
error_delay = 1 # задержка отображения ошибок ввода игрока
bot_delay = 1 # задержка эмуляции думающего бота
# выбор игры
gamemode_list = ['[Крестики-Нолики]', '[Алики-Ордики]']
for n, t in enumerate(gamemode_list, start=1):
    print(f'{n}. {t}')
gamemode = int(input('Выбери режим игры >: '))
# выбор сложности
showBoard(gamemode, board, score)
difficult_list = ['Easy', 'Normal', 'Hard']
for n, d in enumerate(difficult_list, start=1):
    print(f'{n}. {d}')
difficult_choise = int(input('Выбери сложность >: ')) - 1
difficult = difficult_list[difficult_choise]
# выбор стороны
showBoard(gamemode, board, score)
if gamemode == 1:
    sings_list1 = ['X', 'O']
    sings_list2 = ['за Крестики', 'за Нолики']
    sings_list_c = [cs['X'], cs['O']]
elif gamemode == 2:
    sings_list1 = ['A', 'H']
    sings_list2 = ['за Альянс!', 'за Орду!']
    sings_list_c = [cs['A'], cs['H']]
for i in range(2):
    print(f'{i + 1}. {sings_list_c[i]} - {sings_list2[i]}')
sign_choise = int(input('Выбери за кого играть >: ')) - 1
p1_sign = sings_list1[sign_choise]
bot_sign = sings_list1[sign_choise - 1]
# выбор первого хода
showBoard(gamemode, board, score)
start_list = ['Игрок', 'Бот']
for n, s in  enumerate(start_list, start=1):
    print(f'{n}. {s}')
start_choise = int(input('Выбери кто будет первым ходить >: ')) - 1
player_start = not bool(start_choise)
#############################################
# главный цикл
while True:
    # обновление переменных перед новой игрой
    board = make_board()
    last_turn = None
    winner = None
    # игрок ходит первым
    if player_start:
        while True:
            # ход игрока
            p1_x, p1_y, last_turn = player_turn(gamemode, board, score, last_turn, p1_sign, error_delay)
            board[p1_x][p1_y] = p1_sign
            # проверка конца игры после хода игрока 
            winner_sign = game_over_check(board)
            if winner_sign:
                score, winner = get_winner(score, p1_sign, bot_sign, winner_sign)
                break
            # ход бота
            bot_x, bot_y, last_turn = bot_turn(gamemode, board, score, last_turn, p1_sign, bot_sign, difficult, bot_delay)
            board[bot_x][bot_y] = bot_sign
            # проверка конца игры после хода бота
            winner_sign = game_over_check(board)
            if winner_sign:
                score, winner = get_winner(score, p1_sign, bot_sign, winner_sign)
                break
    # бот ходит первым
    else:
        while True:
            # ход бота
            bot_x, bot_y, last_turn = bot_turn(gamemode, board, score, last_turn, p1_sign, bot_sign, difficult, bot_delay)
            board[bot_x][bot_y] = bot_sign
            # проверка конца игры после хода бота
            winner_sign = game_over_check(board)
            if winner_sign:
                score, winner = get_winner(score, p1_sign, bot_sign, winner_sign)
                break
            # ход игрока
            p1_x, p1_y, last_turn = player_turn(gamemode, board, score, last_turn, p1_sign, error_delay)
            board[p1_x][p1_y] = p1_sign
            # проверка конца игры после хода игрока
            winner_sign = game_over_check(board)
            if winner_sign:
                score, winner = get_winner(score, p1_sign, bot_sign, winner_sign)
                break
    # рестарт игры с таймером
    restart_timer(gamemode, board, score, last_turn, winner, 3)