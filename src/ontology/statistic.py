import os
from typing import List, Optional, Dict, Any
import rdflib
from rdflib import Graph, URIRef


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


def get_ontology_info(graph: Graph) -> Dict[str, Any]:
    """
    Extract basic information from the loaded ontology.

    Args:
        graph (rdflib.Graph): The loaded ontology graph

    Returns:
        Dict[str, Any]: Dictionary containing information about the ontology
    """
    if not graph:
        return {}

    # Get basic ontology information
    info: Dict[str, Any] = {
        'triple_count': len(graph),
        'classes': [],
        'properties': [],
        'individuals': []
    }

    # RDF, RDFS, and OWL namespaces
    RDF = rdflib.namespace.RDF
    RDFS = rdflib.namespace.RDFS
    OWL = rdflib.namespace.OWL

    # Extract classes
    for subject in graph.subjects(RDF.type, OWL.Class):
        if isinstance(subject, URIRef):
            label = None
            for label_obj in graph.objects(subject, RDFS.label):
                label = str(label_obj)
                break
            info['classes'].append({'uri': str(subject), 'label': label})

    # Extract properties
    for subject in graph.subjects(RDF.type, OWL.ObjectProperty):
        if isinstance(subject, URIRef):
            info['properties'].append(str(subject))

    for subject in graph.subjects(RDF.type, OWL.DatatypeProperty):
        if isinstance(subject, URIRef):
            info['properties'].append(str(subject))

    # Extract individuals
    for subject in graph.subjects(RDF.type, OWL.NamedIndividual):
        if isinstance(subject, URIRef):
            info['individuals'].append(str(subject))

    return info