import random
steps=0
for i in range(100):
    #η λιστα τετραγωνο ειναι ενα νοητο3*3  τετραγωνο οπου το λεν 0 ειναι το πανω αριστερα το λεν 1 πανω μεση κλπ κλπ
    tetragwno=[0,-1,-2,-3,-4,-5,-6,-7,-8]
    mikra=[1,1,1,1,1,1,1,1,1]
    mik=len(mikra)
    mesea=[2,2,2,2,2,2,2,2,2]
    mes=len (mesea)
    megala=[3,3,3,3,3,3,3,3,3]
    meg=len(megala)
    win=False
    while win==False:
        megethos=random.choice([1,2,3])
        if megethos==1:
            spot=random.randint(0,8)
            if tetragwno[spot]!=1 :
                mikra.pop(0)
                tetragwno.pop(spot)
                tetragwno.insert(spot,1)
                if mik==0:
                   megethos=random.choice([2,3])
        elif megethos==2:
            spot=random.randint(0,8)
            if tetragwno[spot]!=2:
                mesea.pop(0)
                tetragwno.pop(spot)
                tetragwno.insert(spot,2)
                if mes==0:
                    megethos=random.choice([1,3])
        else:
            spot=random.randint(0,8)
            if tetragwno[spot] !=3:
                megala.pop(0)
                tetragwno.pop(spot)
                tetragwno.insert(spot,3)
                if meg==0:
                    megethos=random.randint(1,3)
             
        steps+=1
    #gia idia kai orizontia
        if tetragwno[0]==tetragwno[1]==tetragwno[2] or tetragwno[3]==tetragwno[4]==tetragwno[5] or tetragwno[6]==tetragwno[7]==tetragwno[8]:
            win=True
    #gia idia kai katheta
        elif tetragwno[0]==tetragwno[3]==tetragwno[6] or tetragwno[1]==tetragwno[4]==tetragwno[7] or tetragwno[2]==tetragwno[5]==tetragwno[8]:
            win=True
    #gia idia kai diagwnia
        elif tetragwno[0]==tetragwno[4]==tetragwno[8] or tetragwno[2]==tetragwno[4]==tetragwno[6]:
            win=True
    #gia auksousa kai orizontia
        elif tetragwno[0]==1 and tetragwno[1]==2 and tetragwno[2]==3 or tetragwno[0]==3 and tetragwno[1]==2 and tetragwno[2]==1:
            win=True
        elif tetragwno[3]==1 and tetragwno[4]==2 and tetragwno[5]==3 or tetragwno[3]==3 and tetragwno[4]==2 and tetragwno[5]==1:
            win=True
        elif tetragwno[6]==1 and tetragwno[7]==2 and tetragwno[8]==3 or tetragwno[6]==3 and tetragwno[7]==2 and tetragwno[8]==1:
            win=True
    #gia auksousa kai katheta
        elif tetragwno[0]==1 and tetragwno[3]==2 and tetragwno[6]==3 or tetragwno[0]==3 and tetragwno[3]==2 and tetragwno[6]==1:
            win=True
        elif tetragwno[1]==1 and tetragwno[4]==2 and tetragwno[7]==3 or tetragwno[1]==3 and tetragwno[4]==2 and tetragwno[7]==1:
            win=True
        elif tetragwno[2]==1 and tetragwno[5]==2 and tetragwno[8]==3 or tetragwno[2]==3 and tetragwno[5]==2 and tetragwno[8]==1:
            win=True
    #gia auksousa kai diagwnia
        elif tetragwno[0]==1 and tetragwno[4]==2 and tetragwno[8]==3 or tetragwno[0]==3 and tetragwno[4]==2 and tetragwno[8]==1:
            win=True
        elif tetragwno[2]==1 and tetragwno[4]==2 and tetragwno[6]==3 or tetragwno[2]==3 and tetragwno[4]==2 and tetragwno[6]==1:
            win=True
        else:
            win=False
mo=steps/100
print(mo)




        
