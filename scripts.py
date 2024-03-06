import os, shutil,  smtplib,  requests,  json, csv, logging
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Email Notification method

def send_email_notification(backup_folder):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'eliebamunoba@gmail.com'
    smtp_password = 'wxut whkf kddi ipgr'

    from_email = 'eliebamunoa@gmail.com'
    to_emails = ['etb2808@gmail.com', 'eliebamunoba243@gmail.com', 'felix@deployguru.com']
    subject = 'Backup Server Notification'
    formatted_date = datetime.now().strftime("%a %d/%m/%Y %I:%M %p") + " UTC"
    
    # Creating CSV content with clear column titles
    csv_content = "Status,Backup Time,Backup Path\n"
    csv_content += f"Backup Completed,{formatted_date},{backup_folder}\n"
    
    # Email body
    body = f"The server has been successfully backed up.\n\n"
    
    # Create a MIME multipart message
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] =", ".join(to_emails) 
    message['Subject'] = subject
    
    # Attach the body
    message.attach(MIMEText(body, 'plain'))
    
    # Attach the CSV file
    filename = os.path.basename(backup_folder) + '.csv'
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(csv_content)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename={filename}')
    message.attach(attachment)
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.sendmail(from_email, to_emails, message.as_string())
        print("Email Successfully sent")
    except Exception as error:
        print(f'Something went Wrong\n {error}')

# Slack Notification 

def notify_slack(backup_dir_name):
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Set the logger level to INFO

    # Configure the logger to output log messages in JSON format
    logging.basicConfig(format='%(message)s', level=logger.level)

    # Test messages with structured logging in JSON format
    logger.info(json.dumps({"timestamp": "current_timestamp", "level": "INFO", "message": "This is an info message", "module": "main", "function": "example_function"}))
    
    now = datetime.now()
    formatted_date=now.strftime("%a %d/%m/%Y %I:%M %p") + ' UTC'
    webhook_url = 'https://hooks.slack.com/services/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'
    notification = {
        "Notification_by": "Elie Bamunoba",
        "Backup_time": formatted_date,
        "Backup_path": backup_dir_name
      
    }
    message_payload = {"text": f"```json\n{json.dumps(notification, indent=4)}\n```"}
    
    response = requests.post(webhook_url, json=message_payload)
    
    if response.status_code == 200:
        print("Slack notification sent successfully")
    else:
        print(f"Failed to send slack notification, status code: {response.status_code} {response.message}")

# Backup Method

def create_backup(source_dir="/var/www/html", dest_dir="/opt/backups"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = os.path.join(dest_dir, timestamp)

    try:
        os.makedirs(backup_folder)
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            dest_item = os.path.join(backup_folder, item)
            if os.path.isdir(source_item):
                shutil.copytree(source_item, dest_item)
            else:
                shutil.copy2(source_item, dest_item)
        
        send_email_notification(backup_folder)
        notify_slack(backup_folder)
        print(f"Backup completed successfully to {backup_folder}")
        
    except FileNotFoundError as e:
        print(f"Error: Source directory '{source_dir}' not found.")
    except PermissionError as e:
        print(f"Error: Permission denied while creating backup directory '{backup_folder}'.")
    except shutil.Error as e:
        print(f"Error: Failed to copy files to backup directory '{backup_folder}'.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    create_backup()

