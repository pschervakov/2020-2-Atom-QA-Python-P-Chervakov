#! /usr/bin/env bash

echo '' > result.txt
path=$1
get_files() {
    if [ -d $path ]; then
        for i in $(ls $path | grep log); do
            echo "$path/$i"
        done
    else
        echo $path
    fi
}
files=$(get_files)

while [ -n "$2" ]; do
    case "$2" in
        --total)
            for file in $files; do
                res=`cat $file | wc -l`
                printf "%s Total: %s\n\n" "$file" "$res" >> result.txt
            done
            ;;
        --by-type)
            request_type=$3
            for file in $files; do
                res=`cat $file | awk '{print $6}' | grep $request_type | wc -l `
                printf "%s Requests by type %s : %s\n\n" "$file" "$request_type" "$res" >> result.txt
            done
            shift
            ;;
        --long)
            for file in $files; do
                res=`cat $file | awk '{print $7,$9,$10}' | sort -rnk3 | head -n 10`
                printf "%s Longest requests:\n%s\n\n" "$file" "$res" >> result.txt
            done
            ;;
        --long-server)
            for file in $files; do
                res=`cat $file | awk '$9 ~ /5[0-9]*/ {print $1,$7,$9,$10}' | sort -rnk4 | head -n 10 | cut -d" " -f-3 `
                printf "%s Server error longest requests:\n%s\n\n" "$file" "$res" >> result.txt
            done
            ;;
        *) echo "invalid option -- $2" ;;
    esac
    shift
done
