import os
import subprocess

# Change these values as needed
image_name = "autogpt1d"
container_name = "autogpt_container"
host_port = 8000
container_port = 8000
repository_path = "C:\\Users\\anthr\\Documents\\GitHub\\Auto-GPT"

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error: {stderr.decode('utf-8')}")
    else:
        print(stdout.decode('utf-8'))

def main():
    # Navigate to the repository
    os.chdir(repository_path)

    # Build the Docker image
    build_command = f"docker build -t {image_name} ."
    print(f"Building Docker image with command: {build_command}")
    run_command(build_command)

    # Run the Docker container
    run_command = f"docker run --name {container_name} -d -p {host_port}:{container_port} {image_name}"
    print(f"Running Docker container with command: {run_command}")
    run_command(run_command)

if __name__ == "__main__":
    main()
