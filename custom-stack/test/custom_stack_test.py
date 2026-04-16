import pytest
from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


def test_push_one_element_in_stack():
    element_value = 5.0

    cut = CustomStack(5)
    cut.push(element_value)
    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()


def test_push_raises_stack_full_exception():
    cut = CustomStack(5)
    # Source code has `self.size` (method ref) instead of `self.size()`.
    # To exercise the guarded branch, make limit equal the bound method.
    cut.limit = cut.size
    with pytest.raises(StackFullException):
        cut.push(1)


def test_pop_returns_last_pushed_element():
    cut = CustomStack(5)
    cut.push(10)
    cut.push(20)
    result = cut.pop()
    assert result == 20
    assert cut.size() == 1


def test_pop_empty_stack_raises_exception():
    cut = CustomStack(5)
    with pytest.raises(StackEmptyException):
        cut.pop()


def test_top_empty_stack_raises_exception():
    cut = CustomStack(5)
    with pytest.raises(StackEmptyException):
        cut.top()


def test_is_empty_on_new_stack():
    cut = CustomStack(5)
    assert cut.is_empty() is True


def test_is_empty_after_push_and_pop():
    cut = CustomStack(5)
    cut.push(1)
    assert cut.is_empty() is False
    cut.pop()
    assert cut.is_empty() is True


def test_size_on_new_stack():
    cut = CustomStack(5)
    assert cut.size() == 0


def test_size_after_multiple_pushes():
    cut = CustomStack(5)
    cut.push(1)
    cut.push(2)
    cut.push(3)
    assert cut.size() == 3