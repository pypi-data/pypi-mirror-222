import os
import time
import pexpect
from abstract_security.envy_it import find_and_read_env_file, get_env_value
import subprocess
def get_output_txt(parent_dir:str=os.getcwd()):
    return os.path.join(parent_dir,'output.txt')
def get_env_value(key:str=None,env_path:str=None):
    args={}
    if key != None:
        args["key"]=key
    if env_path != None:
        args["start_path"]=env_path
    return find_and_read_env_file(**args)
def print_cmd(input,output):
    print(f"Command Line Arguments: {input}")
    print(f"Output:\n{output}")
def get_sudo_password(key:str="SUDO_PASSWORD"):
    return find_and_read_env_file(key=key)
def cmd_run_sudo(cmd,password:str=None,key:str=None):
    if password !=None:
        cmd_run(f'echo "{password}" | sudo -S -k {cmd}')
    elif key != None:
        cmd_run(f'echo "{get_env_value(key)}" | sudo -S -k {cmd}')
    else:
        cmd_run(f'echo "{get_sudo_password()}" | sudo -S -k {cmd}')
def cmd_run(cmd):
    # Clear the output file before running the command
    with open(get_output_txt(), 'w') as f:
        pass
    cmd += f' >> '+get_output_txt()+'; echo END_OF_CMD >> '+get_output_txt()  # Add the delimiter at the end of cmd
    print(cmd)
    output = subprocess.call(f'gnome-terminal -- bash -c "{cmd}"', shell=True)
    # Wait until the delimiter appears in the output file
    while True:
        time.sleep(0.5)  # Sleep for a while to reduce CPU usage
        with open(get_output_txt(), 'r') as f:
            lines = f.readlines()
            if lines:  # Check if the file is not empty
                last_line = lines[-1].strip()  # Read the last line of the file
                if last_line == 'END_OF_CMD':
                    break  # Break the loop if the delimiter is found
    # Print the command and its output
    with open(get_output_txt(), 'r') as f:
        output = f.read().strip()  # Read the entire output
    print_cmd(cmd, output)
    print(output)
    # Delete the output file and the bash script
    os.remove(get_output_txt())
def pexpect_cmd_with_args(command, child_runs=[
    {"prompt": "Enter your username: ", "pass": None, "key": "PYPI_USERNAME", "env_path": None},
    {"prompt": "Enter your password: ", "pass": None, "key": "PYPI_PASSWORD", "env_path": None}
]):
    # Ensure the 'command' argument is a string
    command = str(command)

    child = pexpect.spawn(command)

    # Dictionary to track which prompts have been handled
    handled_prompts = {prompt["prompt"]: False for prompt in child_runs}

    while not all(handled_prompts.values()):
        # Check the return value of 'child.expect'
        expect_result = child.expect(list(handled_prompts.keys()) + [pexpect.EOF], timeout=None)

        # Handle any unexpected behavior
        if isinstance(expect_result, int):
            # If it's an int, it means 'child.expect' did not return a tuple as expected
            # Handle the error or exit the loop
            print("Unexpected behavior from 'child.expect'. Exiting the loop.")
            break

        idx, matched_obj, output = expect_result

        # Check if EOF is reached before all prompts are handled
        if idx == len(handled_prompts):
            break

        prompt_text = matched_obj.group().decode("utf-8")
        handled_prompts[prompt_text] = True

        for each in child_runs:
            if each["prompt"] == prompt_text:
                # Respond with the corresponding input
                if each["pass"] is not None:
                    pass_phrase = each["pass"]
                else:
                    args = {}
                    if each["key"] is not None:
                        args["key"] = each["key"]
                    if each["env_path"] is not None:
                        args["start_path"] = each["env_path"]

                    pass_phrase = get_env_value(**args)

                child.sendline(pass_phrase)
                break

    # Wait for the process to finish
    child.expect(pexpect.EOF)
    output = child.before.decode("utf-8")

    # Write output to the output file
    with open(get_output_txt(), "w") as f:
        f.write(output)

    print_cmd(command, output)

    return child.exitstatus
