#/usr/bin/bash
docker run --rm --network myapp -v /home/philip/projects/technoatom-final/tests:/tests -v \
 /var/lib/jenkins/workspace/allure-results:/jenkins/allure test:latest \
pytest /tests --runxfail -n 5  --alluredir=/jenkins/allure

