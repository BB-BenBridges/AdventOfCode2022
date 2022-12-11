input="""addx 1
addx 4
noop
noop
noop
noop
addx 6
addx -1
noop
addx 5
noop
addx 5
noop
noop
noop
addx 1
addx 3
addx 1
addx 6
addx -1
noop
noop
noop
addx 7
noop
addx -39
noop
noop
noop
addx 7
addx 3
addx -2
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx -8
addx 13
noop
addx 3
addx -2
addx 2
addx 5
addx -31
addx 36
addx -2
addx -36
noop
noop
noop
addx 3
addx 5
addx 2
addx -7
addx 15
addx -5
addx 5
addx 2
addx 1
addx 4
noop
addx 3
noop
addx 2
addx -13
addx -16
addx 2
addx 35
addx -40
noop
noop
addx 7
noop
noop
noop
addx 5
noop
addx 5
addx 10
addx -10
noop
noop
noop
addx 3
noop
addx 16
addx -9
noop
noop
noop
addx 3
noop
addx 7
addx -32
addx 35
addx -38
addx 22
addx 10
addx -29
addx 2
noop
addx 3
addx 5
addx 2
addx 2
addx -12
addx 13
noop
noop
addx 7
addx 5
noop
noop
noop
addx 7
addx -6
addx 2
addx 5
addx -38
addx 1
noop
noop
addx 2
noop
addx 3
addx 5
noop
addx 4
addx -2
addx 5
addx 2
addx 1
noop
addx 4
addx 4
addx -14
addx 16
noop
addx -13
addx 18
addx -1
noop
noop
noop"""

cmds = input.split("\n")
checks = [20, 60, 100, 140, 180, 220]

cycle = 0
register = 1
Total = 0

def checkCycle(cyc, chks, reg, pos):
    global Total
    if cyc in chks:
        var = reg*cyc
        print("Cycle: " + str(cyc) + " Register: " + str(var) + "pos:" + str(pos))
        Total += int(var)

for data in cmds:
    cmd = data.split(" ")
    if cmd[0] == "noop":
        cycle += 1
        checkCycle(cycle, checks, register, 2)

    if cmd[0] == "addx":
        cycle += 1
        checkCycle(cycle, checks, register, 3)
        cycle += 1
        checkCycle(cycle, checks, register, 4)
        register += int(cmd[1])
print(Total)
