import os, sys

def main():
    try:
        #os.system('sudo apt update && sudo apt upgrade -y')
        #os.system('sudo apt install git supervisor -y')
        #os.system('source .venv/bin/activate')
        #os.system('pip install -r requirements.txt')
        if sys.argv[1] == '-a':
            #setting avito.ru monitor
            pass
        elif sys.argv[1] == '-u':
            #setting auto.ru monitor
            pass
        elif sys.argv[1] == '-d':
            #setting drom.ru monitor
            pass
        elif sys.argv[1] == '-y':
            #setting youla.ru monitor
            pass
        else:
            print('Неизвестный параметр - ', sys.argv[1])
    except:
        print('fail')
    

if __name__ == '__main__':
    main()
