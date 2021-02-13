# !/bin/bash

docker build -t xmeme_app .

docker run -d --net="host" xmeme_app

chmod +x sleep.sh
./sleep.sh

curl --location --request POST 'http://localhost:8081/memes' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "xyz",
"url": "https://abc.com",
"caption": "This is a meme"
}'

curl --location --request GET 'http://localhost:8081/memes'
