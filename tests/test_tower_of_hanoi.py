"""Tests for hanoi solver."""
import pytest
from src.tower_of_hanoi import hanoi_solver

def test_hanoi_zero_disks():
    """Tests behavior when 0 disks are provided."""
    result = hanoi_solver(0)
    # Should only show the initial state, with all empty rods.
    assert result == "[] [] []"

def test_hanoi_one_disk():
    """Test solver with a single disk."""
    result = hanoi_solver(1)
    lines = result.split("\n")

    # Initial state + 1 move = 2 lines total.
    assert len(lines) == 2

    # Start.
    assert lines[0] == "[1] [] []"
    # End.
    assert lines[1] == "[] [] [1]"

def test_hanoi_two_disks():
    """Test solver with two disks."""
    result = hanoi_solver(2)
    lines = result.split("\n")

    # 2 disks require 2^2 - 1 = 3 moves + initial state = 4 lines total.
    assert len(lines) == 4
    # Start.
    assert lines[0] == "[2, 1] [] []"
    # End.
    assert lines[-1] == "[] [] [2, 1]"

def test_hanoi_three_disks():
    """Test solver with three disks (classic example)."""
    result = hanoi_solver(3)
    lines = result.split("\n")

    # 3 disks require 2^3 - 1 = 7 moves + initial state = 8 lines total.
    assert len(lines) == 8

    # Start.
    assert lines[0] == "[3, 2, 1] [] []"
    # End.
    assert lines[-1] == "[] [] [3, 2, 1]"

@pytest.mark.parametrize("num_disks,expected_lines", [
    (1, 2),
    (2, 4),
    (3, 8),
    (4, 16),
])
def test_hanoi_move_counts(num_disks, expected_lines):
    """Parametrized test to verify that the number of recorded steps
    always matches 2^n + 1 (initial state + 2^n - 1 moves)."""
    result = hanoi_solver(num_disks)
    lines = result.split("\n")
    assert len(lines) == expected_lines
