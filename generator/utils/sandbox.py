import sys
import io

def test_algorithm(code_string: str, test_call: str) -> str:
    """
    Executes generated code in an isolated environment and returns the console output.
    WARNING: For a public web app, wrap this in a Docker container to prevent malicious code execution.
    """
    safe_env = {}
    
    # Capture standard output (print statements)
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    
    try:
        # Load the algorithm into the safe environment
        exec(code_string, safe_env)
        # Run a test execution of the algorithm
        exec(test_call, safe_env)
    except Exception as e:
        print(f"Sandbox Execution Error: {e}")
    finally:
        # Restore normal standard output
        sys.stdout = old_stdout
        
    return redirected_output.getvalue()
  
