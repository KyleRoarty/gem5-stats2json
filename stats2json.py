#!/usr/bin/env python3

import argparse
import json

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('inFile', type=open)
    parser.add_argument('outFile', type=argparse.FileType('w'))
    return parser.parse_args()

def main():
    START_DATA = 2
    END_DATA = -2

    parsed_args = parseArgs()

    test_array = []

    data_lines = parsed_args.inFile.readlines()[START_DATA:END_DATA]

    for line in data_lines:
        test_array.append(line.split(None, 2))

    for arr in test_array:
        #print(arr)
        parsed_args.outFile.write("{} {}\n".format(arr[0], arr[1]))

if __name__ == '__main__':
    main()
