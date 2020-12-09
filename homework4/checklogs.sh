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
            res=`cat $files | wc -l`
            printf "Total: %s\n\n" "$res" >> result.txt
            ;;
        --by-type)
            request_type=$3
            res=`cat $files | awk '{print $6}' | grep $request_type | wc -l `
            printf "Requests by type %s : %s\n\n" "$request_type" "$res" >> result.txt
            shift
            ;;
        --long)
            res=`cat $files | awk '{print $7,$9,$10}' | sort -rnk3 | head -n 10`
            printf "Longest requests:\n%s\n\n" "$res" >> result.txt
            ;;
        --loc-client)
            res=`cat $files | awk '$9 ~ /4[0-9]*/{print $1,$9,$7}' | sort -k3 | uniq -c -f 2 | sort -rnk1 | head -n 10 | awk '{print $2,$3,$4}' `
            printf "Client error requests with most frequent locations :\n%s\n\n" "$res" >> result.txt
            ;;   
        --long-server)
            res=`cat $files | awk '$9 ~ /5[0-9]*/ {print $1,$7,$9,$10}' | sort -rnk4 | head -n 10 | cut -d" " -f-3 `
            printf "Server error longest requests:\n%s\n\n"  "$res" >> result.txt
            ;;
        *) echo "invalid option -- $2" ;;
    esac
    shift
done
