a=356 # известное стороны A
b=29 # известное стороны B
ka=5 # секретное стороны A
kb=6 # секретное стороны B
aSends = (b**ka)%a #вычисляем и отправляем B
bComputes = (aSends**kb)%a #вычисляем полученное от A
bSends = (b**kb)%a # B отправляем полученное число A
aComputes = (bSends**ka)%a # Вычисляем полученное от B
print ("A отправляет: {}".format(aSends))
print ("B вычисляем: {}".format(bComputes))
print ("B отправляет: {}".format(bSends))
print ("A вычисляет: {}".format(aComputes))
print ("Общее число: {}".format((b**(ka*kb))%a))