#!/bin/bash

./ptlsim.py $1
./dramsim.py $1
./totalPower.py $1
./hybridsim.py $1

./genGnuplot.py > gnuplot.plot
gnuplot gnuplot.plot