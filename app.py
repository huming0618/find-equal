import sys

def find(input, limit, all=False):
    result = []
    max = limit + 1
    for m in range(max):
        for n in range(max):
            if m - n == input:
                if not all:
                    check = [x for x in result if (x[0]==m and x[1]==n and x[2]=='-') or (x[0]==n and x[1]==m and x[2]=='-')]
                    if len(check) == 0:
                        result.append([m,n,'-'])
                        print("{}-{}={}".format(m,n,input))
                else:
                    result.append([m,n,'-'])
                    print("{}-{}={}".format(m,n,input))
            if m + n == input:
                if not all:
                    check = [x for x in result if (x[0]==m and x[1]==n and x[2]=='+') or (x[0]==n and x[1]==m and x[2]=='+')]
                    if len(check) == 0:
                        result.append([m,n,'+'])
                        print("{}+{}={}".format(m,n,input))
                else:
                    result.append([m,n,'+'])
                    print("{}+{}={}".format(m,n,input))

    print('--------size-----------')
    print(len(result))


if __name__ == '__main__':
    #python3 app.py 3 10 all
    input = sys.argv[1]
    limit = sys.argv[2]
    all = False 
    if len(sys.argv) > 3:
        all = sys.argv[3] == 'all'
    find(int(input), int(limit), all)