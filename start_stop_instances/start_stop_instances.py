from pathlib import Path
import typer
import boto3
from botocore.exceptions import WaiterError
from dotenv import load_dotenv
import os
from tabulate import tabulate

# Get the path to the directory containing this script
script_directory = Path(__file__).resolve().parent.parent
# print(f"Parent Path = {script_directory}")
load_dotenv(script_directory / ".env")  # Load environment variables from .env file


app = typer.Typer()

# Load AWS credentials from environment variables
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
# DEPRECATED:: aws_session_token
# aws_session_token = os.getenv("AWS_SESSION_TOKEN")
aws_region = os.getenv("AWS_DEFAULT_REGION")


def wait_for_instance_state(ec2, instance_id, desired_state):
    try:
        waiter = ec2.get_waiter(f"instance_{desired_state}")
        waiter.wait(InstanceIds=[instance_id])
        typer.echo(f"Instance is {desired_state}!")
    except WaiterError:
        typer.echo(f"Failed to {desired_state} instance.")


@app.command()
def show_instances():
    """
    Display all EC2 instances. Show Instance Id, Instance Name and Instance Status
    """

    # Create an EC2 client
    ec2 = boto3.client(
        "ec2",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        # aws_session_token=aws_session_token,
        region_name=aws_region,
    )

    # Check if AWS credentials are configured
    try:
        _instances = ec2.describe_instances()
        if "Reservations" in _instances and len(_instances["Reservations"]) > 0:
            # Get instance Ids and instance_name for all the instances
            _instance_ids = [
                i["Instances"][0]["InstanceId"] for i in _instances["Reservations"]
            ]
            _instance_names = [
                i["Instances"][0]["Tags"][0]["Value"]
                for i in _instances["Reservations"]
                if len(i["Instances"][0]["Tags"]) > 0
            ]
            _instance_states = [
                i["Instances"][0]["State"]["Name"] for i in _instances["Reservations"]
            ]

            if len(_instance_ids) == len(_instance_names) == len(_instance_states):
                _instance_metadata = [
                    [id, name, state]
                    for id, name, state in zip(
                        _instance_ids, _instance_names, _instance_states
                    )
                ]
                headers = ["InstanceId", "InstanceName", "InstanceState"]
                table = tabulate(_instance_metadata, headers=headers, tablefmt="grid")
                typer.echo(table)
        else:
            typer.echo("No instances configured for this account.")
            return
    except Exception as e:
        print(str(e))
        typer.echo(
            "AWS credentials are not configured. Please configure them using AWS CLI or environment variables."
        )
        return


@app.command()
def start_stop(instance_id: str):
    """
    Start or stop an EC2 instance.
    """
    # Create an EC2 client
    ec2 = boto3.client(
        "ec2",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        # aws_session_token=aws_session_token,
        region_name=aws_region,
    )

    # Prompt for action
    action = typer.prompt("Enter 'start' or 'stop' to perform the action")

    # Perform action
    if action == "start":
        response = ec2.start_instances(InstanceIds=[instance_id])
        typer.echo(f"Starting instance {instance_id}...")
        wait_for_instance_state(ec2, instance_id, "running")
        # Describe instance to get public IP address
        instance_description = ec2.describe_instances(InstanceIds=[instance_id])
        public_ip = instance_description["Reservations"][0]["Instances"][0][
            "PublicIpAddress"
        ]
        typer.echo(f"Public IP address: {public_ip}")
    elif action == "stop":
        response = ec2.stop_instances(InstanceIds=[instance_id])
        typer.echo(f"Stopping instance {instance_id}...")
        wait_for_instance_state(ec2, instance_id, "stopped")
        typer.echo(f"Instance {instance_id} stopped successfully")
    else:
        typer.echo("Invalid action. Use 'start' or 'stop'")


@app.command()
def show_instance_ip(instance_id: str):
    """Get Public ip of the instance

    Args:
        instance_id (str): EC2 Instance ID
    """

    # Create an EC2 client
    ec2 = boto3.client(
        "ec2",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        # aws_session_token=aws_session_token,
        region_name=aws_region,
    )

    # Check if AWS credentials are configured
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        public_ip = response["Reservations"][0]["Instances"][0]["PublicIpAddress"]
        typer.echo(f"Public IP address: {public_ip}")
    except Exception as e:
        print(str(e))
        typer.echo(
            "AWS credentials are not configured. Please configure them using AWS CLI or environment variables."
        )
        return


if __name__ == "__main__":
    app()
