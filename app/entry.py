import argparse
from app.builder import build_directive
from app.files import new_file
from app.mail import send_mail
from app.init import init_project


def run():
    parser = argparse.ArgumentParser(
        prog="gmcli",
        description="GMCLI — GM Command Line Interface"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("help", help="Show this help message")
    sub.add_parser("init", help="Initialize a GM project in the current folder")

    p_new = sub.add_parser("new", help="Create a new directive")
    p_new.add_argument("name", help="Directive file name (no extension)")
    p_new.add_argument("--template", "-t", default=None, help="Template to use")

    p_build = sub.add_parser("build", help="Preview a directive")
    p_build.add_argument("file", help="Directive file name (no extension)")

    p_send = sub.add_parser("send", help="Preview or send a directive")
    p_send.add_argument("file", help="Directive file name (no extension)")
    p_send.add_argument("--confirm", action="store_true", help="Send directive")

    args = parser.parse_args()

    if args.command == "help":
        parser.print_help()
    elif args.command == "init":
        init_project()
    elif args.command == "new":
        new_file(args.name, template=args.template)
    elif args.command == "build":
        build_directive(args.file)
    elif args.command == "send":
        send_mail(args.file, confirm=args.confirm)