"""DailyThread Python Starter - entry point."""
import ast
from pathlib import Path


def scan_code_tree(file_path: str) -> dict:
    """Scan Python file and return AST structure."""
    with open(file_path, "r") as f:
        tree = ast.parse(f.read(), filename=file_path)
    
    functions = []
    classes = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
    
    return {
        "file": file_path,
        "functions": functions,
        "classes": classes,
        "total_nodes": sum(1 for _ in ast.walk(tree))
    }


def main() -> None:
    """Main entry point."""
    print("Hello from python-starter with AST scanning!")
    
    # Scan this file
    result = scan_code_tree(__file__)
    print(f"Found {len(result['functions'])} functions and {len(result['classes'])} classes")
    print(f"Total AST nodes: {result['total_nodes']}")


if __name__ == "__main__":
    main()
