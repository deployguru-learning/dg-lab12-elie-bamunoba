# dg-lab12-elie-bamunoba
## This Python script performs automatic backups of a specified directory and sends notifications via email and Slack upon completion.
=======
README_CONTENT = """
# Backup Script README

## Introduction
This Python script performs automatic backups of a specified directory and sends notifications via email and Slack upon completion.

## Features
- Creates a backup of a specified directory.
- Sends an email notification with a CSV attachment containing backup details.
- Sends a Slack notification with backup details in JSON format.

## Prerequisites
- Python 3.6 or latest installed.
- Required Python packages:
  - `requests`
  - `smtplib`
  - `email`
- Access to a Gmail account for sending email notifications.
- Access to a Slack webhook URL for sending Slack notifications.

## Setup
1. Clone or download this repository to your local machine.
2. Install the required Python packages using pip:
     ```
     pip install requests
     ```
3. Configure your Gmail account:
   - Update the `smtp_username` and `smtp_password` variables in the script with your Gmail credentials.
4. Configure your Slack webhook:
   - Update the `webhook_url` variable in the script with your Slack webhook URL.
5. Customize backup settings:
   - You can modify the `source_dir` and `dest_dir` variables in the `create_backup` function to specify the source and destination directories for backup.

## Usage
1. Run the script:
     ```
     python script.py
     ```
2. The script will create a backup of the specified directory and send email and Slack notifications upon completion.

## Contact
For any issues or questions, please contact Elie at eliebamunoba@gmail.com
"""

