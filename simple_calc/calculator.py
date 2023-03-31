from typing import List, Union


class Node:
    def accept(self, visitor: "Visitor"):
        pass


class Operand(Node):
    def __init__(self, value: Union[int, float]):
        self.value = value

    def accept(self, visitor: "Visitor"):
        return visitor.visit_operand(self)


class BinaryOperator(Node):
    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right

    def accept(self, visitor: "Visitor"):
        return visitor.visit_binary_operator(self)


class Plus(BinaryOperator):
    pass


class Minus(BinaryOperator):
    pass


class Times(BinaryOperator):
    pass


class Divide(BinaryOperator):
    pass


class Parentheses(Node):
    def __init__(self, expression: Node):
        self.expression = expression

    def accept(self, visitor: "Visitor"):
        return visitor.visit_parentheses(self)


class Visitor:
    def visit_operand(self, node: Operand):
        pass

    def visit_binary_operator(self, node: BinaryOperator):
        pass

    def visit_parentheses(self, node: Parentheses):
        pass


class InfixVisitor(Visitor):
    def __init__(self):
        self.stack: List[Union[int, float]] = []

    def visit_operand(self, node: Operand):
        self.stack.append(node.value)

    def visit_binary_operator(self, node: BinaryOperator):
        node.left.accept(self)
        node.right.accept(self)
        b = self.stack.pop()
        a = self.stack.pop()
        if isinstance(node, Plus):
            self.stack.append(a + b)
        elif isinstance(node, Minus):
            self.stack.append(a - b)
        elif isinstance(node, Times):
            self.stack.append(a * b)
        elif isinstance(node, Divide):
            self.stack.append(a / b)

    def visit_parentheses(self, node: Parentheses):
        node.expression.accept(self)

    def result(self):
        return self.stack.pop()


class ASTBuilder:
    def __init__(self, input_str: str):
        self.input_str = input_str
        self.index = 0

    def build(self) -> Node:
        return self._parse_expression()


