# sanity exploration: saturated boards under the 45-degree SQUARE constraints only (vertical/horizontal diagonals).
# (S)  a tilted square with a vertical diagonal on rows rho<sigma of different parts and horizontal diagonal
#      (x-k,y),(x+k,y): the two horizontal-diagonal cells are not both black (any column x in the board);
#      if column x is the owner then neither is black when both are in the board.
# (S') if column x has rows {y-k,y+k} then columns x-k and x+k (both in board) share no black row.
import sys, itertools, time
def count(h, A, tl=20):
    B=[r for r in range(1,h+1) if r not in A]
    part={r:0 for r in A}; part.update({r:1 for r in B})
    pairs=[(min(r,s),max(r,s)) for r in A for s in B]
    q=len(pairs)
    t0=time.time()
    cols=[]; used=set()
    found=[0]; ex=[]
    maxd=[0]
    def ok(c):
        # full check of the partial board (columns 1..c known), constraints whose cells all lie in 1..c
        rows=cols
        for x in range(1,c+1):
            r,s=rows[x-1]
            # (S) for every y,k with y-k,y+k in different parts: cells (x-k,y),(x+k,y)
            pass
        # check only constraints involving the newest column c
        rc=set(cols[c-1])
        # new black cells (c,y): pair with (c-2k,y) black where rows y-k,y+k in different parts
        for y in rc:
            for k in range(1,min(y-1,h-y)+1):
                if part[y-k]!=part[y+k]:
                    x2=c-2*k
                    if x2>=1 and y in cols[x2-1]:
                        return False
        # owner constraint: column x with rows {y-k,y+k}: (x-k,y),(x+k,y) white if both in board (board width q)
        # as columns appear: check for column c as owner (left cell) and for column c as right cell of owner c-k
        r,s=cols[c-1]
        if (s-r)%2==0:
            k=(s-r)//2; y=r+k
            if c-k>=1 and c+k<=q and y in cols[c-k-1]:
                return False
        for x in range(1,c):
            r,s=cols[x-1]
            if (s-r)%2==0:
                k=(s-r)//2; y=r+k
                if x+k==c and x-k>=1:
                    if y in rc: return False
                    if set(cols[x-k-1])&rc: return False
        return True
    def dfs(c):
        if time.time()-t0>tl: return
        maxd[0]=max(maxd[0],c)
        if c==q:
            found[0]+=1
            if len(ex)<2: ex.append(list(cols))
            return
        for pr in pairs:
            if pr in used: continue
            cols.append(pr); used.add(pr)
            if ok(c+1): dfs(c+1)
            used.discard(pr); cols.pop()
    dfs(0)
    return found[0], maxd[0], ex, time.time()-t0
h=int(sys.argv[1])
k=h//2
for A in itertools.combinations(range(1,h+1),k):
    if h%2==0 and 1 not in A: continue
    f,md,ex,el=count(h,A, 50/ (35 if h==7 else 10))
    print('h',h,'A',A,'saturated boards passing square constraints:',f,'maxdepth',md,'sec',round(el,1), ex[:1])
