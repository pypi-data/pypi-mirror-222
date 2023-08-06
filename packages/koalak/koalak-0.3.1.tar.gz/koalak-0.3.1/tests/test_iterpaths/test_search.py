from pathlib import Path
from typing import List

import pytest
from devtools import debug
from koalak.iterpaths import iterpaths

from .utils_test_iterpath import create_paths


@pytest.mark.skip
def test_iter_paths_arg_search_full(tmp_path):
    # FIXME: this test is skipped because to complecatd to have
    #  one hirarchy to test differents things
    # Create some test files and directories
    paths = [
        # files
        "file",
        "file_key1",
        "file_KEY1",
        "file_key1_key2",
        "file_KEY1_KEY2",
        "file_key1_KEY2",
        # dirs
        "dir/",
        "dir_key1/",
        "dir_KEY1/",
        "dir_key1_key2/",
        "dir_KEY1_KEY2/",
        "dir_key1_KEY2/",
        # Nested in none matching dir
        "dir/file",
        "dir/file_key1",
        "dir/file_KEY1",
        "dir/file_key1_key2",
        "dir/file_KEY1_KEY2",
        "dir/file_key1_KEY2",
        # Nested in matching dir
        "dir_key1_key2/file",
        "dir_key1_key2/file_key1",
        "dir_key1_key2/file_KEY1",
        "dir_key1_key2/file_key1_key2",
        "dir_key1_key2/file_KEY1_KEY2",
        "dir_key1_key2/file_key1_KEY2",
        # Nested in half
        "dir_key1/key2",
    ]
    create_paths(tmp_path, paths)

    # Test 'search' key1
    expected = [
        # files
        "file_key1",
        "file_key1_key2",
        "file_key1_KEY2",
        # dirs
        "dir_key1/",
        "dir_key1_key2/",
        "dir_key1_KEY2/",
        # Nested in none matching dir
        "dir/file_key1",
        "dir/file_key1_key2",
        "dir/file_key1_KEY2",
        # Nested in matching dir
        "dir_key1_key2/file_key1",
        "dir_key1_key2/file_key1_key2",
        "dir_key1_key2/file_key1_KEY2",
        # Nested in half
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, search="key1")))
    # debug(found_paths, expected)
    assert found_paths == expected


def test_iter_paths_arg_search(tmp_path):
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
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, search="bc")))
    # debug(found_paths, expected)
    assert found_paths == expected


def test_iter_paths_arg_search_multiple_string(tmp_path):
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
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, search=["ab", "ac"])))
    # debug(found_paths, expected)
    assert found_paths == expected
    # TODO: continue


def test_iter_paths_arg_dir_search(tmp_path):
    # Create some test files and directories
    paths = [
        "abc",
        "a",
        "bc",
        "bc1/bc2",
        "bc1/ab",
        "dir1/",
        "BC",
        "BD_dir/",
    ]
    expected = [
        "abc",
        "a",
        "bc",
        "bc1/",
        "bc1/ab",
        "bc1/bc2",
        "BC",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, dir_search="bc")))
    assert found_paths == expected


def test_iter_paths_arg_dir_search_multistring(tmp_path):
    # Create some test files and directories
    paths = [
        "abc",
        "a",
        "bc",
        "bc1/bc2",
        "bc1/ab",
        "dir1/",
        "BC",
        "BD_dir/",
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
        "BC",
        "BCac",
        "bcac_dir2/",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, dir_search=["bc", "ac"])))
    assert found_paths == expected


def test_iter_paths_arg_file_search(tmp_path):
    # Create some test files and directories
    paths = [
        "abc",
        "a",
        "bc",
        "bc1/bc2",
        "bc1/ab",
        "dir1/",
        "BC",
        "BD_dir/",
    ]
    expected = [
        "abc",
        "bc",
        "bc1/",
        "bc1/bc2",
        "dir1/",
        "BD_dir",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, file_search="bc")))
    assert found_paths == expected


def test_iter_paths_arg_file_search_multiple(tmp_path):
    # Create some test files and directories
    paths = [
        "abc",
        "a",
        "bc",
        "bc1/bc2",
        "bc1/ab",
        "dir1/",
        "BC",
        "BD_dir/",
        "BCac",
        "BCac_dir/",
        "bc_dir/ac_dir/",
        "bcac_dir2/",
        "bc_ac",
    ]
    expected = [
        "bc1/",
        "dir1/",
        "BD_dir/",
        "BCac_dir/",
        "bc_dir/",
        "bc_dir/ac_dir/",
        "bcac_dir2/",
        "bc_ac",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, file_search=["bc", "ac"])))
    assert found_paths == expected


# TODO: trimdir
