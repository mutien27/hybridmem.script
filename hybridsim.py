#!/usr/bin/python -O

import sys
import re

workload = sys.argv[1]

dram_size = []
#dram_size += ['DRAM'] # must be the first item
dram_size += ['64M']
dram_size += ['128M']
dram_size += ['256M']
dram_size += ['512M']
dram_size += ['1024M']
dram_size += ['2048M']

total_accesses_pattern = re.compile("total accesses: ([0-9]+)")
reads_pattern = re.compile("reads: ([0-9]+)")
writes_pattern = re.compile("writes: ([0-9]+)")
cycles_pattern = re.compile("cycles: ([0-9]+)")
execution_time_pattern = re.compile("execution time: ([0-9\.e\+]+) us") 
misses_pattern = re.compile("misses: ([0-9]+)") # *3
hits_pattern = re.compile("hits: ([0-9]+)") # *3
miss_rate_pattern = re.compile("miss rate: ([0-9\.e\-]+)") # *3
average_latency_pattern = re.compile("average latency: ([0-9\.]+) cycles \(([0-9\.]+) us\)") # *3
average_queue_latency_pattern = re.compile("average queue latency: ([0-9\.]+) cycles \(([0-9\.]+) us\)")
average_miss_latency_pattern = re.compile("average miss latency: ([0-9\.]+) cycles \(([0-9\.]+) us\)") # *3
average_hit_latency_pattern = re.compile("average hit latency: ([0-9\.]+) cycles \(([0-9\.]+) us\)") # *3
throughput_pattern = re.compile("throughput: ([0-9\.e\+]+) KB/s") # *3
working_set_size_pages_pattern = re.compile("working set size in pages: ([0-9]+)")
working_set_size_bytes_pattern = re.compile("working set size in bytes: ([0-9]+) bytes")
end_pattern = re.compile("Epoch data:")

fout1 = open(workload + '.hybridsim.dat', 'w')
fout2 = open(workload + '.hybridsim_table.dat', 'w')

for size in dram_size:
    fin = open(workload + '_' + size + '/hybridsim.log', 'r')
    flag = 0

    for line in fin:
        ta = total_accesses_pattern.match(line)
        r = reads_pattern.match(line)
        w = writes_pattern.match(line)
        c = cycles_pattern.match(line)
        et = execution_time_pattern.match(line)
        m = misses_pattern.match(line)
        h = hits_pattern.match(line)
        mr = miss_rate_pattern.match(line)
        al = average_latency_pattern.match(line)
        aql = average_queue_latency_pattern.match(line)
        aml = average_miss_latency_pattern.match(line)
        ahl = average_hit_latency_pattern.match(line)
        t = throughput_pattern.match(line)
        wssp = working_set_size_pages_pattern.match(line)
        wssb = working_set_size_bytes_pattern.match(line)
        end = end_pattern.match(line)

        if ta is not None: 
            total_accesses = ta.group(1)
            flag = 1
        elif r is not None: 
            reads = r.group(1)
            flag = 2
        elif w is not None: 
            writes = w.group(1)
            flag = 3
        elif c is not None: cycles = c.group(1)
        elif et is not None: execution_time = et.group(1)
        elif m is not None:
            if flag == 1: total_misses = m.group(1)
            elif flag == 2: read_misses = m.group(1)
            elif flag == 3: write_misses = m.group(1)
        elif h is not None:
            if flag == 1: total_hits = h.group(1)
            elif flag == 2: read_hits = h.group(1)
            elif flag == 3: write_hits = h.group(1)
        elif mr is not None:
            if flag == 1: total_miss_rate = mr.group(1)
            elif flag == 2: read_miss_rate = mr.group(1)
            elif flag == 3: write_miss_rate = mr.group(1)
        elif al is not None:
            if flag == 1: 
                total_average_latency_cycles = al.group(1)
                total_average_latency_time = al.group(2)
            elif flag == 2: 
                read_average_latency_cycles = al.group(1)
                read_average_latency_time = al.group(2)
            elif flag == 3: 
                write_average_latency_cycles = al.group(1)
                write_average_latency_time = al.group(2)
        elif aql is not None: 
            total_average_queue_latency_cycles = aql.group(1)
            total_average_queue_latency_time = aql.group(2)
        elif aml is not None:
            if flag == 1: 
                total_average_miss_latency_cycles = aml.group(1)
                total_average_miss_latency_time = aml.group(2)
            elif flag == 2: 
                read_average_miss_latency_cycles = aml.group(1)
                read_average_miss_latency_time = aml.group(2)
            elif flag == 3: 
                write_average_miss_latency_cycles = aml.group(1)
                write_average_miss_latency_time = aml.group(2)
        elif ahl is not None:
            if flag == 1: 
                total_average_hit_latency_cycles = ahl.group(1)
                total_average_hit_latency_time = ahl.group(2)
            elif flag == 2: 
                read_average_hit_latency_cycles = ahl.group(1)
                read_average_hit_latency_time = ahl.group(2)
            elif flag == 3: 
                write_average_hit_latency_cycles = ahl.group(1)
                write_average_hit_latency_time = ahl.group(2)
        elif t is not None:
            if flag == 1: total_throughput = t.group(1)
            if flag == 2: read_throughput = t.group(1)
            if flag == 3: write_throughput = t.group(1)
        elif wssp is not None: working_set_size_pages = wssp.group(1)
        elif wssb is not None: 
            working_set_size_bytes = wssb.group(1)
            working_set_size = float(working_set_size_bytes)/1000000
        elif end is not None: break

    print >>fout1, "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" %(size, total_miss_rate, execution_time, total_throughput, total_average_latency_time, total_average_queue_latency_time, total_average_miss_latency_time, total_average_hit_latency_time, read_miss_rate, read_throughput, read_average_latency_time, read_average_miss_latency_time, read_average_hit_latency_time, write_miss_rate, write_throughput, write_average_latency_time, write_average_miss_latency_time, write_average_hit_latency_time)
    print >>fout2, "%s\t%s\t%s\t%s\t%s\t%s" %(size, total_accesses, reads, writes, working_set_size_pages, working_set_size)

    fin.close()

fout1.close()
fout2.close()

