import subprocess
from time import time
from datetime import datetime

#timed validation of instance data based on TopBraid SHACL Engine

date_time = (datetime.now().strftime(r"%Y-%M-%d_%H%M%S"))

datafile = r"instance_data\patients.ttl"
shapesfile = r"shapes_graphs\sphnOntWOSparql.ttl"
outputfile = f"validation_reports\output{date_time}.ttl"

start_time = time()
subprocess.run([r"C:\Users\franken\Downloads\shacl-1.4.2-bin\shacl-1.4.2\bin\shaclvalidate.bat", "-datafile", datafile, "-shapesfile", shapesfile, "-outputfile", outputfile])
end_time = time()

print("Time taken: ", end_time - start_time)