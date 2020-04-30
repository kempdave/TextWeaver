import sys

def hello_world():
    print('hello world')

def default():
    print ('running normally')

def main():
    if sys.argv[0] == 'hello':
        hello_world()
    else:
        default()


if __name__ == '__main__':
    main()