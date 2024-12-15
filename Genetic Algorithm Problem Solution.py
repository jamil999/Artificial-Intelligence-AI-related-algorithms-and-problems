import random

def create_pop(size):
    popu = []
    for x in range(4):
        chro = ''
        for y in range(size):
            chro += str(random.randint(0, 1))
        popu.append(chro)
    return popu
    
def cal_fit(popu): 
    calculated_fit = []
    for ch in popu:
        fitvalue = 0
        indi = 0
        for gn in ch:
            if gn == '1':
                fitvalue += indi_runs[indi]
            indi += 1
        actualfit = abs(target - fitvalue)
        calculated_fit.append(actualfit)

    return calculated_fit

def do_select(calculated_fit, total_popu):
    selected = []
    max1 = max(calculated_fit)
    max1index = calculated_fit.index(max1)

    for d in range(len(total_popu)):
        if d != max1index:
            selected.append(total_popu[d])

    return selected

def cross(selected):
    chro1, chro2, chro3 = selected[0], selected[1], selected[2]
    len1 = len(chro1)
    par1 = [chro1, chro2]
    par2 = [chro2, chro3]
    par3 = [chro1, chro3]

    split1 = random.randint(1, len1-1)
    offsp1 = par1[0][:split1] + par1[1][split1:]
    offsp2 = par1[1][:split1] + par1[0][split1:]

    split2 = random.randint(1, len1-1)
    offsp3 = par2[0][:split2] + par2[1][split2:]
    offsp4 = par2[1][:split2] + par2[0][split2:]

    split3 = random.randint(1, len1-1)
    offsp5 = par3[0][:split3] + par3[1][split3:]
    offsp6 = par3[1][:split3] + par3[0][split3:]
    
    return offsp1, offsp2, offsp3, offsp4, offsp5, offsp6

def mutat(gen2):
    len1 = len(gen2[0])
    final = []

    for offsp in gen2:     
        mut1 = random.randint(0, len1-1)
        if offsp[mut1] == '1':
            new = offsp[:mut1] + '0' + offsp[mut1+1:]
            final.append(new)
        else:
            new = offsp[:mut1] + '1' + offsp[mut1+1:]
            final.append(new)

    return final

def gen_algo(the_popu):
    for i in range(200):
        fit_num = cal_fit(the_popu)

        selected = do_select(fit_num, the_popu)
        crossed = cross(selected)
        muted = mutat(crossed)

        fit_num = cal_fit(muted)

        for x in fit_num:
            if x == 0:
                return muted[fit_num.index(x)]

        next1 = random.sample(muted, 4)
        the_popu = next1

    return -1

inp = open('Input1.txt')
lines = inp.readline().split()
target = int(lines[1])
players = []
indi_runs = []

for i in range(int(lines[0])):
    lines2 = inp.readline().split()
    players.append(lines2[0])
    indi_runs.append(int(lines2[1]))

initial = create_pop(int(lines[0]))
answer = gen_algo(initial)
print(players)
print(answer)