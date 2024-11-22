from sallu_bhai.core import SalluBhai

# Initialize with a default model
sallu = SalluBhai()

# Test fetching the available model
print("Selected model:", sallu.get_available_model())

# Test converting a natural language query into a CLI command
try:
    command = sallu.get_cli_command("Find all Python files in the current directory")
    print("Generated CLI Command:", command)
except Exception as e:
    print("Error:", e)
