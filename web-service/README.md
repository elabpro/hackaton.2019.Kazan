# Simple image upload API (on Golang)

## How to run

./prepare.sh && docker-composer run --build

API will be available at http://localhost:8080/api/

## API

- GET http://localhost:8080/api/towns - get JSON array of towns
- GET http://localhost:8080/api/towns/{id} -get town #id
- POST http://localhost:8080/api/towns - upload a town
- POST BODY:
  multipart attachments
  url={url for downloading}
- POST BODY for application/json content type
  JSON {
    {name="{townname}",
     lon="{longitude}",
     lat="{latitude}"}, ...
  }

## How to test

cd src && go test
