from enum import Enum

class Direction(Enum):
    right = 1
    left = 0

def move (direction):
    # if direction != right or direction != left :
    #     raise ValueError ('Cannot move in this direction')

    if not isinstance(direction, Direction):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'

if __name__ == '__main__':
    # print(move('rigth'))
    
    print(move(Direction.right))
    print(move(Direction.left))


