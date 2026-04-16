import pytest
from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder


class TestNumberAscOrderWithMock:

    def test_sort_mega_sena_numbers(self, mocker):
        """Pilha de 6 posições com 6 números aleatórios (Mega Sena)."""
        mock_stack = mocker.MagicMock(spec=CustomStack)
        numbers = [42, 7, 58, 13, 29, 3]

        mock_stack.pop.side_effect = numbers
        mock_stack.is_empty.side_effect = [False, False, False, False, False, False, True]

        sorter = NumberAscOrder()
        result = sorter.sort(mock_stack)

        assert result == [3, 7, 13, 29, 42, 58]
        assert mock_stack.pop.call_count == 6
        assert mock_stack.is_empty.call_count == 7

    def test_sort_empty_stack_returns_empty_list(self, mocker):
        """Pilha de 6 posições, porém vazia."""
        mock_stack = mocker.MagicMock(spec=CustomStack)
        mock_stack.is_empty.return_value = True

        sorter = NumberAscOrder()
        result = sorter.sort(mock_stack)

        assert result == []
        assert mock_stack.pop.call_count == 0
        assert mock_stack.is_empty.call_count == 1

    def test_sort_raises_type_error_for_invalid_argument(self):
        """Verificar que sort() rejeita argumentos que não são CustomStack."""
        sorter = NumberAscOrder()
        with pytest.raises(TypeError):
            sorter.sort("not a stack")
