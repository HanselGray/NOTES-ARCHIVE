ans = 0
for a in range(1,6):
    for b in range(1,6):
        for c in range(1,20):
            for d in range(1,12):
                if (a+b == 6) and (2*a + 4*b+ 3*c + 5*d == 60): ans = ans +1 

print(ans)