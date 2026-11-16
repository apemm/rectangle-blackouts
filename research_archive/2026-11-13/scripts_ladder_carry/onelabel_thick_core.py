def mixed_ok(A, B, C, D):
    G = B[0] - A[0]; e = B[1] - A[1]
    if G == 0: return False
    Sx = C[0] + D[0] - A[0] - B[0]; Sy = C[1] + D[1] - A[1] - B[1]
    if Sx == 0 and Sy == 0: return False
    if Sx * G + 4 * Sy * e != 0: return False
    wx = D[0] - C[0]; wy = D[1] - C[1]
    if wx * wx + 4 * wy * wy != G * G + 4 * e * e: return False
    if (wx, wy) in ((G, e), (-G, -e)): return False
    return len({A[0], B[0], C[0], D[0]}) == 4
