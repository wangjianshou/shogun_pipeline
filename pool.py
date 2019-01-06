import sys
import os
import glob
import multiprocessing

def multiFun(tarBz2File):
  ofile = os.path.basename(tarBz2File).replace('.tar.bz2', '.fa')
  outfile = os.path.join(sys.argv[2], ofile)
  status = os.system("python3 /k11e/pvdisk/fastbase/Users/wangjianshou/git/shogun_pipeline/Bz2TarFq_To_fa.py " + tarBz2File + ' ' + outfile)
  

files = glob.glob(sys.argv[1])
n_cpu = int(sys.argv[3])
pool = multiprocessing.Pool(n_cpu)
for f in files:
  pool.apply_async(multiFun, args=(f,))
pool.close()
pool.join()
