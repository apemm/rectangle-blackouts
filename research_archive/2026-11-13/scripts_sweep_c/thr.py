def W(h): return (h-1)**2//4+1
for name,f in [("64p-4(A-1) > 2W_h+1", lambda h: 64*(40*h+1)-4*((h+1)//2-1) > 2*W(h)+1),
               ("64*40h > 2W_h+1", lambda h: 64*40*h > 2*W(h)+1),
               ("64p > 2W_h", lambda h: 64*(40*h+1) > 2*W(h))]:
    h=100
    while f(h): h+=1
    print(name, "first failure at h =", h)
