#import Lab7.shootingmethod as sm
import Lab7.finite_difference_method as fd
import sys

#sm.VAR = 20
#sm.shootingmethod()
#fd.RS_Clear(16)

sys.stdout = open('output.txt', 'a')
j=8
for i in range (2,0,-1):
    while j<=32:
        fd.RS_Clear(j,20,i/10)
        fd.RS_NotClear(j,20,i/10)
        j*=2
    j=8
for i in range(2, 0, -1):
    while j<=32:
        fd.RS_Clear(j, 24, i/10)
        fd.RS_NotClear(j,24,i/10)
        j *= 2
    j=8
sys.stdout.close()
