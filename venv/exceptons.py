#itemsInCart = 1
#if itemsInCart!=2:
#    #raise Exception("hey you have given the wrong input")
#assert(itemsInCart == 2)

try:
    with open('testlogger.txt', 'r') as reader:
        reader.read()
except Exception as a:
    print(a)

