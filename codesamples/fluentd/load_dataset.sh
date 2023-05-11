#!/bin/bash
docker run --name fluentd  --network host --rm -v /${PWD}/dataset/Bundesliga_Results.csv:/tmp/Bundesliga_Results.csv -v /${PWD}/fluent.conf:/fluentd/etc/fluent.conf fluentd-opensearch-training:1.0
