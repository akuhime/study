import string

def main():
    with open("input.txt") as f:
        k = int(f.readline())
        s = f.readline()
    n = len(s)
    alph = string.ascii_lowercase
    res = 0 
    for letter in alph:
        print(letter)
        f = 0
        b = 0
        c = k
        letres = 0
        maxletres = 0
        while f!=n:
            if (maxletres >= (n - f)) or (b==n):
                break 
            while c!=0 and b!=n:
                if s[b] != letter:
                    c -= 1
                letres += 1
                b += 1
                #print('ku, b = ', b)
            while b!=n:
                if s[b] != letter:
                    break
                letres += 1
                b += 1
                #print('kuku, b = ', b)
            #print('f = ', f, 'b = ', b, 'letres = ', letres)
            if maxletres < letres:
                maxletres = letres
            letres -= 1
            if s[f] != letter:
                c+=1
            f += 1
        if maxletres > res:
            res = maxletres
    print(res)

main()