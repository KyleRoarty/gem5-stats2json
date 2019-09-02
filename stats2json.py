#!/usr/bin/env python3

import argparse

def parseArgs():
    parser = argparse.ArgumentParser()
    return parser.parse_args()

def main():
    parsed_args = parseArgs()

if __name__ == '__main__':
    main()
