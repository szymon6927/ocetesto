#!/usr/bin/python

import os
import subprocess
import argparse


class Tester:
    def __init__(self, bin_path, tests):
        self.bin_path = os.path.abspath(bin_path)
        self.tests = os.path.abspath(tests)
        self.all_input = []
        self.all_output = []

    def find_tests(self):
        abs_tests_path = os.path.abspath(self.tests)

        for item in os.listdir(abs_tests_path):
            if os.path.isdir(os.path.join(abs_tests_path, item)):
                sub_directroy = os.path.join(abs_tests_path, item)

                for sub_file in os.listdir(sub_directroy):
                    self.check_extension(sub_file, sub_directroy)
            else:
                self.check_extension(item, abs_tests_path)

    def check_extension(self, file_name, path):
        if file_name.endswith(".in"):
            self.all_input.append(os.path.abspath(os.path.join(path, file_name)))

        if file_name.endswith(".out"):
            self.all_output.append(os.path.abspath(os.path.join(path, file_name)))

    def get_input(self):
        return self.all_input

    def get_output(self):
        return self.all_output

    def valid_test_count(self):
        if len(self.all_input) == len(self.all_output):
            return True
        else:
            return False

    def checker(self):
        if not self.valid_test_count():
            print("Number of input test and output test are not the same, check tests item")
            exit()

        print("Run test: {}".format(os.path.basename(self.all_input[0])))
        program_output = subprocess.check_output('{} < {}'.format(self.bin_path, self.all_input[0]), shell=True)
        test_output = open(self.all_output[0], newline='\r\n').read()

        if program_output == test_output.encode():
            print("TEST PASSED!")
        else:
            print("TEST FAIL!")
            exit()

        self.all_input.pop(0)
        self.all_output.pop(0)

        if self.all_input and self.all_output:
            self.checker()


def arg_parser():
    description = """Program for automaticly run K.M Ocetkwieicz tests for
    Algorithms and data strucutres exercises
    (!important - program tests only output not execution time)

    example usage "python %(prog)s -tests /tests/ -bin main.exe"
    """

    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-tests", required=True, help="path to tests")
    parser.add_argument("-bin", required=True, help="path for exe program")

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        exit()

    return args


if __name__ == "__main__":
    args = arg_parser()
    octotest = Tester(args.bin, args.tests)
    octotest.find_tests()
    octotest.checker()
