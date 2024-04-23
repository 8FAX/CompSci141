"""
141 Tree Lab - Derp the Interpreter

The Derp interpreter parses and evaluates prefix integer expressions 
containing basic arithmetic operators (*,//,-,+). It performs arithmetic with
integer operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, prints the infix expression with 
parentheses to denote order of operation, and evaluates the expression to
print the result.

Author: CS@RIT.EDU

Author: LIAm Scott
"""

from derp_types import *        # dataclasses for the Derp interpreter


##############################################################################
# parse
############################################################################## 
    
def parse(tokens):
    """
    The `parse` function in Python takes a list of tokens as input and constructs a tree structure
    representing a mathematical expression.
    
    Author - Liam Scott
    Last update - 04/23/2024
    @param tokens () - It seems like the input got cut off. Could you please provide the complete list
    of tokens that you want to parse using the `parse` function?
    @returns The `parse` function is returning a tree structure representing a mathematical expression
    parsed from the input tokens. The tree is built using nodes such as `LiteralNode` for numeric
    values, `VariableNode` for variables, and `MathNode` for mathematical operations. The function also
    checks for any remaining tokens in the input and raises a `ValueError` if there are extra tokens
    left.
    
    """
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    precondition: tokens is a non-empty list of strings
    """

    def helper(tokens):
        """
        The function `helper` parses tokens to create a tree structure representing mathematical
        expressions.
        
        Author - Liam Scott
        Last update - 04/23/2024
        @param tokens () - The `tokens` parameter in the `helper` function seems to be a list of tokens
        representing a mathematical expression. Each token can be a number, a variable, or an operator.
        @returns The helper function is returning a tuple containing a node object and the remaining
        tokens after processing. The node object can be a LiteralNode, VariableNode, or MathNode
        depending on the type of token encountered during processing.
        
        """
        if len(tokens) == 0:
            return None, tokens
        token = tokens.pop(0)
        if token.isdigit():
            return LiteralNode(int(token)), tokens
        elif token.isalpha():
            return VariableNode(token), tokens
        else:
            left, tokens = helper(tokens)
            right, tokens = helper(tokens)
            return MathNode(left, token, right), tokens

    tree, remaining_tokens = helper(tokens)
    if remaining_tokens:
        raise ValueError("Extra tokens left in the input")
    return tree
            
##############################################################################
# infix
##############################################################################
        
def infix(node):
    """
    The `infix` function converts a mathematical expression represented as a tree structure into an
    infix notation string.
    
    Author - Liam Scott
    Last update - 04/18/2024
    @param node () - It seems like you have provided a code snippet for an `infix` function that takes a
    `node` as input. The function checks the type of the `node` and returns a string representation of
    the node based on its type.
    @returns The `infix` function takes a node as input and returns a string representation of the node
    in infix notation. The function checks the type of the node and handles different cases accordingly:
    
    """
    """infix: Node -> String 
    Perform an inorder traversal of the node and return a string that
    represents the infix expression.
    precondition: node is a valid derp tree node
    """

    if isinstance(node, LiteralNode):
        return str(node.val)
    elif isinstance(node, VariableNode):
        return node.name
    elif isinstance(node, MathNode):
        left = infix(node.left)
        right = infix(node.right)
        return "(" + left + " " + node.operator + " " + right + ")"
    
 
##############################################################################
# evaluate
##############################################################################    
      
def evaluate(node, sym_tbl):
    """
    The function `evaluate` takes a node and a symbol table as input and recursively evaluates
    mathematical expressions represented by the nodes.
    
    Author - Liam Scott
    Last update - 04/18/2024
    @param node () - The `node` parameter in the `evaluate` function represents a node in an abstract
    syntax tree (AST) that needs to be evaluated. The function recursively evaluates the node and its
    children nodes to compute a final result.
    @param sym_tbl () - The `sym_tbl` parameter in the `evaluate` function is a symbol table that stores
    variable names and their corresponding values. When a `VariableNode` is encountered during
    evaluation, the function looks up the variable name in the symbol table to retrieve its value.
    @returns The `evaluate` function takes a node and a symbol table as input and evaluates the
    expression represented by the node using the symbol table.
    
    """

    """evaluate: Node * dict(key=String, value=int) -> int 
    Return the result of evaluating the expression represented by node.
    Precondition: all variable names must exist in sym_tbl
    precondition: node is a valid derp tree node
    """

    if isinstance(node, LiteralNode):
        return node.val
    elif isinstance(node, VariableNode):
        return sym_tbl[node.name]
    elif isinstance(node, MathNode):
        left = evaluate(node.left, sym_tbl)
        right = evaluate(node.right, sym_tbl)
        if node.operator == "+":
            return left + right
        elif node.operator == "-":
            return left - right
        elif node.operator == "*":
            return left * right
        elif node.operator == "//":
            return left // right
        else:
            return 0


def read_file(in_file):
    """
    The function `read_file` reads a file, extracts key-value pairs from each line, and returns them as
    a dictionary.
    
    Author - Liam Scott
    Last update - 04/18/2024
    @param in_file () - The `read_file` function reads a file and creates a dictionary where the keys
    are the first word in each line of the file and the values are the second word converted to an
    integer.
    @returns A dictionary containing key-value pairs extracted from the lines of the input file. Each
    line is split by a space character, with the first part becoming the key and the second part
    becoming the integer value in the dictionary.
    
    """
    dect = {}
    with open(in_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()  
            if isinstance(line, str): 
                line = line.split(" ")
                dect[line[0]] = int(line[1])
    return dect
                
            

    
##############################################################################
# main
##############################################################################
                     
def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""
    
    print("Hello Herp, welcome to Derp v2.0 :)")
    
    in_file = input("Herp, enter symbol table file: ")
    dect = read_file(in_file)
    
    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    print("Symbol Table")
    print(dect)
    
    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation

    # print("Entering HARD-CODED EXPRESSIONS")
    # hard_coded = MathNode(LiteralNode(3), "*", MathNode(LiteralNode(2), "*", LiteralNode(1)))

    # infixw = infix(hard_coded)
    # print ("infix: " + infixw)
    # print ("evaluation: " + str(evaluate(hard_coded, dect)))
    
    while True:
        prefix_exp = input("derp> ")
        if prefix_exp == "":
            break
        else:
            tokens = prefix_exp.split()
            root = parse(tokens)
            infix_exp = infix(root)
            result = evaluate(root, dect)
            print("--------------------\n")
            print("infix: " + infix_exp)
            print("evaluation: " + str(result))
            print("")
            print("--------------------\n")



        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        
        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE.
            
        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
    # print("Derping the infix expression:")
        
        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
    # print("Derping the evaluation:")
         
    print("Goodbye Herp :(")
    
if __name__ == "__main__":
    main()
