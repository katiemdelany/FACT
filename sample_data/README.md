# Sample Data For Tutorial

## Access

To access the rest of the sample data, download these [files](https://drive.google.com/file/d/1BwvR-Su6vGLfWKZbIGK2D8NSTyyPjd21/view?usp=sharing)
## Test FASTENLOC Pipeline

```
cd Fine-mapping_Pipeline
mv YRI_all1Mb_fastenloc.eqtl.annotation.vcf.gz ./db2fastenloc
python3 finemap.py --fastenloc_SS --pop YRI --LD sample_data/AFR_fourier_ls-all.bed --gwas_SS sample_data/31217584-GCST008053-EFO_0004339-build37.f.tsv.gz --pheno_id Wojcik_Height

```

## Test COLOC Pipeline
```
cd Fine-mapping_Pipeline
python3 finemap.py --coloc --pop YRI ---pop_size 107 --meqtl sample_data/YRI_meqtl_input.txt --frq sample_data/YRI_plink.frq --gwas_SS sample_data/31217584-GCST008053-EFO_0004339-build37.f.tsv.gz --pheno_id Wojcik_Height

```
