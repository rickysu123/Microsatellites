# Microsatellites
Wrote this program with knowledge from only the Codecademy Python course, so really anything is possible! 

Finds microsatellites of length 6 and 9, in multi-fasta files. Microsatellites are repeated amino-acid sequences in genome assemblies. For example: ACTACTACT. Here, the motif is ACT, and is repeated 3 times. A single fasta file gives the genome assembly of a single gene of a single species. The file starts with a ">" character, followed by the description of the gene. Then, the genome assembly is given.

In a multi-fasta file, a certain number of single fasta files from different species are combined together, all describing the same gene. There is an example provided in the repository. 

There is also a sample output. I used this progam on a folder of over 6000 genes of four different insect species. 

For now, this project only works on my computer, because of the directory of the files on my computer. Currently working on making it possible to take in a file from the user. It also probably has a slow runtime. 
