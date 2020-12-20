#/usr/bin/bash
docker run -i -t \
  -d \
 --rm                \
 --name selenoid                                \
  --network myapp \
-p 4444:4444                                    \
-v /var/run/docker.sock:/var/run/docker.sock    \
-v /home/philip/.aerokube/selenoid/:/etc/selenoid/:ro             \
aerokube/selenoid:latest-release \
-container-network myapp
