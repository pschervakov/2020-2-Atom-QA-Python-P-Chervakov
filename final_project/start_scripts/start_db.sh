#!/usr/bin/env bash
docker run --name mysql  -e MYSQL_ROOT_PASSWORD=root -v "/home/philip/projects/technoatom-final/start_scripts/init.sql:/docker-entrypoint-initdb.d/init.sql" -it \
 --rm -p 3306:3306 percona