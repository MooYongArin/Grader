def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True
def next_prime(N):
    i = N
    while True:
        i += 1
        if is_prime(i):
            return i
def next_twin_prime(N):
    i = N
    while True:
        i += 1
        if is_prime(i) and is_prime(i+2):
            return (i,i+2)
exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