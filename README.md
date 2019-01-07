1. Bz2TarFq_To_fa.py from \*.fq.tar.bz2 file to \*.fa file  
usage:
```
  python3 Bz2TarFq_To_fa.py example.tar.bz2 example.fa
```
可以直接读取\*.fq.tar.bz2文件，并得到fa文件，所有序列放在一个fa文件中；只需要一次读盘，一次写盘。 
2. pool.py
usage:
```
python3 '/path/*.fq.tar.bz2' outdir n_cpu
```
第一个参数指定fastq格式的\*.tar.bz2，使用通配符匹配的所有文件都会被Bz2TarFq_To_fa.py调用；  
outdir: 指定输出目录；  
n_cpu: 指定需要的CPU数量，也是并行跑的数量；  

3. shogun_pipeline.yaml
```
argo submit shogun_pipeline.yaml -p samples
```
参数samples指定fasta文件路径，一行一个样本, 如example/samples, 注意samples必须在/k11e/pvdisk/fastbase/Users/目录或其子目录之下。
