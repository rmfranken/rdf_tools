from pyshacl import validate
from datetime import datetime
import os
from time import time

date_time = (datetime.now().strftime(r"%Y-%m-%d_%H%M%S"))

data_graph = 'instance_data/patients.ttl'
shacl_graph = 'shapes_graphs/test_library/sphnOnt.ttl'
output_graph = f'validation_reports/output{date_time}test.ttl'

result = validate(data_graph = data_graph, shacl_graph = shacl_graph, check_sht_result=False, check_dash_result=False, )

result[1].serialize(destination= output_graph, format='ttl')


################
# date_time = (datetime.now().strftime(r"%Y-%m-%d_%H%M%S"))
# resultslist = []
# index = 0
# for shapesfile in os.scandir('shapes_graphs/test_library/sphnSplit'):
#     index += 1
#
#     datafile = 'instance_data/patients.ttl'
#     outputfile = f'validation_reports/output{date_time}-{index}.ttl'
#
#     start_time = time()
#     result = validate(data_graph = datafile, shacl_graph = shapesfile, data_graph_format='ttl')
#     result[1].serialize(destination=outputfile, format='ttl')
#     end_time = time()
#     time_taken = end_time - start_time
#
#     # print(str(file))
#     resultslist.append(str(shapesfile).replace("<DirEntry '","").replace(">","") + " : " + str(time_taken))
#     # print(time_taken)
#
# for r in resultslist:
#     print (r)
