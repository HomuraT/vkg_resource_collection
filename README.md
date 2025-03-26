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
| uobm     | √        | √       | √               | √                      | MySQL           | 69       | 35               | 9              | 58          |
| rodi_cmt | √        | ×       | √               | √                      | PostgreSQL      | 30       | 49               | 11             | 0           |
| rodi_conference | √ | ×       | √               | √                      | PostgreSQL      | 59       | 46               | 22             | 0           |
| rodi_mondial | √    | ×       | √               | √                      | PostgreSQL      | 20       | 44               | 27             | 0           |
| rodi_sigkdd | √     | ×       | √               | √                      | PostgreSQL      | 49       | 21               | 18             | 0           |
| bsbm     | √        | √       | √               | √                      | MySQL           | 8        | 10               | 30             | 0           |
| npd      | √        | √       | √               | √                      | MySQL, PostgreSQL | 342     | 142              | 238            | 855         |
| cordis   | √        | √       | √               | ×                      | PostgreSQL      | 24       | 22               | 24             | 2           |
| suedtirol | √       | √       | √               | √                      | PostgreSQL      | 37       | 5                | 15             | 6           |
| canonical | √       | √       | √               | ×                      | PostgreSQL      | 4        | 4                | 4              | 0           |
| dblp     | √        | √       | √               | ×                      | MySQL           | 55       | 44               | 30             | 0           |


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