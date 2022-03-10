#Calculating gregorian shit
import sys
def easter_date(Y):
    if Y < 1583:
        raise ValueError
    a=Y%19
    b =Y%4
    c =Y%7
    k =(Y//100)
    p =(13+(8*k))//25
    q =(k//4)
    m =(15-p+k-q)%30
    n =(4+k-q)%7
    d =(19*a+m)%30
    e =((2*b)+(4*c)+(6*d)+n)%7
    r = 22+d+e
    s =d+e-9
    
    if d ==29 and e == 6 and s == 26:
       return "April 19"
    elif d == 28 and e == 6 and ((11*m)+11)%30 < 19 and s == 25:
        return "April 18"
    elif s>0:
        return "April " + str(s)
    else:
        return "March " + str(r)        
    
if __name__ == "__main__":
    try:
        year = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a year as a command-line argument")
    except ValueError:
        sys.exit("could not convert", sys.argv[1], "into an integer")
    print(easter_date(year))