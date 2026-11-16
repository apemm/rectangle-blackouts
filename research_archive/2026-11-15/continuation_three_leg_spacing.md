# A cubic bound for three nearby Pythagorean legs

15 November 2026. This strengthens Theorem 3(b) of
`p_two_block_selfsimilar.md`. It reduces the exceptional range from
\(H^6/8\) to \(H^3/(16S)\) when the legs are multiples of a
power-of-two stride \(S\).

For \(S=32\), an exact finite check then proves that one odd vertical
leg never has three horizontal legs in a slot interval of width four.
Consequently the integer three-choice candidate P system has no
two-label obstruction, at any height. This does not prove solvability
of larger systems, or exclude a certified two-label obstruction.

An independent reader checked the proof and both enumeration algorithms,
then compared their full output sets: all 1285 vectors agree, with no
pair of slot values at distance at most four in the finite range.

## 1. Three-leg bound

Let \(Y\) be a positive odd integer. Suppose
\[
 X_i^2+Y^2=L_i^2,\qquad X_1>X_2>X_3>0,
\]
where the \(X_i\) are multiples of \(S=2^s\), \(s\ge2\). Put
\[
 H=X_1-X_3,\qquad H_{ij}=X_i-X_j\quad(i<j).
\]
Then
\[
 Y<\frac{H_{12}H_{13}H_{23}}{4S}
   \le\frac{H^3}{16S}.
\tag{1}
\]

To prove this, use the odd divisors
\[
 a_i=L_i-X_i,\qquad a_i\mid Y^2,\qquad 0<a_1<a_2<a_3<Y.
\]
The exact leg formula gives
\[
 a_j-a_i=\frac{2H_{ij}a_i a_j}{Y^2+a_i a_j}
        <\frac{H_{ij}\sqrt{a_i a_j}}{Y}.
\tag{2}
\]
The strict inequality follows from \(a_i a_j<Y^2\) and the
arithmetic-geometric mean inequality.

Each \(a_i\) satisfies \(a_i\equiv Y\) or \(-Y\pmod S\). Indeed,
\(Y^2=a_i(a_i+2X_i)\), so \(a_i^2\equiv Y^2\pmod{2S}\).
For odd \(a_i,Y\), one of \(a_i-Y,a_i+Y\) has 2-adic valuation
exactly one, and the other is divisible by \(S\). Thus the claimed
two residue classes are exhaustive.

Let \(g_{ij}=\gcd(a_i,a_j)\). These gcds are odd. If the two divisors
have the same residue class, then \((a_j-a_i)/g_{ij}\) is a positive
multiple of \(S\). Otherwise it is a positive even integer. Therefore,
with \(m_{ij}=S\) in the first case and \(m_{ij}=2\) in the second,
\[
 g_{ij}\le\frac{a_j-a_i}{m_{ij}}
 <\frac{H_{ij}\sqrt{a_i a_j}}{m_{ij}Y}.
\tag{3}
\]
At least two of three divisors have the same residue class, so
\(m_{12}m_{13}m_{23}\ge4S\). Multiplying (3) yields
\[
 g_{12}g_{13}g_{23}
 <\frac{H_{12}H_{13}H_{23}a_1a_2a_3}{4S Y^3}.
\]
But
\[
 Y^2\ge\operatorname{lcm}(a_1,a_2,a_3)
 \ge\frac{a_1a_2a_3}{g_{12}g_{13}g_{23}}.
\]
This proves the first inequality in (1). The second follows from
\(H_{12}+H_{23}=H\) and \(H_{12}H_{23}\le H^2/4\).

Without a stride restriction, the same proof uses \(m_{ij}=2\) for
all three pairs and gives the still useful bound \(Y<H^3/32\).

## 2. The complete three-choice pair check

