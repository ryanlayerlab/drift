import argparse
import random
import numpy as mp
import matplotlib.pyplot as plt

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_samples',
                        type=int,
                        required=True)
    parser.add_argument('--num_sites',
                        type=int,
                        required=True)
    parser.add_argument('--max_offspring',
                        type=float,
                        required=True)
    parser.add_argument('--max_generations',
                        type=int,
                        default=10) 
    return parser.parse_args()
    return parser.parse_args()

def get_ac(P):
    l = len(P[0])
    ac = [0] * l

    for s in P:
        for i in range(l):
            ac[i] += s[i]

    return ac

def get_af(P):
    af = []
    ac = get_ac(P)
    for locus in ac:
        af.append(locus/len(P))
    return af

def get_sampples(num_samples, num_sites):
    P = []

    for i in range(num_samples):
        s = [0]*num_sites
        r = random.randint(0,num_sites)
        for j in random.sample(range(0, num_sites), r):
            s[j] = 1
        P.append(s)
    return P

def get_pairs(breaders):
    pairs = []
    while len(breaders) > 0:
        a = breaders.pop()
        if len(breaders) > 0:
            b = breaders.pop(random.randrange(len(breaders)))
            pairs.append([a,b])
    return pairs

def mate(mom, dad, num_offspring):
    O = []
    for i in range(num_offspring):
        o = []
        for j in range(len(mom)):
            o.append(random.sample([mom[j],dad[j]], 1)[0])
        O.append(o)
    return O

def one_generation(P, max_offspring):
    _P = []
    pairs = get_pairs(list(range(len(P))))
    for pair in pairs:
        offspring = mate(P[pair[0]],
                         P[pair[1]],
                         random.randint(0,max_offspring))
        _P += offspring
    return _P

def n_generations(P, max_generations, max_offspring):
    AF = [ get_af(P) ]
    for i in range(max_generations):
        P = one_generation(P, max_offspring)
        if len(P) == 0:
            break
        AF.append(get_af(P))
    return AF

def line_plot(AF, out_file):
    fig, ax = plt.subplots ()

    for i in range(len(AF[0])):
        Y=[]
        for g in AF:
            Y.append(g[i])
        ax.plot(range(len(Y)), Y, label=str(i))
    ax.set_ylabel('Allele freq.')
    ax.set_xlabel('Generation')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend(frameon=False)
    fig.savefig(out_file)


def main():
    args = get_args()

    run_name = '-'.join(['num_sites',str(args.num_sites),
                         'num_samples', str(args.num_samples),
                         'max_generations', str(args.max_generations),
                         'max_offspring', str(args.max_offspring)])
    
    P = get_sampples(args.num_samples, args.num_sites)
    AF = n_generations(P, args.max_generations, args.max_offspring)
    line_plot(AF, run_name + '.lp.png')

if __name__ == '__main__':
    main()
