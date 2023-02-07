from pyshacl import validate
from datetime import datetime
import os.path

date_time = (datetime.now().strftime(r"%Y-%M-%d_%H%M%S"))

data_graph = 'SHACL/instance_data/valid.ttl'
shacl_graph = 'SDSC_Internal_KG/SDSC_IKG_shapes.ttl'
output_graph = f'SHACL/validation_reports/output{date_time}test.ttl'

result = validate(data_graph = data_graph, shacl_graph = shacl_graph, check_sht_result=False, check_dash_result=False, )

result[1].serialize(destination= output_graph, format='ttl')