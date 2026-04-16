from src.custom_stack_class import CustomStack


class NumberAscOrder:

    def sort(self, custom_stack):
        if not isinstance(custom_stack, CustomStack):
            raise TypeError("Expected a CustomStack instance")

        elements = []
        while not custom_stack.is_empty():
            elements.append(custom_stack.pop())

        return sorted(elements)
