
def boxstar(rows):
    for i in range(rows):
        print("*"*rows)
    print("\n")

def increasingStars(rows):
    for i in range(rows+1):
        print("*"*i)
    print("\n")

def numberTriangle_1(rows):
    string=""
    for i in range(rows):
        string=string+str(i+1)
        print(string)
    print("\n")


def numberTriangle_2(rows):
    for i in range(rows+1):
        print(str(i)*i)
    print("\n")

def invertedStars(rows):
    for i in range(rows):
        print("*"*(rows-i))
    print("\n")

def inverted_numberTriange_1(rows):
    string=""
    for i in range(rows):
        for j in range (rows-i):
            string=string+str(j+1)+" "
        print(string)
        string=""
    # for i in range(rows):
    #     string=string+str(i+1)
    # for i in range(len(string)):
    #     print((string))
    #     string=int(string)/int(10
    print("\n")

def TriangleStars(rows):
    for i in range(rows):
        print(" "+" "*(rows-(i+1))+"*"*((2*(i+1))-1)+" "*(rows-(i+1))+" ")
    print("\n")

def UpsidedownTriangleStars(rows):
    for i in range(rows):
        print(""+" "*((i+1))+"*"*(2*(rows-i)-1)+""*((i+1))+"")
    print("\n")


def diamond(rows):
    for i in range(rows):
        print((" "+" "*(rows-(i+1))+"*"*((2*(i+1))-1)+" "*(rows-(i+1))+" "))
    for i in range(rows):
        print(""+" "*((i+1))+"*"*(2*(rows-i)-1)+""*((i+1))+"")    
    print("\n")

def halfdiamond(rows):
    for i in range(rows):
        print("*"*(i))
    for i in range(rows):
        print("*"*(rows-i))    
    print("\n")

def binarytriangle(rows):
    string=""
    for i in range (rows):
        if i%2==0:
            string="1 "+string
        else:
            string="0 "+string
        print(string)
    print("\n")
        
def numtriangle(rows):
    string1=""
    string2=""
    string3=""
    for i in range(rows):
        string1=string1+str(i+1)
        string2=" "*(2*(rows-i)-1)
        string3=str(i+1)+string3
        print(string1+string2+string3)
    print("\n")

def ascendingtriange(rows):
    count = 0
    for i in range(rows+1):
        string=""
        for j in range(i):
            count+=1
            string=string+str(count)+" "
        print(string)    


def alphatriangle(rows):
    for i in range(rows):
       charecter=chr(ord("A")+i)
       print(charecter*(i+1))


def alphatriangle_1(rows):
    charecter=""
    for i in range(rows):
       charecter=charecter+chr(ord("A")+i)
       print(charecter)

def inveredalpha(rows):
    charecter=""
    for i in range(rows+1):
       print(charecter)
       charecter=""
       for j in range(rows-i):
        charecter=charecter+chr(ord('A')+j)+" "
        
    
    
    
        



# def UpsidedownTriangleStar(rows):
#     for i in range(rows):
#         print((" "+"*"*(rows-(i+1))+" "*((2*(i+1))-1)+"*"*(rows-(i+1))+" "))
#     for i in range(rows):
#         print(""+"*"*((i+1))+" "*(2*(rows-i)-1)+"*"*((i+1))+"") 
#     print("\n")  

if __name__ == '__main__':
    pattern_1 = boxstar(5)
    pattern_2= increasingStars(5)
    pattern_3=numberTriangle_1(5)
    pattern_4= numberTriangle_2(5)
    pattern_5=invertedStars(5)
    pattern_6=inverted_numberTriange_1(10)
    pattern_7=TriangleStars(5)
    pattern_8=UpsidedownTriangleStars(5)
    pattern_9=diamond(5)
    pattern_10=halfdiamond(5)
    pattern_11=binarytriangle(5)
    pattern_12=numtriangle(5)
    pattern_13=alphatriangle(5)
    pattern_14=alphatriangle_1(5)
    pattern_15=ascendingtriange(5)
    pattern_16=inveredalpha(5)
