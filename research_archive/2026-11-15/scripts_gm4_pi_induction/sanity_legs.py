import sys
sys.argv = ["x", "3000"]
exec(open("nt_double_legs.py").read().split("doubles = []")[0])
print(legs_q(255), legs_q(247), legs_q(765), legs_q(1025), legs_q(1005))
tot = sum(len(legs_q(Y)) for Y in range(3, 3001, 2)); print("legs total Y<=3000:", tot)
print(legs_q(8463))
