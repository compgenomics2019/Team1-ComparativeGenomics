# Team1-ComparativeGenomics
This pipeline is designed by comparative genomic team of group 1, to analyse genomic features of different organisms <br />
## Script Guidelines
### Requirements
**1.** python3  <br />
**2.** mentalist needs to be on your path <br /> 
**3.** pandas install <br /> 
**4.** tcsh <br />
**5.** kSNP3 appended to path <br />
**6.** MASH appended to path <br />
### Quick start
~~~~
Mentalist installation: 
The instruction of installing Mentalist is described from the website https://github.com/WGS-TB/MentaLiST
~~~~
~~~~
kSNP3 installation:
Please follow the installation guide: http://gensoft.pasteur.fr/docs/kSNP3/01/kSNP3.01%20User%20Guide%20.pdf
~~~~
~~~~
MASH installation:
Please follow the installation guide: https://github.com/marbl/Mash/blob/master/INSTALL.txt
~~~~
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

