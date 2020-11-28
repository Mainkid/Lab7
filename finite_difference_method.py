import math

def d2F(t,x,ksi,var):
    return 1+0.1*t*var*math.cos(math.pi*x)*math.pi+0.1*ksi*math.pi*math.pi*t*var*math.sin(math.pi*x)

def F(t,x,var):
    return x+0.1*t*math.sin(math.pi*x)*var

def findDelta(l,t,h,N,var):
    max=0
    for i in range (N+1):
        if (abs(l[i]-F(t,h*i,var))>max):
            max=abs(l[i]-F(t,h*i,var))
    return max

def printHead(N):
    print(f'{"t":7}|\t{"delta":13}|\t{"x:":2}\t', end="")
    for i in range (0, N+1):
        print(str(1*i/N)+f'{"":15}|\t',end="")
    print()

def printBody(v1,v2,v3,N):
    print(str(v1)+f'{"":10}|\t',end="")
    print(str(v2) + f'{"":10}|\t', end="")
    for i in range (0, N+1):
        print(str(v3[i])+f'{"":10}|\t',end="")
    print()

def FormAnswer(delta):
    print("Del_t= "+str(delta))
    print()

def generateList(N):
    list1=[]
    for i in range(N+1):
        list1.append(i/N)
    return list1


def Solve(N):
    RS_Clear(N)
    RS_NotClear(N)
    return 0

def Find_u(f,Arr,N,h):

    alpha=[0]*(N-1)
    beta=[0]*(N-1)
    alpha[1]=-Arr[0][1]/Arr[0][0]
    beta[1]=f[0]/Arr[0][0]

    n=N-1
    xAnswer= [0]*n
    # print(Arr)
    for i in range (1, n-1):
        alpha[i+1]=-Arr[i][i+1]/(Arr[i][i]+Arr[i][i-1]*alpha[i])
        beta[i+1]=(f[i]-Arr[i][i-1]*beta[i])/(Arr[i][i]+Arr[i][i-1]*alpha[i])


    xAnswer[n-1]=(f[n-1]-Arr[n-1][n-2]*beta[n-1])/(Arr[n-1][n-1]+Arr[n-1][n-2]*alpha[n-1])
    for i in range (n-2,-1,-1):
        xAnswer[i]=alpha[i+1]*xAnswer[i+1]+beta[i+1]

    return xAnswer

def RS_Clear(N,var,ksi):
    print("N= " + N)
    A=0
    B=1
    printHead(N)
    h = 1 / N
    tau = h * h / (4 * ksi)
    resList = generateList(N)
    delta=0
    i=1
    t=0
    while (i * tau<1):
        #t = i * tau
        newStr=[0 for _ in range(0,N+1)]
        newStr[0]=A
        newStr[N]=B
        for j in range(1,N):
            newStr[j]=resList[j]+tau*ksi*(resList[j+1]-2*resList[j]+resList[j-1])/(h**2)+tau*d2F(tau*(i-1), h*j,ksi,var)
        resList= newStr
        delta=findDelta(newStr,tau*i,h,N,var)
        printBody(i*tau, delta, newStr, N)
        i+=1
        #ПЕРЕПСИЬСЬАИЬАЬИ
    FormAnswer(delta)


def RS_NotClear(N,var,ksi):
    print("N= " +str( N))

    A = 0
    B = 1
    printHead(N)
    h = 1 / N
    tau = h
    resList = generateList(N)
    for i in range(0, N - 1):
        resList[i] = h * i
    resList[0] = 0
    resList[N] = 1
    delta = 0
    i = 1
    t = 0
    f = [0] * (N - 1)
    d= (tau*ksi)/(h**2)
    maxdelta=0
    Arr = [0] * (N - 1)

    for i in range(N - 1):
        Arr[i] = [0] * (N - 1)
    Arr[0][0] = (1 + 2 * d)
    Arr[0][1] = -d
    Arr[N - 2][N - 3] = -d
    Arr[N - 2][N - 2] = (1 + 2 * d)
    step = 0

    for i in range(1, N - 2):
        Arr[i][step] = -d
        Arr[i][step + 1] = (1 + 2 * d)
        Arr[i][step + 2] = -d
        step += 1
    i = 1
    while (i * tau<=1):
        for q in range(0, N - 1):
            f[q] = resList[q + 1] + tau * d2F((i) * tau, h * (q + 1),ksi,var)
        f[N - 2] += d * B
        f[0] += d * A
        f= Find_u(f,Arr,N,h)


        for j in range(0,N-1):
            resList[j+1]=f[j]
            #print(resList)
        delta=findDelta(resList,i*tau,h,N,var)
        if (delta>maxdelta):
            maxdelta=delta
        printBody(i * tau, delta, resList, N)
        i += 1
    print()
    FormAnswer(maxdelta)