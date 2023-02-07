import random
import numpy as np

'''
  Memo about cards definition
  Prepare  0-52  Number
  Use  zip()  to make pare of  mark and number??
   0-12  ♡
  13-25  ♦
  26-38  ♣
  39-51  ♠         (mod 13) + 1    is the Card's Number
'''


# Prepare Cards (52 Cards)
random_list = list(range(0,52))

# 20 Cards Choice ( Including exchange cards )
Selected_cards = random.sample(random_list , 20)

# Divid list into 4 parts
Split_list = list( np.array_split( Selected_cards , 4) )

Pre_Player_cards  =  Split_list[0] 
Pre_COM_cards     =  Split_list[1] 
Player_change     =  Split_list[2]
COM_change        =  Split_list[3]

Pre_Player_cards.sort()
Pre_COM_cards.sort()

#  Preparation of cards is finished
def Card(n):
    if n%13==12:
        K = 'K'

    elif n%13==11:
        K = 'Q'

    elif n%13==10:
        K = 'J'

    elif n%13==0:
        K = 'A'
        
    else:
        K = (n%13) + 1

    if n//13==0:
        S= '♡' + str(K)

    elif n//13==1:
        S= '♦' + str(K)

    elif n//13==2:
        S= '♣' + str(K)

    else:
        S= '♠' + str(K)

    return S
