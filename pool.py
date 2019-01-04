import sys
import os
import glob
import multiprocessing

def multiFun(tarBz2File):
  os.system("python3 /k11e/pvdisk/fastbase/Users/wangjianshou/git/shogun_pipeline/Bz2TarFq_To_fa.py")

n_cpu = int(sys.argv[2])
pool = multiprocessing.Pool(n_cpu)
for f in files:
  pool.apply_async(multiFun, args=(m, 
