"""
@file: core.py
@author: @Adam-Al-Rahman
@brief: core [class|method] required for the Rimuru

Guide: core.py
Method or class should be prefixed with `rr_`, because differentiate from others.
"""

# pylint: disable=locally-disabled, E0611:no-name-in-module
from library import ipy_display, pd_dataframe, pd_series, sk_multilabel_binarizer


def rr_clean_alt_list(list_):
    """
    Replace the certain value in the list of string

    Args:
      list_: The list that contain the string.
    """
    return list_.replace('[', '').replace(
        ']', '').replace('\'', '')


def rr_unique_str(dataset: list, to_lower: bool, split_from: str) -> list:
    """
    Return the unique element of a "specific type" of list.

    Args:
        dataset: A list which contain string. e.g: ['['action', 'adventure',]']
        to_lower: a bool value when it true covert all the element in the list to lower case.
        split_from: from which the string element should be split.
    """
    unique_elements = {}

    for sublist in dataset:
        element = sublist.replace('[', '').replace(
            ']', '').replace('\'', '')

        for item in element.split(split_from):
            item = item.strip().lower() if to_lower else item.strip().lower()
            if item in unique_elements.keys():
                unique_elements[item] += 1
            else:
                unique_elements[item] = 1
    return list(unique_elements.keys())


# TODO(@Adam-Al-Rahaman): combine with rr_unique_str
# and remove this one.
def rr_unique(dataset: pd_series) -> pd_series:
    unique_elements = {}

    for element in dataset:
        if type(element) == list:
            for item in element:
                if item in unique_elements.keys():
                    unique_elements[item] += 1
                else:
                    unique_elements[item] = 1
        else:
            if element in unique_elements.keys():
                unique_elements[element] += 1
            else:
                unique_elements[element] = 1
    return pd_series(unique_elements.keys())


def rr_display(dataset: pd_dataframe) -> None:
    """
    Display the pandas dataframe in left align.

    Note: This method should not be used for pandas series as it does not have the `style` method.

    Args:
        dataset: A pandas dataframe
    """

    dataset = dataset.style.set_properties(
        **{'text-align': 'left'})
    dataset = dataset.set_table_styles(
        [dict(selector='th', props=[('text-align', 'left')])])
    ipy_display(dataset)


def rr_to_series(to_series: list, nested: bool = False) -> pd_series:
    """
    Convert the list into pandas series
    Args:
        to_series: list that has to be convert into pandas series
        nested: to check if the list is nested or not.
    """
    return pd_series([element for _list in to_series for element in _list]) if nested else pd_series(to_series)


# rr_to_series(anime_dataset["Genres"].apply(eval))
def rr_str_series(dataset, split_from=",", strip_white_space: bool = False, to_lower: bool = False):
    """
    Convert the dataset which contain string separated with `,` as list.

    Args:
        dataset: A list which contain string. e.g: ['['action', 'adventure',]']
        split_from: from which the string element should be split.
    """
    items = []

    for sublist in dataset:
        element = sublist.replace('[', '').replace(
            ']', '').replace('\'', '')
        current_items = []
        for item in element.split(split_from):
            item = item.lower() if to_lower else item
            current_items.append(item.strip() if strip_white_space else item)
        # items.append(pd_series(current_items).values), use if required
        # to convert the inner list to pandas series
        items.append(current_items)
    return rr_to_series(items)


def rr_encoding(dataframe: pd_dataframe, col: str):
    sk_mlb = sk_multilabel_binarizer()
    dataframe = dataframe.join(
        pd_dataframe(
            sk_mlb.fit_transform(dataframe.pop(col)),
            index=dataframe.index,
            columns=col + "_" + sk_mlb.classes_
        )
    )
    return dataframe


def rr_remove_none(dataset: pd_dataframe, col: str, assign_val):
    """remove the 'None' from 'Genres'"""

    for index, element in enumerate(dataset[col]):
        if element == ["None"]:
            dataset[col][index] = assign_val


def rr_to_df(dataset: pd_series, unique_elements: list):
    """
    Convert the list containing str to a separate column

    Args:
      dataset: pandas series to which need to convert
      unique_elements: all unique elements that the dataset contains
    """
    bool_dict = {}

    for _, element in enumerate(unique_elements):
        bool_dict[element] = dataset.apply(lambda x: element in x)

    return pd_dataframe(bool_dict)


def rr_to_numeric(dataset: pd_series):
    dataset_unique = len(rr_unique(dataset))
