import sys    
from hawser import Hawser

file_name = sys.argv[1]

if not file_name:
    print "No filename given"
    sys.exit(1)

hawser.Hawser(file_name)
