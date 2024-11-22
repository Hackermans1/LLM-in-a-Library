# cli_tool.py
import argparse
from sallu_bhai.core import execute_natural_language_command, list_models


def main():
    parser = argparse.ArgumentParser(
        description="Sallu-Bhai: Convert natural language to CLI commands using Ollama."
    )

    parser.add_argument(
        "query", 
        nargs="?", 
        help="The natural language query to convert into a CLI command."
    )

    parser.add_argument(
        "-m", "--model", 
        type=str, 
        default="qwen2.5-coder:0.5b-instruct-q4_0",
        help="Specify the model to use. Default is 'default'."
    )

    parser.add_argument(
        "-l", "--list-models", 
        action="store_true", 
        help="List all available models in Ollama."
    )

    parser.add_argument(
        "-v", "--version", 
        action="store_true", 
        help="Show the current version of sallu-bhai."
    )

    args = parser.parse_args()

    if args.version:
        print("Sallu-Bhai version 0.1.0")
        return

    if args.list_models:
        print("Fetching available models...")
        models = list_models()
        print("\n".join(models))
        return

    if args.query:
        print(f"Processing query: {args.query}")
        try:
            result = execute_natural_language_command(args.query, args.model)
            print(f"Generated CLI Command: {result}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("No query provided. Use -h for help.")
