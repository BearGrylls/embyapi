#!/bin/bash

# wget -O openapi.json https://raw.githubusercontent.com/MediaBrowser/Emby.SDK/master/Resources/OpenApi/openapi_v2.json

docker compose up
docker compose down -v