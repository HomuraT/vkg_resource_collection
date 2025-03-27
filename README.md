# python enviroment
## create conda enviroment
```shell
conda create -n vkg_collection python=3.12
conda activate vkg_collection
pip install -r requirement.txt
```

# VKGs
| VKG name | Ontology | Mapping | Database Schema | Internal Data Available | Database System | #classes | #object property | #data property | #individual |
|----------|----------|---------|-----------------|------------------------|-----------------|----------|------------------|----------------|-------------|
| [uobm](https://github.com/ontop/ontop-examples/tree/master/aaai-2016-ontoprox) | √ | √ | √ | √ | MySQL | 69 | 35 | 9 | 58 |
| [rodi_cmt](https://github.com/chrpin/rodi/tree/master/data/conference_naive) | √ | × | √ | √ | PostgreSQL | 30 | 49 | 11 | 0 |
| [rodi_conference](https://github.com/chrpin/rodi/tree/master/data/conference_naive) | √ | × | √ | √ | PostgreSQL | 59 | 46 | 22 | 0 |
| [rodi_mondial](https://github.com/chrpin/rodi/tree/master/data/mondial_rel) | √ | × | √ | √ | PostgreSQL | 20 | 44 | 27 | 0 |
| [rodi_sigkdd](https://github.com/chrpin/rodi/tree/master/data/sigkdd_naive) | √ | × | √ | √ | PostgreSQL | 49 | 21 | 18 | 0 |
| [bsbm](https://github.com/ontop/ontop-examples/tree/master/dke-2022-mapping-patterns/scenarios) | √ | √ | √ | √ | MySQL | 8 | 10 | 30 | 0 |
| [npd](https://github.com/ontop/ontop-examples/tree/master/caise-2021-patterns/scenarios/npd) | √ | √ | √ | √ | MySQL, PostgreSQL | 342 | 142 | 238 | 855 |
| [cordis](https://github.com/ontop/ontop-examples/tree/master/caise-2021-patterns/scenarios/cordis) | √ | √ | √ | × | PostgreSQL | 24 | 22 | 24 | 2 |
| [suedtirol](https://github.com/ontop/ontop-examples/tree/master/dke-2022-mapping-patterns/scenarios/suedtirol-open-data) | √ | √ | √ | √ | PostgreSQL | 37 | 5 | 15 | 6 |
| [canonical](https://github.com/ontop/ontop-examples/tree/master/eswc-2018-canonical-iri) | √ | √ | √ | × | PostgreSQL | 4 | 4 | 4 | 0 |
| [dblp](https://github.com/ontop/ontop-examples/tree/master/swj-2017-vig) | √ | √ | √ | × | MySQL | 55 | 44 | 30 | 0 |

# raw vkg resources
## [ontop-examples](https://github.com/ontop/ontop-examples/tree/master)

## [RODI](https://github.com/chrpin/rodi)

## BSBM
http://wbsg.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/V1/results/index.html

## DBLP
https://github.com/kite1988/dblp-parser/blob/master/ReadMe.md
https://dataconverter.io/convert/xml-to-mysql
https://github.com/calledit/xml2rDB

## others
https://github.com/ghxiao/city-bench/tree/master


⭐⭐⭐ https://github.com/ontop/ontop-patterns-tutorial/tree/main