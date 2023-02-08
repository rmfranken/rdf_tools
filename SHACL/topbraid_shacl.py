import subprocess
from time import time
from datetime import datetime
import os

#timed validation of instance data based on TopBraid SHACL Engine

date_time = (datetime.now().strftime(r"%Y-%m-%d_%H%M%S"))
resultslist = []
index = 0
for file in os.scandir(r"./shapes_graphs/test_library/sphnSplit"):
    index += 1
    shapesfile = file

    datafile = r"instance_data/patients.ttl"
    outputfile = f"validation_reports/output{date_time}-{index}.ttl"

    start_time = time()
    subprocess.run([r"./shacl-142/bin/shaclvalidate.sh", "-datafile", datafile, "-shapesfile", shapesfile, ">", outputfile ])
    end_time = time()
    time_taken = end_time - start_time

    # print(str(file))
    resultslist.append(str(file).replace("<DirEntry '","").replace(">","") + " : " + str(time_taken))
    # print(time_taken)

for r in resultslist:
    print (r)
