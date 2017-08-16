# pybamer
Capture Coverage and Read Length Statistics from your BAM files

---

## Install

1. `wget https://github.com/dantaki/pybamer/releases/download/v0.1/pybamer-0.1.tar.gz`
2. `pip install pybamer-0.1.tar.gz`
 
## Usage

```
$ pybamer --help
usage: pybamer [-h] -i I [-q Q] [-o O]

pybamer        --coverage and read length statistics from your bam file--

optional arguments:
  -h, --help  show this help message and exit

required arguments:
  -i I        BAM file

Optional arguments:
  -q Q        Mapping Quality cutoff [10]
  -o O        Output [pybamer.out]
```


## Output

`$ pybamer -i NA12878.bam -o NA12878_stats.txt`

```
$ less NA12878_stats.txt

#REF    COVERAGE        AVG_READ_LEN    N_READS REF_LEN
1       9.3791701205    2869.05923524   814819  249250621
2       10.3775438229   2921.46434946   863886  243199373
3       10.3559131508   2865.52721178   715646  198022430

...

GENOME  9.67926735249   2897.71371804   10360995        3101804739
```
