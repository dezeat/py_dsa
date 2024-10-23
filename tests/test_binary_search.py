import pytest

from binary_search.binary_search import binary_search


@pytest.mark.parametrize(
    ["arr", "target", "expected"],
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 0),  # Target is first element
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 8),  # Target is last element
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 4),  # Target is middle element
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, -1),  # Target not present (greater)
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, -1),  # Target not present (smaller)
        ([2, 4, 6, 8], 5, -1),  # Target not present (in between)
        ([10], 10, 0),  # Single element present
        ([10], 5, -1),  # Single element not present
        ([-5, -3, -1, 0, 1, 3, 5], -3, 1),  # Negative numbers, target present
        ([-5, -3, -1, 0, 1, 3, 5], 0, 3),  # Negative numbers, target zero
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 2),  # Target present
        ([1000000, 2000000, 3000000], 2000000, 1),  # Large numbers
    ],
    ids=[
        "test_first_element",
        "test_last_element",
        "test_middle_element",
        "test_target_not_present_greater",
        "test_target_not_present_smaller",
        "test_target_not_present_fits",
        "test_single_element_present",
        "test_single_element_not_present",
        "test_negative_numbers_target_present",
        "test_zero_as_target",
        "test_target_present",
        "test_large_numbers",
    ],
)
def test_binary_search(arr: list[int], target: int, expected: int) -> None:
    """Test the binary_search functiom with valid inputs"""
    actual = binary_search(arr, target, 0, len(arr) - 1)

    assert actual == expected


@pytest.mark.parametrize(
    ["arr", "target"],
    [
        ([], 8),  # Empty array
        ([1, 2, 3, 4], None),  # Target is None
    ],
    ids=[
        "test_empty_arr",
        "test_non_target",
    ],
)
def test_invalid_input_binary_search(
    arr: list[int],
    target: int,
) -> None:
    """Test the binary_search functiom with invalid inputs"""
    with pytest.raises(ValueError):
        binary_search(arr, target, 0, len(arr) - 1)
