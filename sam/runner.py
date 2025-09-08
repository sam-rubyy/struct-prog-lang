import sys
import tokenizer 
import parser 
import evaluator 

def run(text):
    tokens = tokenizer.tokenize(text)
    ast = parser.parse(tokens)
    result = evaluator.evaluate(ast)
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            src = f.read()
        run(src)
    else:
        print("Usage: python runner.py <filename>")