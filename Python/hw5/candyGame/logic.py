from random import randint

def get_total_candys(min_candys: int, rnd_gen_max: int = None):
    if rnd_gen_max != None:
        if rnd_gen_max > min_candys:
            total_candys = randint(min_candys + 1, rnd_gen_max)
        else:
            raise ValueError('ОШИБКА: аргумент rnd_gen_max не может быть меньше min_candys.')
    else:
        while True:
            try:
                total_candys: int = int(input(f'Введите количество конфет на столе (не менее {min_candys} конфет) >: '))
                if total_candys > min_candys:
                    break
                else:
                    print(f'ОШИБКА: На столе должно быть не менее {min_candys} конфет.')
            except:
                print('ОШИБКА: Введено некорректное значение, количество конфет должно быть целым положительным числом.')
    print(f'Итак, на столе {total_candys} конфет.')
    return total_candys

def get_player_step(max_step: int):
    while True:
        try:
            step = int(input('Сколько конфет берешь? >: '))
            if 1 <= step <= max_step:
                break
            else:
                print(f'ОШИБКА: Ты можешь брать не менее 1 и не более {max_step} конфет.')
        except:
            print('ОШИБКА: Введено некорректное значение, количество забираемых конфет должно быть числом.')
    return step

def get_pc_step(max_step: int, total: int):
    step = total % (max_step + 1)
    if step == 0:
        step = 1
    return step

def game_over(player: str, last_step: int, total: int):
    if total <= 0:
        print(f'{player.capitalize()} забрал последние {last_step} конфеты, {player.lower()} победил!')
        return True
    else:
        print(f'{player.capitalize()} забрал {last_step} конфет, на столе осталось {total} конфет.')
        return False