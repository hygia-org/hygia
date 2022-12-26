import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from parser.generator import Generator

Generator('src/yamls').generate_dags()