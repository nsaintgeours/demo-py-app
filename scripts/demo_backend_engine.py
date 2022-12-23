"""
Script that runs the data processing engine on some sample data.
"""

import logging

import pkg_resources

from backend.dataclasses import InputData
from backend.engine import Engine


def run_demo():
    # Load some sample input data
    sample_json = pkg_resources.resource_filename('backend', 'resources/sample_input_data.json')
    input_data = InputData.parse_file(path=sample_json)

    # Run data processing engine on sample data
    engine = Engine()
    output_data = engine.run(data=input_data)
    print(output_data)


if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    run_demo()
