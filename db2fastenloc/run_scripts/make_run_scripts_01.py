#!/usr/bin/env python

'''make a run script for each subset and output a qsub file'''
import string
import argparse
import sys
import os

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Matrix EQTL to .dat format from .db SNP list')
    parser.add_argument('-g', '--geno',
                        help='input genotype file',
                        required='True'
                        )
    parser.add_argument('-p', '--pheno',
                        help='input phenotype file',
                        required='True'
                        )
    parser.add_argument('-m', '--genemap',
                        help='gene position map',
                        required='True'
                        )
    parser.add_argument('-b', '--pop',
                        help='group/pop id for group_id column of .dat file',
                        required='True'
                        )
    parser.add_argument('-o', '--outdir',
                        help='output .dat file directory',
                        required='True'
                        )
    return parser.parse_args(args)

#retrieve command line arguments
args = check_arg(sys.argv[1:])
genofile = args.geno
phenofile = args.pheno
genemapfile = args.genemap
outdir = args.outdir
pop = args.pop

qsubfile = open('../qsub.txt','w')
prescript = '01_all1MbSNPs2dat'

for i in range(1,23):
    newi = str(i)
    outfilename = 'run_scripts/run_' + prescript + '_' + newi + '.sh'
    outfile = open(outfilename,'w')
    output = '''#!/bin/bash
#PBS -N allmeqtl2dat.''' + newi + '''\n#PBS -S /bin/bash
#PBS -l walltime=24:00:00
#PBS -l nodes=1:ppn=1
#PBS -l mem=16gb
#PBS -o logs/${PBS_JOBNAME}.o${PBS_JOBID}.log
#PBS -e logs/${PBS_JOBNAME}.e${PBS_JOBID}.err
#cd $PBS_O_WORKDIR

'''
    outfile.write(output)
    outfile.write('python3 01_all1MbSNPs2dat.py -g '+ genofile + pop +'_' + newi + '_snp.txt -p '+phenofile +' -m '+genemapfile+' -b '+ pop+ ' -o ' + outdir +'/\n')

    qsubfile.write('nohup run_scripts/' + outfilename + '&\nsleep 3\n')
