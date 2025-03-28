from src.ontology.statistic import load_ontology, get_ontology_info
from src.utils.os_utils import find_owl_ttl_files, dict_list_to_csv

ontology_paths = find_owl_ttl_files('../vkgs')

o_infos = []
for opath in ontology_paths:
    graph = load_ontology(opath)
    o_info = get_ontology_info(graph)
    if o_info:
        o_infos.append({
            'name': opath,
            'triple_count': o_info['triple_count'],
            'classes': len(o_info['classes']),
            'object properties': len(o_info['object_properties']),
            'data properties': len(o_info['data_properties']),
            'individuals': len(o_info['individuals']),
        })

dict_list_to_csv(o_infos, output_file='../record/ontology_statistic.csv')