PREFIX bsbm: <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/vocabulary/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX rev: <http://purl.org/stuff/rev#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?title ?text ?reviewDate ?reviewer ?reviewerName ?rating1 ?rating2 ?rating3 ?rating4 
WHERE { 
	?review bsbm:reviewFor <http://www4.wiwiss.fu-berlin.de/bizer/bsbm/v01/instances/dataFromProducer/Product${1:review.product}> .
	?review dc:title ?title .
	?review rev:text ?text .
	?review bsbm:reviewDate ?reviewDate .
	?review rev:reviewer ?reviewer .
	?reviewer foaf:name ?reviewerName .
	OPTIONAL { ?review bsbm:rating1 ?rating1 . }
	OPTIONAL { ?review bsbm:rating2 ?rating2 . }
	OPTIONAL { ?review bsbm:rating3 ?rating3 . }
	OPTIONAL { ?review bsbm:rating4 ?rating4 . }
}
ORDER BY DESC(?reviewDate)