n = [n for n in range(16)]
 
def py_logo(x):
    for row in range(15):
        for col in range(16):

            if (row==0 and col in n[5:10]) or (row==1 and col in n[4:6]+n[7:11]) or (row==2 and col in n[4:11]) or (row==3 and col in n[7:11]) or (row==4 and col in n[1:11]) or (row==5 and col in n[:11]) or (row==6 and col in n[:10]) or (row in n[7:10] and col in n[:4]) or (row==10 and col in n[1:4]):
        
                print(x[0],end=" ")

            elif (row==4 and col in n[12:15]) or (row in n[5:8] and col in n[12:]) or (row==8 and col in n[6:]) or (row==9 and col in n[5:]) or (row==10 and col in n[5:15]) or (row==11 and col in n[5:9]) or (row==12 and col in n[5:12]) or (row==13 and col in n[5:9]+n[10:12]) or (row==14 and col in n[6:11]):
        
                print(x[1],end=" ")
            
            else:
        
                print(end="  ")
        print()
        
py_logo((__import__('random').choice(['0', '#', '#'])+(__import__('random').choice(['*', '.', '*', '@']))))