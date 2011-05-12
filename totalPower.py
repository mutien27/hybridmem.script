#!/usr/bin/python -O

import sys
import re

CYCLE_TIME = float(1) / 667000000

workload = sys.argv[1]

dram_size = []
dram_size += ['DRAM']
dram_size += ['64M']
dram_size += ['128M']
dram_size += ['256M']
dram_size += ['512M']
dram_size += ['1024M']
dram_size += ['2048M']

pattern = re.compile("([0-9]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)(\s*)([0-9\.]+)")

start_pattern = re.compile("Data for Full Simulation: ")
idle_energy_pattern = re.compile("Accumulated Idle Energy: ([0-9\.]+) mJ")
access_energy_pattern = re.compile("Accumulated Access Energy: ([0-9\.]+) mJ")
erase_energy_pattern = re.compile("Accumulated Erase Energy: ([0-9\.]+) mJ")
energy_pattern = re.compile("Total Energy: ([0-9\.]+) mJ")
idle_power_pattern = re.compile("Average Idle Power: ([0-9\.]+) mW")
access_power_pattern = re.compile("Average Access Power: ([0-9\.]+) mW")
erase_power_pattern = re.compile("Average Erase Power: ([0-9\.]+) mW")
power_pattern = re.compile("Average Power: ([0-9\.]+) mW")

# === initialization ===
total_cycle = 0

pure_dram_energy = 0
pure_background_energy = 0
pure_actpre_energy = 0
pure_burst_energy = 0
pure_refresh_energy = 0
pure_dram_power = 0
pure_background_power = 0
pure_actpre_power = 0
pure_burst_power = 0
pure_refresh_power = 0

dram_energy = 0
background_energy = 0
actpre_energy = 0
burst_energy = 0
refresh_energy = 0
dram_power = 0
background_power = 0
actpre_power = 0
burst_power = 0
refresh_power = 0

fout = open(workload + '.totalPower.dat', 'w')

# === main ===    
for size in dram_size:
    if size == "DRAM":
        fin1 = open(workload + '_' + size + '/dramPower.dat', 'r')
        for line in fin1:
            p = pattern.match(line)
        
            if p is not None:
                pure_dram_energy += float(p.group(13))
                pure_background_energy += float(p.group(15))
                pure_actpre_energy += float(p.group(17))
                pure_burst_energy += float(p.group(19))
                pure_refresh_energy += float(p.group(21))

                total_cycle = int(p.group(1))
                
        pure_dram_power = pure_dram_energy / (total_cycle * CYCLE_TIME)
        pure_background_power = pure_background_energy / (total_cycle * CYCLE_TIME)
        pure_actpre_power = pure_actpre_energy / (total_cycle * CYCLE_TIME)
        pure_burst_power = pure_burst_energy / (total_cycle * CYCLE_TIME)
        pure_refresh_power = pure_refresh_energy / (total_cycle * CYCLE_TIME)

        fin1.close()

    else:
        fin1 = open(workload + '_' + size + '/dramPower.dat', 'r')

        dram_energy = 0
        background_energy = 0
        actpre_energy = 0
        burst_energy = 0
        refresh_energy = 0
        dram_power = 0
        background_power = 0
        actpre_power = 0
        burst_power = 0
        refresh_power = 0

        for line in fin1:
            p = pattern.match(line)
        
            if p is not None:
                dram_energy += float(p.group(13))
                background_energy += float(p.group(15))
                actpre_energy += float(p.group(17))
                burst_energy += float(p.group(19))
                refresh_energy += float(p.group(21))

                total_cycle = int(p.group(1))

        dram_power = dram_energy / (total_cycle * CYCLE_TIME)
        background_power = background_energy / (total_cycle * CYCLE_TIME)
        actpre_power = actpre_energy / (total_cycle * CYCLE_TIME)
        burst_power = burst_energy / (total_cycle * CYCLE_TIME)
        refresh_power = refresh_energy / (total_cycle * CYCLE_TIME)

        fin1.close()

        fin2 = open(workload + '_' + size + '/NVDIMM.log', 'r')
        flag = 0
        for line in fin2:
            s = start_pattern.match(line)
            ie = idle_energy_pattern.match(line)
            ae = access_energy_pattern.match(line)
            ee = erase_energy_pattern.match(line)
            e = energy_pattern.match(line)
            ip = idle_power_pattern.match(line)
            ap = access_power_pattern.match(line)
            ep = erase_power_pattern.match(line)
            p = power_pattern.match(line)

            if s is not None: flag = 1

            if flag == 1:
                if ie is not None: idle_energy = float(ie.group(1))
                elif ae is not None: access_energy = float(ae.group(1))
                elif ee is not None: erase_energy = float(ee.group(1))
                elif e is not None: energy = float(e.group(1))
                elif ip is not None: idle_power = float(ip.group(1))
                elif ap is not None: access_power = float(ap.group(1))
                elif ep is not None: erase_power = float(ep.group(1))
                elif p is not None:  
                    power = float(p.group(1))
                    break

        fin2.close()

        total_energy = dram_energy + energy
        total_power = dram_power + power
        normalized_energy = total_energy / pure_dram_energy
        normalized_power = total_power / pure_dram_power
        dram_dynamic_energy  = actpre_energy + burst_energy + refresh_energy
        nv_dynamic_energy = access_energy + erase_energy
        dram_dynamic_power = actpre_power + burst_power + refresh_power
        nv_dynamic_power = access_power + erase_power

#        print "%f\t%f\t%f\t%f\t%f\t%f" %(total_energy, dram_energy, energy, total_power, dram_power, power) 
        print >>fout, "%s\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f" %(size, total_energy, normalized_energy, dram_energy, energy, total_power, normalized_power, dram_power, power, background_energy, actpre_energy, burst_energy, refresh_energy, dram_dynamic_energy, idle_energy, access_energy, erase_energy, nv_dynamic_energy, background_power, actpre_power, burst_power, refresh_power, dram_dynamic_power, idle_power, access_power, erase_power, nv_dynamic_power)

fout.close()
