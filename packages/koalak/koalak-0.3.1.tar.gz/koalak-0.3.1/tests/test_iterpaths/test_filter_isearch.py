from pathlib import Path
from typing import List

import pytest
from devtools import debug
from koalak.iterpaths import iterpaths

from .utils_test_iterpath import create_paths


def test_iter_paths_arg_isearch(tmp_path):
    # Create some test files and directories
    paths = [
        "abc",
        "a",
        "bc",
        "bc1/bc2",
        "bc1/ab",
        "BC2/",
    ]
    expected = [
        "abc",
        "bc",
        "bc1/bc2",
        "bc1/",
        "BC2/",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, isearch="bc")))
    assert found_paths == expected


def test_iter_paths_arg_isearch_multiple_string(tmp_path):
    # Create some test files and directories
    paths = [
        "ab_file",
        "ac_file",
        "abac_file",
        "ab_dir/ac_file",
        "something_ab_ac/",
        "ABac/",  # not insensitive
    ]
    expected = [
        "abac_file",
        "something_ab_ac/",
        "ABac",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, isearch=["ab", "ac"])))
    # debug(found_paths, expected)
    assert found_paths == expected
    # TODO: continue


def test_iter_paths_arg_dir_isearch(tmp_path):
    # Create some test files and directories
    paths = [
        "abc",
        "a",
        "bc",
        "bc1/bc2",
        "bc1/ab",
        "dir1/",
        "BC",
        "BC_dir/",
    ]
    expected = [
        "abc",
        "a",
        "bc",
        "bc1/",
        "bc1/ab",
        "bc1/bc2",
        "BC",
        "BC_dir/",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, dir_isearch="bc")))
    assert found_paths == expected


def test_iter_paths_arg_dir_isearch_multistring(tmp_path):
    # Create some test files and directories
    paths = [
        "abc",
        "a",
        "bc",
        "bc1/bc2",
        "bc1/ab",
        "dir1/",
        "BC",
        "BC_dir/",
        "BCac",
        "BCac_dir/",
        "bc_dir/ac_dir/",
        "bcac_dir2/",
    ]
    expected = [
        "abc",
        "a",
        "bc",
        "bc1/bc2",
        "bc1/ab",
        "BCac",
        "BCac_dir/",
        "bcac_dir2/",
        "BC",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, dir_isearch=["bc", "ac"])))
    assert found_paths == expected


def test_iter_paths_arg_file_isearch(tmp_path):
    # Create some test files and directories
    paths = [
        "abc",
        "a",
        "bc",
        "bc1/bc2",
        "bc1/ab",
        "dir1/",
        "BC",
        "BC_dir/",
    ]
    expected = [
        "abc",
        "bc",
        "bc1/",
        "bc1/bc2",
        "dir1/",
        "BC_dir",
        "BC",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, file_isearch="bc")))
    assert found_paths == expected


def test_iter_paths_arg_file_isearch_multiple(tmp_path):
    # Create some test files and directories
    paths = [
        "abc",
        "a",
        "bc",
        "bc1/bc2",
        "bc1/ab",
        "dir1/",
        "BC",
        "BC_dir/",
        "BCac",
        "BCac_dir/",
        "bc_dir/ac_dir/",
        "bcac_dir2/",
        "bc_ac",
        "file_BC_ac",
    ]
    expected = [
        "bc1/",
        "dir1/",
        "BC_dir/",
        "BCac",
        "BCac_dir/",
        "bc_dir/",
        "bc_dir/ac_dir/",
        "bcac_dir2/",
        "bc_ac",
        "file_BC_ac",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, file_isearch=["bc", "ac"])))
    assert found_paths == expected


# TODO: trimdir
