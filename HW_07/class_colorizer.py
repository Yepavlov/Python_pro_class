class colorizer:
    def __init__(self, color: str):
        self.color = color

    def __enter__(self):
        if self.color == 'red':
            print('\033[1m\033[91m', end='')
        elif self.color == 'green':
            print('\033[1m\033[92m', end='')
        elif self.color == 'yellow':
            print('\033[1m\033[93m', end='')
        elif self.color == 'blue':
            print('\033[1m\033[94m', end='')
        elif self.color == 'purple':
            print('\033[1m\033[95m', end='')
        elif self.color == 'cyan':
            print('\033[1m\033[96m', end='')
        elif self.color == 'white':
            print('\033[1m\033[97m', end='')

    def __exit__(self, exc_type, exc_value, traceback):
        print('\033[0m', end='')


print('Text in default color')
with colorizer('red'):
    print('This text is in red')
with colorizer('green'):
    print('This text is in green')
with colorizer('yellow'):
    print('This text is in yellow')
with colorizer('blue'):
    print('This text is in blue')
with colorizer('purple'):
    print('This text is in purple')
with colorizer('cyan'):
    print('This text is in cyan')
with colorizer('white'):
    print('This text is in white')
print('Back to default color')
