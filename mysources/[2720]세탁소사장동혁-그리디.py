n=int(input())
for i in range(n):
    c=int(input())    # 거스름돈 총액
    q=c//25      
    c=c%25            # 남은 거스름돈
    d=c//10
    c=c%10            # 남은 거스름돈
    n=c//5
    p=c%5             # 남은 거스름돈
    print(q,d,n,p)