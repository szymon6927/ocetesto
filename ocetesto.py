#!/usr/bin/python

import os
import subprocess
import argparse
import time
from colorama import init
from colorama import Fore, Back, Style
import re


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]


class Tester:
    def __init__(self, bin_path, tests):
        self.bin_path = os.path.abspath(bin_path)
        self.tests = os.path.abspath(tests)
        self.all_input = []
        self.all_output = []
        self.test_count = 0

    @staticmethod
    def welcome():
        print(""" {}
  ______     ______  _______ .___________. _______     _______.___________.  ______   
 /  __  \   /      ||   ____||           ||   ____|   /       |           | /  __  \  
|  |  |  | |  ,----'|  |__   `---|  |----`|  |__     |   (----`---|  |----`|  |  |  | 
|  |  |  | |  |     |   __|      |  |     |   __|     \   \       |  |     |  |  |  | 
|  `--'  | |  `----.|  |____     |  |     |  |____.----)   |      |  |     |  `--'  | 
 \______/   \______||_______|    |__|     |_______|_______/       |__|      \______/ 

            autor: Szymon Miks
            ETI PG, informatyka
""".format(Fore.MAGENTA))
        time.sleep(3)

    def find_tests(self):
        abs_tests_path = os.path.abspath(self.tests)

        for item in os.listdir(abs_tests_path):
            if os.path.isdir(os.path.join(abs_tests_path, item)):
                sub_directory = os.path.join(abs_tests_path, item)

                for sub_file in os.listdir(sub_directory):
                    self.check_extension(sub_file, sub_directory)
            else:
                self.check_extension(item, abs_tests_path)

        # sort list with naturl sorting
        self.all_input.sort(key=natural_keys)
        self.all_output.sort(key=natural_keys)

        self.set_test_count()

    def check_extension(self, file_name, path):
        if file_name.endswith(".in"):
            self.all_input.append(os.path.abspath(
                os.path.join(path, file_name)))

        if file_name.endswith(".out"):
            self.all_output.append(os.path.abspath(
                os.path.join(path, file_name)))

    def get_input(self):
        return self.all_input

    def get_output(self):
        return self.all_output

    def valid_test_count(self):
        if len(self.all_input) == len(self.all_output):
            return True
        else:
            return False

    def set_test_count(self):
        self.test_count = len(self.all_input)

    def checker(self):
        if not self.valid_test_count():
            print(
                "{} Number of input test and output test are not the same, check tests item".format(Fore.RED))
            return

        print(Style.RESET_ALL)

        print("{} Run test: {}".format(Fore.YELLOW,
                                       os.path.basename(self.all_input[0])), end="\t\t")

        start = time.time()
        program_output = subprocess.check_output(
            '{} < {}'.format(self.bin_path, self.all_input[0]), shell=True)
        elapsed = (time.time() - start)

        test_output = open(self.all_output[0], newline='\r\n').read()

        if program_output == test_output.encode():
            print("{} TEST PASSED! (execution time: {}s)".format(
                Fore.GREEN, round(elapsed, 3)))
        else:
            print("{} TEST FAIL! (execution time: {}s)".format(
                Fore.RED, round(elapsed, 3)))
            print(Style.RESET_ALL)
            self.show_error(program_output.decode(), test_output)
            return

        self.all_input.pop(0)
        self.all_output.pop(0)

        if self.all_input and self.all_output:
            self.checker()

    def show_error(self, student_output, teacher_output):
        print("----------------------------------------------------------")
        print("\n{}The difference is between\n".format(Fore.RED))
        print(student_output)
        print("\n{}and this\n".format(Fore.GREEN))
        print(teacher_output)

    def summary(self):
        print("\n\n")
        print(
            "{}----------------------------------------------------------".format(Fore.CYAN))
        if self.all_input and self.all_output:
            print("{}\t\tFailed!  {}/{}".format(Fore.RED, len(self.all_input),
                                                self.test_count))
        else:
            print("{}\t\tSuccess!  {}/{}".format(Fore.GREEN, self.test_count,
                                                 self.test_count))
        print(
            "{}----------------------------------------------------------".format(Fore.CYAN))


def arg_parser():
    description = """{} Program for automaticly run K.M Ocetkwieicz tests for
    Algorithms and data strucutres exercises
    (!important - program tests only output not execution time)

    example usage {} "python %(prog)s -tests /tests/ -bin main.exe" {}
    """.format(Fore.YELLOW, Fore.GREEN, Fore.CYAN)

    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("--tests", required=True, help="path to tests")
    parser.add_argument("--bin", required=True, help="path for exe program")

    print(Style.RESET_ALL)

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        exit()

    return args


if __name__ == "__main__":
    init()
    Tester.welcome()
    args = arg_parser()
    octotest = Tester(args.bin, args.tests)
    octotest.find_tests()
    octotest.checker()
    octotest.summary()
