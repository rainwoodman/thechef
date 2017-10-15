from runtests.tester import Tester
import sys
import os.path

tester = Tester(os.path.abspath(__file__), "thechef")

tester.main(sys.argv[1:])
