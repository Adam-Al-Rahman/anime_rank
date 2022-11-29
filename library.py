"""
@file: library.py
@brief: Required libraries for the project Rimuru
@author(s): @Adam-Al-Rahaman
"""

# TODO(@Adam-Al-Rahaman): configure the python env
# to remove the error pylint(E0401:import-error)

# Lib: csv
# pylint: disable=locally-disabled, E0401:import-error
from csv import Sniffer

# Lib: IPython
from IPython.display import display

# Lib: pandas
# util then use the pylint commenting system to ignore it.
# pylint: disable=locally-disabled, W0012:unknown-option-value
# pylint: disable=locally-disabled, W0622:redefined-builti
from pandas import DataFrame, Series, read_csv, eval, get_dummies


# Lib: scikit-learn
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MultiLabelBinarizer

# Lib: seaborn
from seaborn import heatmap

# Lib: seaborn
from matplotlib.pyplot import subplots, xticks


# Lib: numpy
from numpy import dot

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
pd_eval = eval
pd_get_dummies = get_dummies

# Required [method|class]: numpy.*
# Alias prefix: np_
np_dot = dot


# Required [method|class]: seaborn.*
# Alias prefix: sns_
sns_heatmap = heatmap

# Required [method|class]: matplotlib.*
# Alias prefix: plt_
plt_subplots = subplots
plt_xticks = xticks


# Required [method|class]: IPython.*
# Alias prefix: ipy_
ipy_display = display

# Required [method|class]: sklearn.*
# Alias prefix: sk_
sk_shuffle = shuffle
sk_train_test_split = train_test_split
sk_logistic_regression = LogisticRegression
sk_multilabel_binarizer = MultiLabelBinarizer
