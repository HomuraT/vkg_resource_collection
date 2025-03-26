from src.ontology.statistic import load_ontology, get_ontology_info
from src.utils.os_utils import find_owl_ttl_files

ontology_path = find_owl_ttl_files('../vkgs_raw_data')[0]

graph = load_ontology(ontology_path)

o_info = get_ontology_info(graph)

pass