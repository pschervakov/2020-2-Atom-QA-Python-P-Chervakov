docker run --rm  -d -v /home/philip/projects/technoatom-final/conf:/tmp/conf  -p 8080:8080 --link mysql:mysql  myapp /app/myapp --config=/tmp/conf
