
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

def UpsidedownTriangleStar(rows):
    for i in range(rows):
        print((" "+"*"*(rows-(i+1))+" "*((2*(i+1))-1)+"*"*(rows-(i+1))+" "))
    for i in range(rows):
        print(""+"*"*((i+1))+" "*(2*(rows-i)-1)+"*"*((i+1))+"") 
    print("\n")  

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
    pattern_11=UpsidedownTriangleStar(5)

