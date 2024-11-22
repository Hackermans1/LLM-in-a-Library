# A Library with a Brain

Sallu-Bhai is the version one of the Python library that uses natural language processing (NLP) to convert natural language descriptions into actual command-line interface (CLI) commands. The library utilizes the power of the Ollama LLM (Large Language Model) to process the input and generate accurate CLI commands.

## Features

- **Natural Language to CLI Conversion**: Input a natural language description, and get the exact CLI command.
- **Dynamic Model Selection**: Automatically selects available LLM models, or you can specify a model to use.
- **Cross-Platform**: Works on Linux, macOS, and Windows environments where Ollama is installed.
- **Easy to Integrate**: Can be integrated into any existing CLI-based automation workflows.

## Installation

You can install `sallu-bhai` directly from PyPI:

```bash
pip install sallu-bhai
```
Usage
-----

### Command Line Tool

To use sallu-bhai as a CLI tool, simply run:

```   sallu-bhai "List all files in the current directory"   ```

You can also specify a model and list available models:

```sallu-bhai -m  "List all files in the current directory"  sallu-bhai -l  # List available models   ```

### Programmatic Usage

You can also use sallu-bhai programmatically:

``` from sallu_bhai.core import execute_natural_language_command  # Execute a query  command = execute_natural_language_command("List all Python files in the current directory")  print(command)  # Output: find . -name "*.py"   ```

### Options

*   \-m, --model : Specify which model to use.
    
*   \-l, --list-models: List available models in Ollama.
    
*   \-v, --version: Display the current version of the library.
    

Requirements
------------

*   Python 3.6+
    
*   Ollama installed and configured on your machine.
    

To install Ollama, follow the instructions on their official website: [Ollama](https://ollama.com/).

Troubleshooting
---------------

*   **Model not found**: Ensure that the model is available on your system. You can run ollama list to check available models or use ollama pull to pull a specific model.
    
*   **No models available**: If no models are listed, make sure Ollama is correctly installed and configured.
    

Future Upgrades
---------------

*   **Multi-Command Support**: Ability to parse multiple commands from a single input description.
    
*   **Advanced Query Parsing**: Integrating advanced NLP features to better handle more complex queries, including conditional logic.
    
*   **Improved CLI Options**: Adding more flexible command-line options for advanced users (e.g., logging, model performance tuning).
    
*   **Cloud Model Integration**: Support for running models hosted in the cloud for users without local access to heavy models.
    
*   **Custom Model Support**: Ability for users to add their custom models into the library for specific use cases.
    
*   **Error Handling Enhancements**: More comprehensive error messages to assist with troubleshooting and debugging.
    

Contributing
------------

We welcome contributions! If you have suggestions for improvements or would like to contribute new features, feel free to fork the repository, create a branch, and submit a pull request. Please ensure your code passes all tests and adheres to the existing code style.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
----------------

*   Ollama for providing the powerful models that drive this project.
    
*   Python community and open-source developers for the tools that made this possible
