import os
import smtplib
from email.message import EmailMessage
from app.builder import build_directive


def _get_config():
    return {
        "user": os.environ.get("EMAIL_USER"),
        "pass": os.environ.get("EMAIL_PASS"),
        "dest": os.environ.get("DEST_EMAIL"),
        "server": os.environ.get("SMTP_SERVER", "smtp.gmail.com"),
        "port": int(os.environ.get("SMTP_PORT", 465))
    }


def _print_config(config):
    print("\n--- ENV CONFIG ---")
    for key, val in config.items():
        display_val = "********" if key == "pass" and val else val
        print(f"{key.upper()}: {display_val}")


def _execute_smtp(body, file_name, config):
    _print_config(config)

    if not all([config['user'], config['pass'], config['dest']]):
        print(" [X] Missing required environment variables.")
        return

    print(f"\n [MOCK] Connecting to {config['server']}:{config['port']}...")
    print(f" [MOCK] Auth: {config['user']}")
    print(f" [MOCK] To: {config['dest']}")

    # msg = EmailMessage()
    # msg.set_content(body)
    # msg['Subject'] = f"Diretiva Gabinete: {file_name}"
    # msg['From'] = config['user']
    # msg['To'] = config['dest']
    # try:
    #     with smtplib.SMTP_SSL(config['server'], config['port']) as smtp:
    #         smtp.login(config['user'], config['pass'])
    #         smtp.send_message(msg)
    #     print(" [OK] Sent successfully!")
    # except Exception as e:
    #     print(f" [X] Send failed: {e}")

    print("\n ✅ [MOCK] Send flow simulated successfully!")


def send_mail(file_name: str, confirm: bool = False):
    config = _get_config()

    body = build_directive(file_name)
    if body is None:
        return

    if not confirm:
        print(f" [PREVIEW] To send to {config['dest']}, use --confirm")
        _print_config(config)
        return

    _execute_smtp(body, file_name, config)