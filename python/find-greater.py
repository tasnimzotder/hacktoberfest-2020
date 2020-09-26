# Finf the greater number

def find_greater(x, y):
    # Todo: Write a function to return greater number
    return x if x > y else y

x = int(input())
y = int(input())

print('Greater Number: {}'.format(find_greater(x, y)))
