import os
import re
import xml.etree.ElementTree as ET
from typing import Dict, Any, Optional

import rdflib
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS, OWL


def load_ontology(file_path: str) -> Optional[Graph]:
    """
    Load an ontology file (.owl or .ttl) into an RDFLib Graph.

    Args:
        file_path (str): Path to the ontology file (.owl or .ttl)

    Returns:
        Optional[rdflib.Graph]: The loaded ontology graph or None if loading fails
    """
    # Check if file exists
    if not os.path.isfile(file_path):
        print(f"Error: File not found - {file_path}")
        return None

    # Create empty graph
    graph = Graph()

    try:
        # Determine format based on file extension
        file_format = None
        if file_path.lower().endswith('.owl'):
            file_format = 'xml'  # Usually .owl files are in RDF/XML format
        elif file_path.lower().endswith('.ttl'):
            file_format = 'turtle'  # .ttl files are in Turtle format
        else:
            print(f"Warning: Unknown file extension for {file_path}, attempting to parse anyway")

        # Load the ontology
        graph.parse(file_path, format=file_format)
        print(f"Successfully loaded ontology from {file_path}")

        # Basic info about the loaded ontology
        print(f"Graph contains {len(graph)} triples")
        return graph

    except Exception as e:
        print(f"Error loading ontology {file_path}: {str(e)}")
        return None


from typing import Dict, Any
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, OWL


def get_ontology_info(graph: Graph) -> Dict[str, Any]:
    """
    Extract basic element counts from an ontology graph

    Args:
        graph (rdflib.Graph): Loaded ontology graph

    Returns:
        Dict[str, Any]: Dictionary with ontology information
    """
    # Initialize basic information
    if graph is None:
        return {}

    info = {
        'triple_count': len(graph),
        'classes': [],
        'object_properties': [],
        'data_properties': [],
        'individuals': []
    }

    # 1. Query all classes
    for subject in graph.subjects(RDF.type, OWL.Class):
        if isinstance(subject, URIRef):
            uri_str = str(subject)
            if uri_str not in [c['uri'] for c in info['classes'] if 'uri' in c]:
                info['classes'].append({'uri': uri_str})

    # 2. Query all object properties
    for subject in graph.subjects(RDF.type, OWL.ObjectProperty):
        if isinstance(subject, URIRef):
            uri_str = str(subject)
            if uri_str not in info['object_properties']:
                info['object_properties'].append(uri_str)

    # 3. Query all data properties
    for subject in graph.subjects(RDF.type, OWL.DatatypeProperty):
        if isinstance(subject, URIRef):
            uri_str = str(subject)
            if uri_str not in info['data_properties']:
                info['data_properties'].append(uri_str)

    # 4. Query all individuals
    for subject in graph.subjects(RDF.type, OWL.NamedIndividual):
        if isinstance(subject, URIRef):
            uri_str = str(subject)
            if uri_str not in info['individuals']:
                info['individuals'].append(uri_str)

    return info


