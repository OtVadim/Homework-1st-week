
one = str(input())
two = str(input())

def get_summ(one, two, delimiter = '&'):
    return one + ' ' + delimiter + ' ' + two


print(get_summ(one,two))
print(get_summ("learn".capitalize(),"python".capitalize()))
