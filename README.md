# Start Stop Instances CLI Tool

A command-line tool to start or stop an EC2 instance using AWS credentials and Typer.

## Installation

1. Clone this repository or create a new directory for your project:

```bash
git clone https://github.com/abhinavchat-cal/start-stop-instances
cd start-stop-instances
```

## Create  a virtual environment

```bash
python -m venv env
source env/bin/activate
pip install --upgrade pip

pip install poetry
```



## Install the required dependencies using Poetry:

```bash
poetry install
```

This also installs the package as a CLI.

```bash
start-stop-instances --help
```
## Usage
### Running the CLI Tool (standalone)

- To get help

```bash
start-stop-instances --help
```
```plaintext
start-stop-instances --help                              
Usage: start-stop-instances [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  show-instance-ip  Get Public ip of the instance
  show-instances    Display all EC2 instances.
  start-stop        Start or stop an EC2 instance.
```

- View all available instances
```bash
start-stop-instances show-instances
```

```plaintext
start-stop-instances show-instances
+---------------------+-------------------------------+-----------------+
| InstanceId          | InstanceName                  | InstanceState   |
+=====================+===============================+=================+
| i-123456 | otsuka-enrollment-docker-app  | stopped         |
+---------------------+-------------------------------+-----------------+
| i-234567 | redcliffelabs_memory_instance | running         |
+---------------------+-------------------------------+-----------------+
```

- Show Public IP for an Instance
```bash
start-stop-instances show-instance-ip i-234567
```

```plaintext
start-stop-instances show-instance-ip i-234567
Public IP address: 10.1.7.32
```

- Start/Stop an Instance
```bash
start-stop-instances start-stop i-123456
```

```plaintext
start-stop-instances start-stop i-123456
Enter 'start' or 'stop' to perform the action: start
Starting instance i-123456...
Instance is running!
Public IP address: 10.1.30.72
```
### Running the CLI Tool with `poetry` or `python`

To run the CLI tool and start or stop an EC2 instance, use the following command:

```bash
poetry run start-stop-instances show-instances
poetry run start-stop-instances start-stop instance_id
```
or

```bash
python start_stop_instances/start_stop_instances.py show-instances
python start_stop_instances/start_stop_instances.py start-stop instance_id
```

Replace instance_id with the actual EC2 instance ID you want to start or stop.

For any help,

```bash
poetry run start-stop-instances --help
```

or 

```bash
python start_stop_instances/start_stop_instances.py --help
```

## AWS Credentials and Environment Variables
Make sure to configure your AWS credentials using environment variables or the AWS CLI. Additionally, you can place your AWS credentials and other environment variables in a .env file in the project root directory. An example .env file:

```plaintext
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
(deprecated) :: AWS_SESSION_TOKEN=your_session_token
```
## Script Explanation
The start_stop_instances.py script in the start_stop_instances package is the command-line tool that uses Typer to interact with AWS and perform instance actions. The configuration in `pyproject.toml` associates the script with the start-stop-instances CLI command.