import parser

def evaluate(ast):
    if ast["tag"] == "number":
        return ast["value"]
    elif ast["tag"] == "+":
        return evaluate(ast["left"]) + evaluate(ast["right"])
    elif ast["tag"] == "-":
        return evaluate(ast["left"]) - evaluate(ast["right"])
    elif ast["tag"] == "*":
        return evaluate(ast["left"]) * evaluate(ast["right"])
    elif ast["tag"] == "/":
        return evaluate(ast["left"]) / evaluate(ast["right"])
    else:
        raise ValueError(f"Unknown AST node: {ast}")
    
    def test_evaluate():
        print("test evaluate()")
        ast = {"tag": "number", "value": 3}
        assert evaluate(ast) == 3
        ast = {
            "tag": "+",
            "left": {"tag": "number", "value": 3},
            "right": {"tag": "number", "value": 4},
        }
