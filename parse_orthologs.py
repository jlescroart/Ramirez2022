#!/usr/bin/env python

#### Description: Parse gene set of each sample into separate genes 
#### ... and group orthologous genes of all samples in a fasta per gene.
#### ... Takes GffRead gene sets as input and generates orthologs for downstream local realignment with PRANK.
#### List file: The absolute path for the gene set of each sample in order, one per line.
#### Use: parse_orthologs.py DATASETXXX.list
#### Written by: Henrique V. Figueiró - henriquevf@gmail.com as prankAlignment.py
#### Adapted by Jonas Lescroart on 24 May 2020.
#### Following changes were made:
#### 1/ number of input gene sets is determined from list file rather than hardcoded in script;
#### 2/ If genomic coordinates are available in header from preceding gffread analysis,
#### ... these are now propagated. Switch comment flag on lines 49-50 to disable.

from Bio import SeqIO
import sys
import os

#Open dataset.list file

dataset = open(sys.argv[1], 'r')
lines = dataset.readlines()

dataset_name = sys.argv[1].split('.')[0]

#Create dataset and windows folders

if not os.path.exists(os.getcwd() + '/fasta/'):
    os.makedirs(os.getcwd() + '/fasta')

chr_dir = os.getcwd() + '/fasta/'

#Read gene set filenames and get species/sample names

names = list()

for i in range(len(lines)):
    line = str(lines[i].rstrip())
    name = str(line.split('/')[-1].split('.')[0])
    names.append(name)
    print(names[i])

#Create each orthologous gene fasta file and append ortholog from subsequent samples

for i in range(len(lines)):
    with open(str(lines[i].rstrip()), 'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            with open(chr_dir + record.id + ".fa", 'a') as out_file:
                coordinates = ' '.join(record.description.split(' ')[1:])
                seq_name = str('>' + names[i])
                seq =  str(record.seq)
                #out_file.write(seq_name + '\n' + seq + '\n')
                out_file.write(seq_name + ' ' + coordinates + '\n' + seq + '\n')
            out_file.close()
