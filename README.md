## gem5 stats.txt to json

This script takes a gem5 stats file, and converts it into json for easier parsing

### How to run?
```
make venv
. venv/bin/activate
./stats2json <stats file> <output file>
```
Note: There's no input file checking

### ToDo
* Work for multiple stats dumps per run
* Use arrays for some things? (cpu0, cpu1 as cpu[0], cpu[1]?)
* Simplify reading numbers from histograms?
