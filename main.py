#!/usr/bin/python

import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-tests", required=True, help="path to tests")
parser.add_argument("-bin", required=True, help="path for exe program")
args = parser.parse_args()

print("args {} {}".format(args.tests, args.bin))

# TEST_DIRECTORY = "testy/"

# TEST_DIRECTORY_ABS = os.path.abspath(TEST_DIRECTORY)

# print(TEST_DIRECTORY_ABS)

# for dictionary in os.listdir(TEST_DIRECTORY_ABS):
#     print(dictionary)

#     sub_directroy = os.path.join(TEST_DIRECTORY_ABS, dictionary)
#     print("sub_directroy {}".format(sub_directroy))

#     for file in os.listdir(sub_directroy):
#         print(file)


# # print("text_output {}".format(text_output))
# exe_path = "trash\main.exe"
# exe_input = "trash\input.txt"
# print(exe_path)
# print(exe_input)
# text_output = subprocess.getoutput('{} < {}'.format(exe_path, exe_input))
# print("text_output: {}".format(text_output))
