class bcolors:
    PURPLE = '\033[95m'
    WHITE = '\033[97m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
csigns = {
    'X': f'{bcolors.RED}X{bcolors.END}',
    'O': f'{bcolors.BLUE}O{bcolors.END}',
    'A': f'{bcolors.BLUE}A{bcolors.END}',
    'H': f'{bcolors.RED}H{bcolors.END}',
}