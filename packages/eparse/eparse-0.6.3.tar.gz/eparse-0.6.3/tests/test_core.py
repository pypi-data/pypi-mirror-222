#!/usr/bin/env python

'''
unit tests for eparse core
'''

import pandas as pd
import pytest

from eparse.core import (
    df_find_tables,
    df_parse_table,
    df_serialize_table,
    get_df_from_file,
)


@pytest.fixture
def xlsx():
    '''
    excel file fixture
    '''

    return pd.read_excel(
        'tests/eparse_unit_test_data.xlsx',
        header=None,
        index_col=None,
    )


def test_df_find_tables(xlsx):
    t = df_find_tables(xlsx)
    assert len(t) == 2
    assert (2, 2, 'C3', 'ID') in t


def test_df_find_tables_loose(xlsx):
    t = df_find_tables(xlsx, loose=True)
    assert len(t) == 10
    assert (2, 2, 'C3', 'ID') in t
    assert (102, 2, 'C103', 'Schedule of Principal Repayments:') in t


def test_df_parse_table(xlsx):
    t = df_parse_table(xlsx, 102, 2)
    assert t.shape == (11, 8)
    assert t.iloc[0, 2] == 'Date'


def test_df_serialize_table(xlsx):
    t = df_serialize_table(df_parse_table(xlsx, 102, 2), foo='bar')
    assert len(t) == 11 * 8
    assert isinstance(t[22], dict)
    assert 'c_header' in t[22].keys()
    assert t[22]['c_header'] == 'Date'


def test_get_df_from_file():
    filename = 'tests/eparse_unit_test_data.xlsx'
    df_a, *_ = next(get_df_from_file(filename))
    with open(filename, 'rb') as file:
        df_b, *_ = next(get_df_from_file(file))
    assert isinstance(df_a, pd.DataFrame)
    assert isinstance(df_b, pd.DataFrame)
    assert df_a.shape == df_b.shape
