## GWAS Summary Statistics data steps

### Scripts:
#### liftover_GWAS_SS.R : R script to transform the GWAS Summary Statistics data from genome build hg19 to hg38. This script is called when the user specifies the --liftover flag.

#### assign_LD_GWAS_SS.R : R script to assign LD blocks to each locus and calculate the z-score. Requires three parameters:
      - assoc: GWAS Summary Statistics file
      - LD : LD blocking file 
      - o : output file path