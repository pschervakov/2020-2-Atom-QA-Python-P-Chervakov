#!/usr/bin/env python3

import argparse
import json
parser = argparse.ArgumentParser(description='log_analysis')
parser.add_argument('path')
parser.add_argument('--total', action='store_true')
parser.add_argument('--by-type', dest='by_type')
parser.add_argument('--long', action='store_true')
parser.add_argument('--long-server',
                    dest='long_server', action='store_true')
parser.add_argument('--json', action='store_true')
args = parser.parse_args()


requests = open(args.path).readlines()

for i in range(0, len(requests)):
    requests[i] = requests[i].split()


def total():
    return str(len(requests))


def requests_by_type(query_type):
    count = 0
    for el in requests:
        if el[5][1:] == query_type:
            count += 1
    return f'{query_type}:{count}'


def longest_requests():
    longest = sorted(requests, key=lambda x: int(
        x[9].replace('-', '0')), reverse=True)
    results = []
    for i in range(0, 10):
        results.append(f'{longest[i][6]}{longest[i][8]}{longest[i][9]}')
    return results


def server_error_request():
    longest = []
    for el in requests:
        if el[8].startswith('5'):
            longest.append(el)
    longest = sorted(longest, key=lambda x: int(
        x[9].replace('-', '0')), reverse=True)
    results = []
    for i in range(0, 10):
        results.append(f'{longest[i][0]} {longest[i][6]} {longest[i][8]}')
    return results


with open('result.txt', 'w') as outfile:
    result = {}
    if args.total:
        result['Total'] = total()
        print('Total:', result['Total'], file=outfile, end='\n\n')
    if args.by_type:
        result['Requests_by_type'] = requests_by_type(args.by_type)
        print('Requests_by_type:',
              result['Requests_by_type'], file=outfile, end='\n\n')
    if args.long:
        print('Longest requests:',file=outfile)
        result['Longest_requests'] = longest_requests()
        for el in result['Longest_requests']:
            print(el, file=outfile)
        print(file=outfile)

    if args.long_server:
        result['Server_error_longest_requests'] = server_error_request()
        print('Server_error_longest_requests:',file=outfile)
        for el in result['Server_error_longest_requests']:
            print(el, file=outfile)
        print(file=outfile)

if args.json:
    with open('result.json', 'w') as outfile_json:
        json.dump(result, outfile_json, indent=4)
 