from __future__ import annotations
import operator
from typing import List

class ExprNode:
    """Abstract base class for expression tree nodes."""
    pass

class UnaryOperatorNode(ExprNode):
    """Represents a unary operator node."""
    def __init__(self, operator: str, operand: ExprNode):
        self.operator = operator
        self.operand = operand

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_unary_operator(self)

class BinaryOperatorNode(ExprNode):
    """Represents a binary operator node."""
    def __init__(self, operator: str, left_operand: ExprNode, right_operand: ExprNode):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_binary_operator(self)

class NumericNode(ExprNode):
    """Represents a numeric node."""
    def __init__(self, value: str):
        self.value = value

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_numeric(self)

class PostfixVisitor(Visitor):
    """Visitor to evaluate an expression tree in postfix notation."""
    def __init__(self):
        self.stack = []

    def visit_unary_operator(self, node: UnaryOperatorNode) -> None:
        operand = self.stack.pop()
        op_func = self.get_operator_func(node.operator)
        result = op_func(operand)
        self.stack.append(result)

    def visit_binary_operator(self, node: BinaryOperatorNode) -> None:
        right_operand = self.stack.pop()
        left_operand = self.stack.pop()
        op_func = self.get_operator_func(node.operator)
        result = op_func(left_operand, right_operand)
        self.stack.append(result)

    def visit_numeric(self, node: NumericNode) -> None:
        self.stack.append(float(node.value))

    def get_operator_func(self, operator: str):
        return {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow
        }[operator]

class Parser:
    """Parser to create an expression tree from an arithmetic expression string."""
    def __init__(self, expr: str):
        self.expr = expr
        self.pos = 0

    def parse(self) -> ExprNode:
        """Parses the arithmetic expression string and returns an expression tree."""
        return self.parse_expr()

    def parse_expr(self) -> ExprNode:
        """Parses an expression."""
        node = self.parse_term()

        while True:
            if self.consume('+'):
                right_node = self.parse_term()
                node = BinaryOperatorNode('+', node, right_node)
            elif self.consume('-'):
                right_node = self.parse_term()
                node = BinaryOperatorNode('-', node, right_node)
            else:
                return node

    def parse_term(self) -> ExprNode:
        """Parses a term."""
        node = self.parse_factor()

        while True:
            if self.consume('*'):
                right_node = self.parse_factor()
                node = BinaryOperatorNode('*', node, right_node)
            elif self.consume('/'):
                right_node = self.parse_factor()
                node = BinaryOperatorNode('/', node, right_node)
            elif self.consume('^'):
                right_node = self.parse_factor()
                node = BinaryOperatorNode('^', node, right_node)
            else:
                return node

    def parse_factor(self) -> ExprNode:
        """Parses a factor."""
        if self.consume('-'):
            operand_node =

