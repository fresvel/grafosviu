import sys

from grafoviu.arista import Arista

def main():
    print("Bienvenido a grafoviu!")
    arista=Arista("a","b",1)
    print(arista)

if __name__ == "__main__":
    sys.exit(main())