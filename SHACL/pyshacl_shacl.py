from pyshacl import validate
from datetime import datetime

date_time = (datetime.now().strftime(r"%Y-%M-%d_%H%M%S"))

data_graph = 'instance_data/patients.ttl'
shacl_graph = 'shapes_graphs/sphnOnt.ttl'
output_graph = f'validation_reports/output{date_time}test.ttl'

result = validate(data_graph = data_graph, shacl_graph = shacl_graph, check_sht_result=False, check_dash_result=False, )

result[1].serialize(destination= output_graph, format='ttl')