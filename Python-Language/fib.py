while True:
    x:int = 0
    y = 1
    while x < 255:
        print("{}\n".format(x))
        
        z = x + y
        x = y
        y = z
        
