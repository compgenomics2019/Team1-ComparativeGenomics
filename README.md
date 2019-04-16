# Team1-ComparativeGenomics
This pipeline is designed by comparative genomic team of group 1, to analyse genomic features of different organisms <br />
## Script Guidline
### Requirements
**1.** python3  <br />
**2.** mentalist needs to be on your path <br /> 
**3.** pandas install <br /> 
### Quick start
~~~~
git clone https://github.gatech.edu/compgenomics2019/Team1-ComparativeGenomics.git
cd Team1-ComparativeGenomics 
To run cgMLST: ./comparativePipeline.py (or python comparativePipeline.py ) -m - i<name of input> -o <name of output> -db <name of database>
To calculate difference for cgMLST: ./comparativePipeline.py (or python comparativePipeline.py) -diff -i <name of cgMLST output>
~~~~
#### Arguments
`-i `: name of input file <br />
`-o `: name of output file <br />
`-m `:to run cgMLST <br />
`-diff`: to calculate differences for cgMLST result<br />
