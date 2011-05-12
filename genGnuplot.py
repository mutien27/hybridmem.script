#!/usr/bin/python -O

import sys

workload = []
#workload += ['mcf_4']
workload += ['multi-prog_4']

workloadName = []
#workloadName += ['mcf']
workloadName += ['mix1']

figure = []
# --- total ---
figure += ['ipc']
figure += ['normalized_ipc']
figure += ['miss_rate']
figure += ['execution_time']
figure += ['throughput']
figure += ['latency']
# figure += ['queue_latency']
# figure += ['miss_latency']
# figure += ['hit_latency']
# # --- read ---
# figure += ['read_miss_rate']
# figure += ['read_throughput']
# figure += ['read_latency']
# figure += ['read_miss_latency']
# figure += ['read_hit_latency']
# # --- write ---
# figure += ['write_miss_rate']
# figure += ['write_throughput']
# figure += ['write_latency']
# figure += ['write_miss_latency']
# figure += ['write_hit_latency']
# --- power, energy ---
figure += ['power']
figure += ['normalized_power']
figure += ['dram_power']
figure += ['nv_power']
figure += ['energy']
figure += ['normalized_energy']
figure += ['dram_energy']
figure += ['nv_energy']

epoch_figure = []
# epoch_figure += ['working_set_size']

