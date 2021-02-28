itemsInCart = 0

# 2 items will be added to cart

if itemsInCart != 2:
    pass # raise Exception("There is not enough item in your cart")

assert(itemsInCart == 0)


# try, catch

try:
    with open('.\\OOP\\filelog.txt', 'r') as reader:
        reader.read()

except:
    print('File not found')

try:
    with open('.\\OOP\\filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)


# 'finally' will always execute even if there was an error that occured
finally:
    print("cleaning up resources")

