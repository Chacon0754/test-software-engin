import sys

def hello(name: str) -> None:
    print(f" Hello {name}")

def main(*args):
    if len(sys.argv) < 2:
        print("Uso: python hello.py")
    
    name = sys.argv[1]
    hello(name)

if __name__ == "__main__":
    main()
