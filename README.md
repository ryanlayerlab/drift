# drift
A simulation to experiment with the effect of drift on population allele frequency.

## Usage 
```
usage: af.py [-h] --num_samples NUM_SAMPLES --num_sites NUM_SITES
             --mean_offspring MEAN_OFFSPRING --stdev_offspring STDEV_OFFSPRING
             [--max_generations MAX_GENERATIONS] --out_file OUT_FILE

optional arguments:
  -h, --help            show this help message and exit
  --num_samples NUM_SAMPLES
  --num_sites NUM_SITES
  --mean_offspring MEAN_OFFSPRING
  --stdev_offspring STDEV_OFFSPRING
  --max_generations MAX_GENERATIONS
  --out_file OUT_FILE
```

## Example
The following command produces a line chart of the allele frequencies for each generation.
```
python af.py --num_samples 10 --num_sites 5 --mean_offspring 2 --stdev_offspring 1 --out_file af.png
```
<center><img src="/doc/fig1.png" width="300"/></center>


