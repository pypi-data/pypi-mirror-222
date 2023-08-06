# FastaTransformer
FastaTransformer is a python toolset containing fucntions to simplify the usage of .fasta files in analysis as well as transform them into useful states for other tools.

### Authors
The primary author of the FastaTransformer package is [MDinhobl](https://github.com/MDinhobl).

## Major Functions
The following list contains the most useful functions of FastaTransformer.

### Creating Data Folders

1. **MakeGeneBank** - Take a CSV or pandas Dataframe with columns representing Genomes, Gene (or other category), and Sequence and create a folder of .fasta files for each Gene (or chosen category).
1. **GeneBankToAlignmentBank** - Uses [Muscle](https://www.drive5.com/muscle/) (must be installed locally) to transform a folder of .fasta files into a folder of matching alignment files.
1. **AlignmentBankToMatrixBank** - Take a folder of .fasta alignment files (such as one produced by **GeneBankToAlignmentBank**) and produce a folder of distance matricies using the [BioPython](https://biopython.org/docs/1.76/api/Bio.Phylo.TreeConstruction.html) package.
1. **MatrixBankToClusterBank** - Take a folder of distance matricies and create a folder of clusters using [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html).

The functionality of the above tools are combined in  **CSVToAllBanks** - A tool that combines the functionality of **MakeGeneBank**, **GeneBankToAlignmentBank**, **AlignmentBankToMatrixBank**, and **MatrixBankToClusterBank** into one script.

### Other Tools

1. **AlignmentChangeFinder** - Searches a folder of .fasta alignment files for novel changes in several designated ('new') genomes compared to reference ('old') genomes. These results can be further refined by **AlignmentChangeFinderCleanup**.
1. **MatrixBankToAverageMatrix** - Take a folder of distance matricices and produce an 'average' distance matrix with weights.
1. **MatrixBankStats** - Find the statistics of each gene in a folder of distance matricies, such as one produced by **AlignmentBankToMatrixBank**.
1. **FastaDescriptionHunter** - A tool used to search the descriptions of fasta entries (everything following the ">") downloaded from the [NCBI Genbank](https://www.ncbi.nlm.nih.gov/genbank/) for information in specific categories. This is especially useful when trying to search for speicfic sequences after gathering a large number of accession sequences, such as when using [NCBI Batch Entrez](https://www.ncbi.nlm.nih.gov/sites/batchentrez). 

## Installation
To install the latest version of FastaTransformer, use pip install:

    pip install FastaTransformer

## What is a .fasta file?
A .fasta file is a text file format commonly used for storing sequence information for genomic analysis. Each .fasta file can contain information on multiple sequences. Each sequence includes the following information:
- The first row consists of an ">" followed by a *sequence id* and possibly a *description*. 
- The next row (or rows) contain the sequence itself. It can either be an amino acid sequence or a nucleotide sequence.

Here is an example of text within a .fasta file with three sequences, two of which include a description: 
<br>

    >Genome1
    ATATGCAC
    >Genome2 [Gene = B602L]
    ATATGCAT
    >Genome2 [Gene = P72]
    ATATGCATC

Documentation for .fasta files can be found at the [NCBI](https://www.ncbi.nlm.nih.gov/genbank/fastaformat/) and general examples provided at [Wikipedia](https://en.wikipedia.org/wiki/FASTA_format#Description_line) as well as [Bioinformatics.nl](https://www.bioinformatics.nl/tools/crab_fasta.html).