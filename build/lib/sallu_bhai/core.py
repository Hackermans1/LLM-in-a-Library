import subprocess
from ollama import chat


class SalluBhai:
    """
    A library for converting natural language to CLI commands using Ollama's chat functionality.
    """

    def __init__(self, model=None):
        """
        Initialize the library with a model.
        If `-n` is passed, it selects an available model dynamically.
        
        :param model: The name of the LLM model hosted on Ollama.
                      If None, defaults to the first available model or a predefined model.
        """
        if model == "-n":
            self.model = self.get_available_model()
        else:
            self.model = model or "qwen2.5-coder:0.5b-instruct-q4_0"

    @staticmethod
    def get_available_model() -> str:
        """
        Fetches available models using `ollama list` and returns the first available one.

        :return: The name of the first available model.
        :raises RuntimeError: If no models are available or the command fails.
        """
        try:
            # Run the `ollama list` command to get available models
            result = subprocess.run(
                ["ollama", "list"], capture_output=True, text=True, check=True
            )
            models = [line.strip() for line in result.stdout.strip().split("\n") if line]
            
            # Extract model names and pick the first one
            if models:
                return models[0]  # Select the first model
            else:
                raise RuntimeError("No models available on the Ollama server.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to fetch models: {e.stderr.strip()}") from e
        except Exception as e:
            raise RuntimeError(f"An error occurred while listing models: {e}") from e

    def set_model(self, model_name: str):
        """
        Update the model used by the library.
        
        :param model_name: The new model name to use.
        """
        self.model = model_name


    def get_cli_command(self, natural_language: str) -> str:
        """
        Sends the natural language description to the LLM and retrieves the corresponding CLI command.

        :param natural_language: The natural language input.
        :return: The cleaned CLI command as a string.
        :raises RuntimeError: If the API call fails or the response format is unexpected.
        """
        messages = [
            {
                "role": "user",
                "content": (
                    "You are an assistant that converts natural language into CLI commands.\n"
                    "Translate the following description into an exact CLI command:\n\n"
                    f"{natural_language}\n\n"
                    "Only output the command, without any additional explanation."
                )
            }
        ]
    
        try:
            # Call Ollama's chat API with the given model and messages
            response = chat(model=self.model, messages=messages)
            
            # Extract the CLI command from the response
            cleaned_text = response.get("message", {}).get("content", "").strip()
            if not cleaned_text:
                raise ValueError("The response content is empty.")
            return cleaned_text
        except KeyError:
            raise RuntimeError("Unexpected response format from Ollama chat.")
        except Exception as e:
            raise RuntimeError(f"Error communicating with Ollama chat: {e}")

def execute_natural_language_command(query, model="default"):
    """
    Sends a natural language description to the LLM and retrieves the corresponding CLI command.
    
    :param query: The natural language description of the desired CLI command.
    :param model: The LLM model to use.
    :return: The CLI command as a string.
    """
    sallu = SalluBhai(model=model)
    return sallu.get_cli_command(query)
def list_models():
    """
    Lists available models on the Ollama server.
    
    :return: A list of available model names.
    """
    return SalluBhai.get_available_model()
