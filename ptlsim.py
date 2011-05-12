#!/usr/bin/python -O

import sys
import re

workload = sys.argv[1]

dram_size = []
dram_size += ['DRAM'] # must be the first item 
dram_size += ['64M']
dram_size += ['128M']
dram_size += ['256M']
dram_size += ['512M']
dram_size += ['1024M']
dram_size += ['2048M']

kernel_insns_pattern = re.compile(" kernel-insns ([0-9\.]+)")
user_insns_pattern = re.compile(" user-insns ([0-9\.]+)")
ipc_pattern = re.compile("Stopping simulation loop at specified limits \(([0-9]+) iterations, ([0-9]+) commits\)")

fout = open(workload + '.ptlsim.dat', 'w')

for size in dram_size:
    fin = open(workload + '_' + size + '/ptlsim.log', 'r')
    
    for line in fin:
        k = kernel_insns_pattern.match(line)
        u = user_insns_pattern.match(line)
        i = ipc_pattern.match(line)

        if k is not None: kernel_insns = k.group(1)
        elif u is not None: user_insns = u.group(1)
        elif i is not None:
            cycles = i.group(1)
            insns = i.group(2)
            ipc = float(insns) / float(cycles)

            if size == "DRAM": 
                dram_ipc = ipc
                dont_print = 1
            else: 
                normalized_ipc = ipc / dram_ipc
                dont_print = 0
    
    fin.close()

    if dont_print == 0:
        print >>fout, "%s\t%f\t%f\t%s\t%s\t%s\t%s" %(size, ipc, normalized_ipc, cycles, insns, kernel_insns, user_insns)

fout.close()
