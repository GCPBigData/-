import pandas as pd

def print_hi(name):
    print(f'{name}')

    φ = pd.read_csv("phi.txt")
    φstr = φ.to_string()
    print(φstr.count('0'))
    print(φstr.count('1'))
    print(φstr.count('2'))
    print(φstr.count('3'))
    print(φstr.count('4'))
    print(φstr.count('5'))
    print(φstr.count('6'))
    print(φstr.count('7'))
    print(φstr.count('8'))
    print(φstr.count('9'))

if __name__ == '__main__':
    print_hi('INICIANDO')

