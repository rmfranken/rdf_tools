import subprocess
from time import time
from datetime import datetime
import os
import configparser

#timed validation of instance data based on TopBraid SHACL Engine
config = configparser.ConfigParser()
config.read('config.ini')

date_time = (datetime.now().strftime(r"%Y-%m-%d_%H:%M:%S"))
resultslist = []
index = 0

datafile = config['SHACL']['instance_data_path']
shapes_folder_path = config['SHACL']['shapes_path']


for file in os.scandir(shapes_folder_path):
    index += 1
    shapesfile = file
    outputfile = str(config['SHACL']['validation_report_path'] + f"{date_time}-{index}.ttl")
    start_time = time()
    subprocess.run([r"./shacl-142/bin/shaclvalidate.sh", "-datafile", datafile, "-shapesfile", shapesfile, ">", outputfile ])
    end_time = time()
    time_taken = end_time - start_time

    # print(str(file))
    resultslist.append(str(file).replace("<DirEntry '","").replace(">","") + " : " + str(time_taken))
    # print(time_taken)

for r in resultslist:
    print (r)
