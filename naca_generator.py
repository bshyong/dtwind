# This script generates a cross section
# of a symmetrical NACA airfoil given the
# four digit designation.
# Created Sept 24, 2013 by Benjamin Shyong.
# hello@benshyong.com

import sys
import os.path
import csv
import math

def sym_naca(x, length, code):
  x = float(x)
  length = float(length)
  code = float(code)
  return ((code/100)/0.2)*length*(0.2969*math.sqrt(x/length)-(0.1260*x/length)-(0.3516*(x/length)**2)+(0.2843*(x/length)**3)-0.1015*(x/length)**4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: python naca_generator.py NACA_designation length"
        sys.exit(0)
    naca_code = sys.argv[1]
    length = int(sys.argv[2])

    csvwriter = csv.writer(open(naca_code+'.csv','wb'))
    for x in xrange(0,length,1):
      csvwriter.writerow([x, sym_naca(x, length, naca_code)])
