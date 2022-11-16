"""
@file: library.py
@brief: Required libraries for the project Rimuru
@author(s): @Adam-Al-Rahaman
"""

# Lib: csv
from csv import Sniffer

# Lib: IPython
from IPython.display import display

# Lib: pandas
# TODO(@Adam-Al-Rahaman): configure the python env
# to remove the error pylint(E0401:import-error)
# util then use the pylint commenting system to ignore it.
# pylint: disable=locally-disabled, E0401:import-error
from pandas import DataFrame, Series, read_csv

# Method alias casing: lower_snakes_case
# Class alias casing: PascalCase

# Required [method|class]: csv
# Alias prefix: csv_
CsvSniffer = Sniffer

# Required [method|class]: pandas.*
# Alias prefix: pd_
pd_read_csv = read_csv
pd_dataframe = DataFrame
pd_series = Series


# Required [method|class]: IPython.*
# Alias prefix: ipy_
ipy_display = display