# === functions ===
# --- total ---
def ipc(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output '%s-ipc.eps'" %workload[0]
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"IPC\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.ptlsim.dat\" using 1:2 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    # print "plot \"%s.ptlsim.dat\" using 1:2 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    # print "\"%s.ptlsim.dat\" using 1:2 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def normalizedIpc(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output '%s-normalizedIpc.eps'" %workload[0]
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Normalized IPC\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.ptlsim.dat\" using 1:3 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "reset"
    return

def missRate(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output '%s-missRate.eps'" %workload[0]
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"DRAM Cache Miss Rate\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.hybridsim.dat\" using 1:2 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
#    print "plot \"%s.hybridsim.dat\" using 1:2 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
#    print "\"%s.hybridsim.dat\" using 1:2 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def executionTime(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output '%s-executionTime.eps'" %workload[0]
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Execution Time (us)\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.hybridsim.dat\" using 1:3 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
#    print "plot \"%s.hybridsim.dat\" using 1:3 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
#    print "\"%s.hybridsim.dat\" using 1:3 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def throughput(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output '%s-throughput.eps'" %workload[0]
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Throughput (KB/s)\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.hybridsim.dat\" using 1:4 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
#    print "plot \"%s.hybridsim.dat\" using 1:4 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
#    print "\"%s.hybridsim.dat\" using 1:4 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def latency(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output '%s-latency.eps'" %workload[0]
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Average Memory Latency (us)\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.hybridsim.dat\" using 1:5 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
#    print "plot \"%s.hybridsim.dat\" using 1:5 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
#    print "\"%s.hybridsim.dat\" using 1:5 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def queueLatency(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'queueLatency.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Average Queue Latency (us)\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:6 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:6 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:6 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def missLatency(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'missLatency.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Average Memory Miss Latency (us)\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:7 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:7 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:7 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def hitLatency(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'hitLatency.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Average Memory Hit Latency (us)\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:8 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:8 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:8 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

# --- read ---
def readMissRate(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'readMissRate.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"DRAM Cache Read Miss Rate\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:9 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:9 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:9 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def readThroughput(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'readThroughput.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Read Throughput (KB/s)\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:10 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:10 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:10 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def readLatency(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'readLatency.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Average Read Latency (us)\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:11 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:11 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:11 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def readMissLatency(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'readMissLatency.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Average Read Miss Latency (us)\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:12 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:12 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:12 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def readHitLatency(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'readHitLatency.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Average Read Hit Latency (us)\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:13 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:13 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:13 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

# --- write ---
def writeMissRate(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'writeMissRate.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"DRAM Cache Write Miss Rate\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:14 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:14 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:14 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def writeThroughput(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'writeThroughput.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Write Throughput (KB/s)\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:15 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:15 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:15 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def writeLatency(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'writeLatency.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Average Write Latency (us)\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:16 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:16 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:16 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def writeMissLatency(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'writeMissLatency.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Average Write Miss Latency (us)\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:17 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:17 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:17 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

def writeHitLatency(workload, workloadName):
    print "set terminal postscript enhanced color eps 30"
    print "set output 'writeHitLatency.eps'"
    print "set key right Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Average Write Hit Latency (us)\""
    print "set xtics nomirror (16, 32, 64, 128, 256, 512, 1024)"
    print "set ytics nomirror"
    print "set log x"
#    print "plot \"%s.hybridsim.txt\" using 1:18 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "plot \"%s.hybridsim.dat\" using 1:18 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %(workload[0], workloadName[0]) 
    print "\"%s.hybridsim.dat\" using 1:18 axis x1y1 title \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"red\"" %(workload[1], workloadName[1]) 
    print "reset"
    return

# --- epoch ---
def workingSetSize(item, itemName):
    print "set terminal postscript enhanced color eps 15"
    print "set output \'%s.workingSetSize.eps\'" %itemName
    print "set key right Left reverse nobox"
    print "set xlabel \"Epoch\""
    print "set ylabel \"Working Set Size (MB)\""
    print "set xtics nomirror"
    print "set ytics nomirror"
    print "plot \"%s.epoch.txt\" using 1:3 axis x1y1 title \"%s\" lc rgb \"blue\"" %(item, itemName) 
    print "reset"
    return

# --- power, energy ---
def power(workload, workloadName):
    print "set terminal postscript enhanced color eps 20"
    print "set output '%s-power.eps'" %workload[0]
    print "set key left Left reverse box"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Power (mW)\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.totalPower.dat\" using 1:6 axis x1y1 title \"total\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:8 axis x1y1 title \"dram\" w lp lt 2 lw 5 pt 7 lc rgb \"red\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:9 axis x1y1 title \"nv\" w lp lt 3 lw 5 pt 8 lc rgb \"green\"" %workload[0]
    print "reset"
    return

def normalizedPower(workload, workloadName):
    print "set terminal postscript enhanced color eps 20"
    print "set output '%s-normalizedPower.eps'" %workload[0]
    print "set key left Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Normalized Power\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.totalPower.dat\" using 1:7 axis x1y1 notitle \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "reset"
    return

def dramPower(workload, workloadName):
    print "set terminal postscript enhanced color eps 20"
    print "set output '%s-dramPower.eps'" %workload[0]
    print "set key left Left reverse box"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"DRAM Power (mW)\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.totalPower.dat\" using 1:8 axis x1y1 title \"average power\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:19 axis x1y1 title \"background power\" w lp lt 2 lw 5 pt 7 lc rgb \"red\", \\" %workload[0]
#    print "     \"%s.totalPower.dat\" using 1:20 axis x1y1 title \"act/pre power\" w lp lt 1 lw 5 pt 5 lc rgb \"green\", \\" %workload[0]
#    print "     \"%s.totalPower.dat\" using 1:21 axis x1y1 title \"burst power\" w lp lt 1 lw 5 pt 5 lc rgb \"orange\", \\" %workload[0]
#    print "     \"%s.totalPower.dat\" using 1:22 axis x1y1 title \"refresh power\" w lp lt 1 lw 5 pt 5 lc rgb \"purple\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:23 axis x1y1 title \"dynamic power\" w lp lt 3 lw 5 pt 8 lc rgb \"green\"" %workload[0]
    print "reset"
    return

def nvPower(workload, workloadName):
    print "set terminal postscript enhanced color eps 20"
    print "set output '%s-nvPower.eps'" %workload[0]
    print "set key left Left reverse box"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"NV Power (mW)\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.totalPower.dat\" using 1:9 axis x1y1 title \"average power\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:24 axis x1y1 title \"idle power\" w lp lt 2 lw 5 pt 7 lc rgb \"red\", \\" %workload[0]
#    print "     \"%s.totalPower.dat\" using 1:25 axis x1y1 title \"access power\" w lp lt 1 lw 5 pt 5 lc rgb \"green\", \\" %workload[0]
#    print "     \"%s.totalPower.dat\" using 1:26 axis x1y1 title \"erase power\" w lp lt 1 lw 5 pt 5 lc rgb \"orange\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:27 axis x1y1 title \"dynamic power\" w lp lt 3 lw 5 pt 8 lc rgb \"green\"" %workload[0]
    print "reset"
    return

def energy(workload, workloadName):
    print "set terminal postscript enhanced color eps 20"
    print "set output '%s-energy.eps'" %workload[0]
    print "set key left Left reverse box"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Energy (mJ)\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.totalPower.dat\" using 1:2 axis x1y1 title \"total\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:4 axis x1y1 title \"dram\" w lp lt 2 lw 5 pt 7 lc rgb \"red\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:5 axis x1y1 title \"nv\" w lp lt 3 lw 5 pt 8 lc rgb \"green\"" %workload[0]
    print "reset"
    return

def normalizedEnergy(workload, workloadName):
    print "set terminal postscript enhanced color eps 20"
    print "set output '%s-normalizedEnergy.eps'" %workload[0]
    print "set key left Left reverse nobox"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"Normalized Energy\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.totalPower.dat\" using 1:3 axis x1y1 notitle \"%s\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\"" %(workload[0], workloadName[0]) 
    print "reset"
    return

def dramEnergy(workload, workloadName):
    print "set terminal postscript enhanced color eps 20"
    print "set output '%s-dramEnergy.eps'" %workload[0]
    print "set key left Left reverse box"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"DRAM Energy (mJ)\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.totalPower.dat\" using 1:4 axis x1y1 title \"total energy\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:10 axis x1y1 title \"background energy\" w lp lt 2 lw 5 pt 7 lc rgb \"red\", \\" %workload[0]
#    print "     \"%s.totalPower.dat\" using 1:11 axis x1y1 title \"act/pre energy\" w lp lt 1 lw 5 pt 5 lc rgb \"green\", \\" %workload[0]
#    print "     \"%s.totalPower.dat\" using 1:12 axis x1y1 title \"burst energy\" w lp lt 1 lw 5 pt 5 lc rgb \"orange\", \\" %workload[0]
#    print "     \"%s.totalPower.dat\" using 1:13 axis x1y1 title \"refresh energy\" w lp lt 1 lw 5 pt 5 lc rgb \"purple\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:14 axis x1y1 title \"dynamic energy\" w lp lt 3 lw 5 pt 8 lc rgb \"green\"" %workload[0]
    print "reset"
    return

def nvEnergy(workload, workloadName):
    print "set terminal postscript enhanced color eps 20"
    print "set output '%s-nvEnergy.eps'" %workload[0]
    print "set key left Left reverse box"
    print "set xlabel \"DRAM Cache Size (MB)\""
    print "set ylabel \"NV Energy (mJ)\""
    print "set xtics nomirror (64, 128, 256, 512, 1024, 2048)"
    print "set ytics nomirror"
    print "set log x"
    print "plot \"%s.totalPower.dat\" using 1:5 axis x1y1 title \"total energy\" w lp lt 1 lw 5 pt 5 lc rgb \"blue\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:15 axis x1y1 title \"idle energy\" w lp lt 2 lw 5 pt 7 lc rgb \"red\", \\" %workload[0]
#    print "     \"%s.totalPower.dat\" using 1:16 axis x1y1 title \"access energy\" w lp lt 1 lw 5 pt 5 lc rgb \"green\", \\" %workload[0]
#    print "     \"%s.totalPower.dat\" using 1:17 axis x1y1 title \"erase energy\" w lp lt 1 lw 5 pt 5 lc rgb \"orange\", \\" %workload[0]
    print "     \"%s.totalPower.dat\" using 1:18 axis x1y1 title \"dynamic energy\" w lp lt 3 lw 5 pt 8 lc rgb \"green\"" %workload[0]
    print "reset"
    return


# === main ===
for fig in figure:
    # --- total ---
    if fig == 'ipc': ipc(workload, workloadName)
    elif fig == 'normalized_ipc': normalizedIpc(workload, workloadName)
    elif fig == 'miss_rate': missRate(workload, workloadName)
    elif fig == 'execution_time': executionTime(workload, workloadName)
    elif fig == 'throughput': throughput(workload, workloadName)
    elif fig == 'latency': latency(workload, workloadName)
    elif fig == 'queue_latency': queueLatency(workload, workloadName)
    elif fig == 'miss_latency': missLatency(workload, workloadName)
    elif fig == 'hit_latency': hitLatency(workload, workloadName)
    # --- read ---
    elif fig == 'read_miss_rate': readMissRate(workload, workloadName)
    elif fig == 'read_throughput': readThroughput(workload, workloadName)
    elif fig == 'read_latency': readLatency(workload, workloadName)
    elif fig == 'read_miss_latency': readMissLatency(workload, workloadName)
    elif fig == 'read_hit_latency': readHitLatency(workload, workloadName)
    # --- write ---
    elif fig == 'write_miss_rate': writeMissRate(workload, workloadName)
    elif fig == 'write_throughput': writeThroughput(workload, workloadName)
    elif fig == 'write_latency': writeLatency(workload, workloadName)
    elif fig == 'write_miss_latency': writeMissLatency(workload, workloadName)
    elif fig == 'write_hit_latency': writeHitLatency(workload, workloadName)
    # --- power, energy ---
    elif fig == 'power': power(workload, workloadName)
    elif fig == 'normalized_power': normalizedPower(workload, workloadName)
    elif fig == 'dram_power': dramPower(workload, workloadName)
    elif fig == 'nv_power': nvPower(workload, workloadName)
    elif fig == 'energy': energy(workload, workloadName)
    elif fig == 'normalized_energy': normalizedEnergy(workload, workloadName)
    elif fig == 'dram_energy': dramEnergy(workload, workloadName)
    elif fig == 'nv_energy': nvEnergy(workload, workloadName)


for epoch_fig in epoch_figure:
    if epoch_fig == 'working_set_size': workingSetSize(workload[0], workloadName[0])
    if epoch_fig == 'working_set_size': workingSetSize(workload[1], workloadName[1])
