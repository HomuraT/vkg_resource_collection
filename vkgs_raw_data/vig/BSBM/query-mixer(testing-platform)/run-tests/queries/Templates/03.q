PREFIX bsbm-inst: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/>
PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?product ?label
WHERE {
    ?product rdfs:label ?label .
	?product bsbm:productPropertyNumeric1 ?p1 .
	#FILTER ( ?p1 > ${1:product.propertyNum1} ) 
	?product bsbm:productPropertyNumeric3 ?p3 .
	FILTER (?p3 < ${1:product.propertyNum3} )
    OPTIONAL { 
        ?product bsbm:productFeature <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/ProductFeature${1:productfeature.nr}> .
        ?product rdfs:label ?testVar }
    FILTER (!bound(?testVar)) 
}
ORDER BY ?label

