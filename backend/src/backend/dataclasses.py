"""
Define the JSON schemas of the REST API input/output data
"""

import logging
from dataclasses import field

from pydantic.dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class User:
    """ A user from the 'users' database table. """

    user_id: int = field(metadata=dict(title='User ID'))
    user_name: str = field(metadata=dict(title='User name'))


@dataclass
class Measurement:
    """ A measurement from the 'measurements' database table. """

    measurement_id: int = field(metadata=dict(title='Measurement ID'))
    measurement_type: str = field(metadata=dict(title='Measurement name'))
    measurement_value: float = field(metadata=dict(title='Measurement value'))


@dataclass
class InputData:
    """ Input data of the data processing engine. """

    user_id: int = field(metadata=dict(
        title='User ID',
        description='A unique user ID'
    ))
    measurements: list[Measurement] = field(metadata=dict(
        title='Another input field',
        description='A field that contains a list of measurements.'
    ))

    @classmethod
    def parse_file(cls, path) -> 'InputData':
        """ Parse input data from a .json file. """
        return cls.__pydantic_model__.parse_file(path=path)


@dataclass
class OutputData:
    """ Output data of the data processing engine. """

    some_output_field: Measurement = field(metadata=dict(
        title='Some output field',
        description='Some description'
    ))
    some_other_output_field: float = field(metadata=dict(
        title='Some other output field',
        description='Some description'
    ))
    some_last_output_field: str = field(metadata=dict(
        title='Some last output field',
        description='Some description'
    ))
