import argparse
from app.builder import build_directive
from app.files import new_file
from app.mail import send_mail

def run():
    parser = argparse.ArgumentParser(
        prog="gmcli",
        description="GMCLI — GM Command Line Interface"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("help", help="Show this help message")

    p_new = sub.add_parser("new", help="Create a new directive")
    p_new.add_argument("name", help="Directive file name (no extension)")

    p_build = sub.add_parser("build", help="Preview a built directive")
    p_build.add_argument("file", help="Directive file name (no extension)")

    p_send = sub.add_parser("send", help="Preview or send a directive")
    p_send.add_argument("file", help="Directive file name (no extension)")
    p_send.add_argument("--confirm", action="store_true", help="Send directive")

    args = parser.parse_args()

    if args.command == "help":
        parser.print_help()
    elif args.command == "new":
        new_file(args.name)
    elif args.command == "build":
        build_directive(args.file)
    elif args.command == "send":
        build_directive(args.file)
        send_mail(args.file, confirm=args.confirm)