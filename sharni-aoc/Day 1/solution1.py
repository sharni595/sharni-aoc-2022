def read_data():
    f = open('sample.txt', 'r')
    input = f.read().splitlines()
    data = [ int(x) for x in input ]
    # print(data)
    return data

data = read_data()

print(data)