At \(S=32,M=3\), a pair of ranks has possible slot values
\[
 q\in[3d-2,3d+2].
\]
Their horizontal span is at most \(H=128\). By (1), three legs for
the same odd \(Y\) in this interval require
\[
 Y<128^3/(16\cdot32)=4096.
\tag{4}
\]

The exact script
[check_three_leg_spacing.py](check_three_leg_spacing.py) enumerates all
legs divisible by 32 for every odd \(Y<4096\), with no upper bound
on the hypotenuse. One enumeration uses every divisor \(a<Y\) of
\(Y^2\). An independent enumeration uses primitive Euclid triples and
all admissible odd scale factors. Both return the same 1285 vectors.
There are no two, and therefore no three, slot values within span four
in this finite range. Results are in
[check_three_leg_spacing.json](check_three_leg_spacing.json).

Together with (4), this proves that every odd \(Y\), however large,
has at most two legs in every slot interval of width four.

Each pair of Hilbert labels supplies two odd vertical gaps, one for
each cross-parity role. Each gap therefore forbids at most two of the
five integer differences \(\delta\in\{-2,-1,0,1,2\}\). Their union
forbids at most four. Some difference remains, and every one of the
five differences is attained by choices in \(\{0,1,2\}\).
Thus no two-label subsystem is integer-unsatisfiable, at any scale.

The certified system works modulo three. Four forbidden integer
differences can cover all three residues, so the last argument does
not exclude a certified two-label obstruction. It also gives no bound
on obstruction size beyond three labels in the integer system.

## 3. General strides and a common divisor

The spacing inequality extends to every positive stride \(S\) divisible
by four. If \(g=\gcd(Y,S)\), then
\[
 Y<\frac{H_{12}H_{13}H_{23}}{4Sg}
   \le\frac{H^3}{16Sg}.
\tag{5}
\]
This is an analytic extension. The finite enumeration in Section 2
remains specifically for \(S=32,M=3\).
The prime-power argument and the scaling by \(g\) have also received
an independent written audit.

First suppose \(\gcd(Y,S)=1\). The divisors \(a_i=L_i-X_i\) are then
coprime to \(S\). Write \(S=2^s\prod_p p^{e_p}\), where \(s\ge2\)
and the product runs over odd primes. Since \(a_i^2\equiv Y^2\pmod{2S}\),
each \(a_i\) is congruent to one of \(\pm Y\) modulo \(2^s\) and
modulo every \(p^{e_p}\). For odd prime powers, this follows because
the two factors \(a_i-Y,a_i+Y\) cannot both be divisible by \(p\).
The 2-adic assertion is the same one used in Section 1.

For each pair \(i,j\), let \(m_{ij}\) include \(p^{e_p}\) whenever
the two divisors have the same sign class modulo \(p^{e_p}\). Its
2-part is \(2^s\) when they have the same sign class modulo \(2^s\),
and two otherwise. Then
\[
 m_{ij}\mid\frac{a_j-a_i}{\gcd(a_i,a_j)}.
\]
Indeed the gcd in the denominator is coprime to \(S\), so dividing
by it removes none of these prime-power divisibilities. For every
prime power, at least one of the three pairs has matching signs.
The matching pair can be different at different primes. It follows
nevertheless that
\[
 m_{12}m_{13}m_{23}\ge4S.
\]
Thus the same product and lcm argument proves (5) with \(g=1\).

For general \(g=\gcd(Y,S)\), every \(X_i\) and \(Y\) is divisible
by \(g\). The identity \(L_i^2=X_i^2+Y^2\) implies \(g\mid L_i\)
as well. Divide all lengths and the stride by \(g\). The new vertical
leg \(Y/g\) is odd, the new stride \(S/g\) is still divisible by four,
and \(\gcd(Y/g,S/g)=1\). Applying the coprime bound gives
\[
 Y/g<\frac{(H_{12}/g)(H_{13}/g)(H_{23}/g)}{4(S/g)}.
\]
Multiplication by \(g\) yields (5).
