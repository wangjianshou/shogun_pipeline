
# sys.path.append('/k11e/pvdisk/fastbase/Users/wangjianshou/git/shogun_pipeline')
# from Bz2TarFq_To_fa import Tarbz2File

import sys
import bz2
import os
from itertools import compress

class Tarbz2File:
  def __init__(self, file, rFile):
    self._file = file
    self._rFile = rFile
  def open(self):
    try:
      if self.file.closed:
        self.file = bz2.open(self._file, 'rb')
    except AttributeError:
      self.file = bz2.open(self._file, 'rb')
    try:
      if self.rFile.closed:
        self.rFile = open(self._rFile, 'wb')
    except AttributeError:
      self.rFile = open(self._rFile, 'wb')
  def close(self):
    if not self.file.closed:
      self.file.close()
    if not self.rFile.closed:
      self.rFile.close()
  def __enter__(self):
    self.open()
    return self
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.close()
  def getInfo(self):
    info = self.file.read(512)
    self.filename = info[:100].strip(b'\x00').decode(encoding='utf-8')
    sumASCII = sum(info[:148] + info[156:]) + 32 * 8
    checksum_str = info[148:156].strip(b' ').strip(b'\x00').decode()
    checksum = 0 if checksum_str=='' else int(checksum_str, 8)
    if info[257:263].strip() == b'ustar' or checksum==sumASCII:
      self.fsize = int(info[124:136].strip(b'\x00').decode(), 8)
      self.fzero = 512 - self.fsize % 512
      return True
    else:
      return False
  def fq2fa_bool(self):
    self.iterCompress = [True, True, False, False]
  def process(self):
    if self.fsize == 0: return
    fq = bytearray(self.file.read(self.fsize)).strip().split(b'\n')
    for i in fq[0::4]: i[0] = 62
    self.rFile.write(b'\n'.join(compress(fq, self.iterCompress * (len(fq) // 4))))
    self.rFile.write(b'\n')
    self.file.seek(self.fzero, 1)
  def __iter__(self):
    self.file.seek(0, 0)
    self.rFile.seek(0, 0)
    return self
  def __next__(self):
    while True:
      if self.getInfo():
        self.process()
        return self.filename
      else:
        raise StopIteration

if __name__ == '__main__':
  fq = sys.argv[1]
  fa = sys.argv[2]
  with Tarbz2File(fq, fa) as tarfile:
    tarfile.fq2fa_bool()
    print(list(tarfile))

