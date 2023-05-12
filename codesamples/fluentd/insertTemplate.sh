#!/bin/bash
curl -XPUT -H 'Content-Type: application/json' https://localhost:9200/_template/bundesliga -d@index_template.json -u admin -k
