#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
<<<<<<< HEAD
import pandas as pd
import createDiffMatrix
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
    subprocess.call(['mentalist','call','-o',outFile,"--db",dbFile,"-i",inFile])
 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mlst",action="store_true", help="running mentalist")
    parser.add_argument("-diff",action="store_true", help="calculate differences from cgMLST results")
    parser.add_argument("-i", "--inputFile",help="the path of input File")
    parser.add_argument("-o", "--outFile" ,help="path of output file ") 
=======
def cgMLST_call(inFile,outFile,dbFile):
    #note: mentalist has to be on your path
    subprocess.call(['mentalist','call','-o',outFile,"--db",dbFile,"-i",inFile])
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mlst",action="store_true", help="running mentalist")
    parser.add_argument("-i", "--inputFile", required = True,help="the path of input File")
    parser.add_argument("-o", "--outFile",required = True, help="path of output file ") 
>>>>>>> 33a406c1fd41ea32f38cbb98e2572192ff7373c7
    parser.add_argument("-db", "--database", help="path of database for cgMLST ") 
    args = parser.parse_args()
    if args.mlst:
        if args.database == None:
<<<<<<< HEAD
            raise SystemExit("missing database to run mentalist. Exit")
        if args.inputFile==None:
            raise SystemExit("missing input file to run mentalist. Exit")
        if args.outFile==None:
            raise SystemExit("missing output name to run mentalist. Exit")
        #else:
            #cgMLST_call(args.inputFile,args.outFile,args.database)
    if args.diff:
        if args.inputFile==None:
            raise SystemExit("missing the result file of cgMLST calling to calculate the differences. Exit")
        calDifference(args.inputFile)
=======
            raise SystemExit("need a database to run mentalist. Exit")
        cgMLST_call(args.inputFile,args.outFile,args.database)

>>>>>>> 33a406c1fd41ea32f38cbb98e2572192ff7373c7
if __name__ == "__main__":
    main()