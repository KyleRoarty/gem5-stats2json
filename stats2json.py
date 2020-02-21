#!/usr/bin/env python3

import argparse
import json

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('inFile', type=open)
    parser.add_argument('outFile', type=argparse.FileType('w'))
    return parser.parse_args()

# Takes in list of lists, outputs dict
def recurseStats(unproc_data_lines):
    data_lines = [arr[0].split('.', 1) + [arr[1]] for arr in unproc_data_lines]

    root_lines = []
    nonroot_lines = []

    ret_dict = {}
    recurse_dict = {}

    for line in data_lines:
        root_lines.append(line) if len(line) == 2 else nonroot_lines.append(line)

    root_lines = [line[0].split('::') + [line[1]] for line in root_lines]

    multi_root_lines = []
    single_root_lines = []
    for line in root_lines:
        single_root_lines.append(line) if len(line) == 2 else multi_root_lines.append(line)

    for line in single_root_lines:
        try:
            ret_dict[line[0]] = int(line[1])
        except ValueError:
            ret_dict[line[0]] = float(line[1])

    for line in multi_root_lines:
        try:
            val = int(line[2])
        except ValueError:
            val = float(line[2])
        try:
            ret_dict[line[0]][line[1]] = val
        except KeyError:
            ret_dict[line[0]] = {line[1]: val}

    for line in nonroot_lines:
        try:
            recurse_dict[line[0]].append(line[1:])
        except KeyError:
            recurse_dict[line[0]] = [line[1:]]


    for key in recurse_dict:
        ret_dict[key] = recurseStats(recurse_dict[key])

    return ret_dict

def main():
    START_DATA = 2
    END_DATA = -2

    parsed_args = parseArgs()

    data_array = []

    root = {}

    data_lines = parsed_args.inFile.readlines()[START_DATA:END_DATA]

    for line in data_lines:
        data_array.append(line.split(None, 2))

    root = recurseStats(data_array)

    json.dump(root, parsed_args.outFile, indent=4, separators=(',',':'))

if __name__ == '__main__':
    main()
