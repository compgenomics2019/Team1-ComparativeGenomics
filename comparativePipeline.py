#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
import pandas as pd
import createDiffMatrix
def kchoose(Kchooser):
    # Opens Kchooser.report to find optimum k-mer value from Kchooser kSNP3 script 
	dir_kc = os.getcwd()
	file_hand = open('dir_kc/Kchooser.report', 'r')
	k_val = 0
	for i in file_hand:
		if i.startswith('When'):
			if int(i.split()[3]) > k_val:
				k_val = int(i.split()[3])
            
	print("Your optimum k-mer length is: {}\n".format(k_val))
	print("Review Kchooser.report for more details..")
	
	return(k_val)

def kSNP3():
    ## <subprocess for various utility commands>
    ## Test in gabriel_
    ## :)
    
def MASH():
    ## Translate this into a script
    '''
    first i did this: ./mash dist refseq.genomes.k21s1000.msh ../../functional_annotation/assembled_reads/{}_scaffolds.fasta > distances_{}.tab
    replacing  the “{}” with the number for the input file
    then i did sort -gk3 distances_{}.tab | head -n1 >> strains_file.txt
    '''

def calDifference(inFile):
    """ before calculate difference for output of cgMLST, the last two columns need to be cut
    the output will be on the inFile """
    inFile_dropST=os.path.abspath(inFile) + "_dropST.csv" 
    dropColumns(inFile,inFile_dropST)
    outFile=os.path.join("/".join(os.path.abspath(inFile_dropST).split("/")[:-1]),"diffMatrix.csv")
    
    #after dropping ST columns, now can begin calculating the difference
    createDiffMatrix.main(inFile_dropST,outFile)
def dropColumns(inFile,outFile):
    file=pd.read_csv(inFile,sep='\t')
    file=file.drop(columns=['ST','clonal_complex']) ### drop columns
    file.to_csv(outFile,sep=',',index=False)     ### write into csv
def cgMLST_call(inFile,outFile,dbFile):
    #note: mentalist has to be on your path
    command="mentalist call -i {} -o {} --db {}".format(inFile,outFile,dbFile)    
    #print(command)
    #subprocess.run(command)
    #subprocess.call(['mentalist','call','-o',outFile,"--db",dbFile,"-i",inFile])
    subprocess.call(command,shell=True)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mlst",action="store_true", help="running mentalist")
    parser.add_argument("-diff",action="store_true", help="calculate differences from cgMLST results")
    parser.add_argument("-i", "--inputFile",help="the path of input File")
    parser.add_argument("-o", "--outFile" ,help="path of output file ") 
    parser.add_argument("-db", "--database", help="path of database for cgMLST ") 
    args = parser.parse_args()
    if args.mlst:
        if args.database == None:
            raise SystemExit("missing database to run mentalist. Exit")
        if args.inputFile==None:
            raise SystemExit("missing input sample file to run mentalist. Exit")
        if args.outFile==None:
            raise SystemExit("missing output name to run mentalist. Exit")
        else:
            cgMLST_call(args.inputFile,args.outFile,args.database)
    if args.diff:
        if args.inputFile==None:
            raise SystemExit("missing the result file of cgMLST calling to calculate the differences. Exit")
        calDifference(args.inputFile)
if __name__ == "__main__":
    main()
