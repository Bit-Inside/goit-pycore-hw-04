
import sys
from pathlib import Path
from colorama import init, Fore

init()

def print_structure(path: Path, prefix=''):
    for item in path.iterdir():
        if item.is_dir():
            print(prefix + Fore.BLUE + item.name + '/' + Fore.RESET)
            print_structure(item, prefix + '    ')
        else:
            print(prefix + Fore.GREEN + item.name + Fore.RESET)

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії")
        return
    
    path = Path(sys.argv[1])
    if not path.exists() or not path.is_dir():
        print("Невірний шлях або це не директорія")
        return

    print_structure(path)

if __name__ == "__main__":
    main()