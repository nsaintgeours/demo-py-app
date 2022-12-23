"""
Data processing engine
"""

import logging
import os
from pathlib import Path

from dotenv import load_dotenv

from backend.dataclasses import OutputData, InputData

logger = logging.getLogger(__name__)

# Load engine parameters from .env file
load_dotenv(dotenv_path=Path(__file__).parent.parent.parent.parent / '.env')


# noinspection PyArgumentList
class Engine(object):

    def __init__(self):
        """
        Creates a new instance of the data processing engine.
        Engine parameters are loaded from the .env file.
        """
        self.my_param = os.getenv('MY_ENGINE_PARAM', 'MY_DEFAULT_VALUE')
        logger.info(f'Start data processing engine with params: {self.my_param}')

    def run(self, data: InputData, **kwargs) -> OutputData:
        """
        Runs some data processing operations.

        Args:
            data (InputData): input data
            kwargs (dict): some keyword parameters

        Returns: (OutputData) output data
        """

        logger.info('... start data processing engine')

        return OutputData(
            some_output_field=data.measurements[0],
            some_other_output_field=kwargs['some_param'] if 'some_param' in kwargs.keys() else 0.0,
            some_last_output_field=self.my_param
        )
