curl -XPUT  http://localhost:9200/datalake -d '
{
  "mappings": {
    "properties": {
      "location": {
        "type": "geo_point"
      }
    }
  }
}' -H 'Content-Type: application/json'
