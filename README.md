# drift
A simulation to experiment with the effect of drift on population allele frequency.

## Usage 
```
usage: af.py [-h] --num_samples NUM_SAMPLES --num_sites NUM_SITES --max_offspring MAX_OFFSPRING [--max_generations MAX_GENERATIONS]

optional arguments:
  -h, --help            show this help message and exit
  --num_samples NUM_SAMPLES
  --num_sites NUM_SITES
  --max_offspring MAX_OFFSPRING
```

## Example
The following command produces a line chart of the allele frequencies for each generation.
```
python af.py --num_samples 10 --num_sites 10 --max_offspring 5
```
<center><img src="/doc/fig1.png" width="300"/></center>


