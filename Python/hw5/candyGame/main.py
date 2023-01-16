from logic import get_total_candys, get_player_step, get_pc_step, game_over
from os import system
system('cls')
# параметры игры
max_step = 28
max_candys = 100
# total = 30 # ручное указание стартового кол-ва конфет на столе
total = get_total_candys(max_step, max_candys) # рандомное указание стартового кол-ва конфет на столе

round_counter = 1
while True:
    print(f'Раунд {round_counter}. На столе {total} конфет.')

    player_step = get_player_step(max_step)
    total -= player_step
    if game_over('ИГРОК', player_step, total):
        break
    
    pc_step = get_pc_step(max_step, total)
    total -= pc_step
    if game_over('КОМПЬЮТЕР', pc_step, total):
        break
    
    round_counter += 1
    print('='*64)
print('ИГРА ОКОНЧЕНА!')