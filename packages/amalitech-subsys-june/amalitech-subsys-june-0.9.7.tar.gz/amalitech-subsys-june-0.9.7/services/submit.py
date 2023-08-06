import base64
import click
import datetime
from pathlib import Path
import requests

from utils.misc import read_config, update_submission_id
from utils.snap import get_snap_files_content


# Function to submit a specific snap to the server
def submit_snap(snap_id, session_cookie):
    snap_object = Path(".subsys") / "objects" / f"sn_{snap_id}"

    with snap_object.open() as snap_file:
        snap_content = snap_file.read()

    snap_files_content = get_snap_files_content(snap_id)
    parent_snap_id = None

    for line in snap_content.splitlines():
        if line.startswith("Parent:"):
            parent_snap_id = line.split(":", 1)[1].strip()
            break

    slug = None
    for line in snap_content.splitlines():
        if line.startswith("Slug:"):
            slug = line.split(":", 1)[1].strip()
            break

    config = read_config()
    author = config.get("DEFAULT", "StudentID", fallback="") 
    assignment = config.get("DEFAULT", "Code", fallback="")
    submission_id = config.get("DEFAULT", "SubmissionID", fallback="")

    snap_data = {
        "snap": str(snap_id),  # Converted to string
        "Parent": parent_snap_id,
        "Date": datetime.datetime.now().isoformat(),  # Converted to string
        "Slug": slug
    }

    # Converted snap_files_content values to Base64 format
    base64_snap_files_content = {
        str(key): base64.b64encode(value).decode("utf-8")
        for key, value in snap_files_content.items()
    }

    data = {
        "assignment": assignment,
        "author": author,
        "file_contents": base64_snap_files_content,
        "snap_content": snap_data,
        "snap_id": snap_id,
        "submission_id": submission_id,
    }

    headers = {
        "Cookie": f"connect.sid={session_cookie}"
    }

    api_url = "https://gitinspired-june-api.amalitech-dev.net/api/cli/submit"
    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 200:
        # Access the 'data' attribute of the 'response' object
        response_data = response.json().get("data")
        submission_id = response_data.get("submission_id")
        if submission_id:
            update_submission_id(submission_id)

        click.echo(f"Snapshot {slug} submitted successfully.")
    else:
        click.echo(f"Failed to submit snapshot> {slug}.")