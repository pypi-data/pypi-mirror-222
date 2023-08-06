# Below is version 1 of the client side pythonGPT code, which isn't optimized, but should hopefully serve as a proof of principle.

import IPython
import requests
from IPython.display import display, Markdown
from time import sleep

#####security######
ACCESS_CODE = "python@future!"
initialized = False

def initialize(user_code):
    global initialized
    if user_code != ACCESS_CODE:
        raise PermissionError("Invalid access code!")
    initialized = True

def _ensure_initialized():
    if not initialized:
        raise PermissionError("Module not initialized. Call `initialize()` with the access code first.")
#####security######

current_cell_has_delayed_output = False  # Initialize the variable b/c it's used in two defs

BASE_URL = 'https://pythongpt-de5fb0514677.herokuapp.com'
ip = IPython.get_ipython()

history = []


def ask_gpt4(prompt):
    _ensure_initialized()  # Make sure the module is initialized before proceeding
    try:
        # Initiate the request
        response = requests.post(f'{BASE_URL}/gpt-4', json={"prompt": prompt, "history": history})
        #print("HISTORY: " + str(history))
        response.raise_for_status()  # Check for HTTP errors.
        response_json = response.json()

        # Wait for the response from the threaded function
        while True:
            check_response = requests.get(f'{BASE_URL}/get-response/{response_json["id"]}')
            if check_response.json()["status"] == "completed":
                response_text = check_response.json()["response"]
                break
            sleep(2)  # Wait for 2 seconds before checking again

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return
    except Exception as err:
        print(f"Other error occurred: {err}")
        return

    # Append the GPT-4 response to the history
    history.append({"role": "assistant", "content": response_text})

    # Display the response text with proper formatting
    display(Markdown(response_text))


# IF more functions besides ask_gpt4 are added to this we need to include them below keyword list
DELAYED_OUTPUT_KEYWORDS = ["ask_gpt4", "requests.post",
                           "requests.get"]  # Add any other keyword that might indicate delayed output


def pre_run_cell_handler(info):
    """Capture the cell input before it's executed."""
    global current_cell_has_delayed_output  # Declare the variable as global
    input_content = info.raw_cell
    current_cell_has_delayed_output = any(keyword in input_content for keyword in DELAYED_OUTPUT_KEYWORDS)
    history.append({"role": "user", "content": input_content})


def post_run_cell_handler(info):
    """Capture the cell output after it's executed."""
    global current_cell_has_delayed_output  # Declare the variable as global

    # Get the last executed cell number
    last_cell_number = len(ip.user_ns["In"]) - 1

    # Check if the output corresponds to the most recent input cell
    if last_cell_number in ip.user_ns["Out"]:
        latest_output = str(ip.user_ns["Out"][last_cell_number])
    else:
        # Only append "no output..." if we are not expecting delayed output
        if not current_cell_has_delayed_output:
            latest_output = "no output or output only visible in notebook"
        else:
            return  # If it's a delayed output, we don't append anything at this point

    # Append the latest output to history
    history.append({"role": "assistant", "content": latest_output})


# Register the events
#ip.events.register('pre_run_cell', pre_run_cell_handler)
#ip.events.register('post_run_cell', post_run_cell_handler)

def register_events():
    ip = IPython.get_ipython()
    ip.events.register('pre_run_cell', pre_run_cell_handler)
    ip.events.register('post_run_cell', post_run_cell_handler)


# The new function to add a problem statement to history
def problem_statement(statement: str):
    history.append({"role": "user", "content": "I am working on this Problem: " + statement})
