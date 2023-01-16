from logic import *
from time import sleep
clear() # очистка консоли перед началом

# рабочие переменные
board = make_board()
score = [0, 0, 0] # [player_score, draw_score, bot_score]
# параметры #################################
player_error_showing_delay = 2 # задержка отображения ошибок ввода игрока
bot_thinking_delay = 2 # задержка эмуляции думающего бота
# выбор игры
game_type_list = ['[Крестики-Нолики]', '[Алики-Ордики]']
for n, t in enumerate(game_type_list, start=1):
    print(f'{n}. {t}')
showBoardChoise = int(input('Выбери режим игры >: ')) - 1
showBoard = [showBoardXO, showBoardEgg][showBoardChoise]
# выбор сложности
showBoard(board, score)
difficult_list = ['Easy', 'Normal', 'Hard']
for n, d in enumerate(difficult_list, start=1):
    print(f'{n}. {d}')
difficult_choise = int(input('Выбери сложность >: ')) - 1
difficult = difficult_list[difficult_choise]
# выбор стороны
showBoard(board, score)
if showBoardChoise == 0:
    sings_list1 = ['X', 'O']
    sings_list2 = ['за Крестики', 'за Нолики']
    sings_list_c = [cs['X'], cs['O']]
elif showBoardChoise == 1:
    sings_list1 = ['A', 'H']
    sings_list2 = ['за Альянс!', 'за Орду!']
    sings_list_c = [cs['A'], cs['H']]
for i in range(2):
    print(f'{i + 1}. {sings_list_c[i]} - {sings_list2[i]}')
sign_choise = int(input('Выбери за кого играть >: ')) - 1
p1_sign = sings_list1[sign_choise]
bot_sign = sings_list1[sign_choise - 1]
# выбор первого хода
showBoard(board, score)
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
            player_turn = None
            while not player_turn:
                showBoard(board, score, last_turn)
                player_turn = get_player_turn(board, p1_sign)
                if not player_turn:
                    sleep(player_error_showing_delay)
            else:
                p1_x, p1_y = player_turn
                board[p1_x][p1_y] = p1_sign
                last_turn = f'{bc.RED}Игрок{bc.END} поставил {sings_list_c[sign_choise]} на {(3 * p1_x) + p1_y + 1} клетку!'
            # проверка конца игры после хода игрока 
            if game_over_check(board):
                score, winner = check_winner(score, p1_sign, bot_sign, game_over_check(board))
                break
            # ход бота
            showBoard(board, score, last_turn)
            print('Железяка думает над ходом...')
            sleep(bot_thinking_delay)
            bot_x, bot_y = get_bot_turn(board, p1_sign, bot_sign, difficult)
            board[bot_x][bot_y] = bot_sign
            last_turn = f'{bc.BLUE}Железяка{bc.END} поставила {sings_list_c[sign_choise - 1]} на {(3 * bot_x) + bot_y + 1} клетку!'
            # проверка конца игры после хода бота
            if game_over_check(board):
                score, winner = check_winner(score, p1_sign, bot_sign, game_over_check(board))
                break
    # бот ходит первым
    else:
        while True:
            # ход бота
            showBoard(board, score, last_turn)
            print('Железяка думает над ходом...')
            sleep(bot_thinking_delay)
            bot_x, bot_y = get_bot_turn(board, p1_sign, bot_sign, difficult)
            board[bot_x][bot_y] = bot_sign
            last_turn = f'{bc.BLUE}Железяка{bc.END} поставила {sings_list_c[sign_choise - 1]} на {(3 * bot_x) + bot_y + 1} клетку!'
            # проверка конца игры после хода бота
            if game_over_check(board):
                score, winner = check_winner(score, p1_sign, bot_sign, game_over_check(board))
                break
            # ход игрока
            player_turn = None
            while not player_turn:
                showBoard(board, score, last_turn)
                player_turn = get_player_turn(board, p1_sign)
                if not player_turn:
                    sleep(player_error_showing_delay)
            else:
                p1_x, p1_y = player_turn
                board[p1_x][p1_y] = p1_sign
                last_turn = f'{bc.RED}Игрок{bc.END} поставил {sings_list_c[sign_choise]} на {(3 * p1_x) + p1_y + 1} клетку!'
            # проверка конца игры после хода игрока
            if game_over_check(board):
                score, winer = check_winner(score, p1_sign, bot_sign, game_over_check(board))
                break
    # рестарт игры с таймером
    for i in range(3, 0, -1):
        showBoard(board, score, last_turn)
        print(f'{bc.BOLD}{bc.PURPLE}{winner}{bc.END}')
        print(f'Новая игра через {i}... ')
        sleep(1)