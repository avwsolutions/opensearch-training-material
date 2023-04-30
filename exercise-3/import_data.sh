if [ -z $1 ]
then
  NODE="localhost"
else
  NODE=$1
fi

curl -H "Content-Type: application/x-ndjson" -X PUT "https://$NODE:9200/ecommerce/_bulk" -ku admin --data-binary "@ecommerce.json"
