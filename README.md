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
## Usage
- Running the CLI Tool

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