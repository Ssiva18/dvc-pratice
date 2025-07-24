# Nesting if else statements become quite unmanagable,
# guard clause pattern is going to simplify our code.

DirectionFirst = 'North'
DirectionSecond = 'South'
DirectionThird = 'East'
DirectionFourth = 'West'

def classification():

    if not DirectionFirst == 'North':
        print(f'The path choosed to walk is not {DirectionFirst}.')
        return
    
    if not DirectionSecond == 'South':
        print(f'The path choosed to walk is not {DirectionSecond}.')
        return
    
    if not DirectionThird == 'East':
        print(f'The path choosed to walk is not {DirectionThird}.')
        return
    
    if not DirectionFourth == 'West':
        print(f'The path choosed to walk is not {DirectionFourth}.')
        return
    
    print("you have reached the destination")


from argparse import ArgumentParser,Namespace

parser = ArgumentParser()

parser.add_argument('value')
parser.add_argument('value1')

args: Namespace = parser.parse_args()

if args.value == 'siva':
    print(args.value1)









if __name__ == "__main__":
    print(classification())

