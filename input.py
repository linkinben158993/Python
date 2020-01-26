def inputpl(player):
    x = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    y = {'1':0,'2':1,'3':2,'4':3,'5':6,'6':5,'7':6,'8':7}
    keyx = ""
    #while True:
    if player == 'W':
        inx = input("Player W:")
        return [x[inx[0]],y[inx[1]]]
    else:
        inx = input("Player B:")
        return [x[inx[0]],y[inx[1]]]
