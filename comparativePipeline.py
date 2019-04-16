#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
def cgMLST_call(inFile,outFile,dbFile):
    #note: mentalist has to be on your path
    subprocess.call(['mentalist','call','-o',outFile,"--db",dbFile,"-i",inFile])
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mlst",action="store_true", help="running mentalist")
    parser.add_argument("-i", "--inputFile", required = True,help="the path of input File")
    parser.add_argument("-o", "--outFile",required = True, help="path of output file ") 
    parser.add_argument("-db", "--database", help="path of database for cgMLST ") 
    args = parser.parse_args()
    if args.mlst:
        if args.database == None:
            raise SystemExit("need a database to run mentalist. Exit")
        cgMLST_call(args.inputFile,args.outFile,args.database)

if __name__ == "__main__":
    main()