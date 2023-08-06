import sys

from pistar_echo_agent.utilities.argument_parser.argument_parser import ArgumentParser
from pistar_echo_agent.utilities.server.server import Server
from pistar_echo_agent.utilities.configuration import VERSION


def main():
    """
    description: this function is used to parse the command line arguments.
    """
    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        '-p', '--port',
        action='store',
        type=int,
        default=10001,
        help='specify the port of pistar echo agent server'
    )

    argument_parser.add_argument(
        '-o', '--output',
        action='store',
        type=str,
        required=True,
        help='specify the report path of the task'
    )

    argument_parser.add_argument(
        '-v', '--version',
        action='version',
        version=VERSION,
        help='show the version of pistar-echo-agent'
    )

    arguments = argument_parser.parse_args(sys.argv[1:])

    start_server(arguments)


def start_server(arguments):
    server = Server(
        report_path=arguments.output,
        port=arguments.port
    )
    server.start()


if __name__ == "__main__":
    main()
