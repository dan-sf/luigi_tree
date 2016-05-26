import argparse
import sys
import luigi
import luigi_tasks
import socket

def check_server(host, port):
    """
    Function to check if a server is up and running
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((host, port))
        return True
    except socket.error as e:
        return False
    finally:
        server.close()

def cmd_line_parser(args):
    """
    Parse cmd line args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--level', type=int, default=2,
                        help='Set the number of levels the tree will have, default is 2')
    parser.add_argument('--sleep', type=int, default=2,
                        help='Set how many seconds each task will sleep for, default is 2')
    parser.add_argument('--output-dir', type=str, default='/tmp',
                        help='Directory path to write output targets to, default is /tmp')
    parser.add_argument('--server', type=str, default='localhost',
                        help='Server the luigi scheduler is running on, default is localhost')
    parser.add_argument('--port', type=int, default=8082,
                        help='Port the luigi scheduler is running on, default is 8082')
    return parser.parse_args(args)

def main():
    """
    Run the luigi task flow
    """
    args = cmd_line_parser(sys.argv[1:])

    luigi_args = ['Root',
                  '--level', str(args.level),
                  '--sleep', str(args.sleep),
                  '--output-dir', str(args.output_dir),
                 ]

    # Run luigi in the local scheduler if the server isn't up
    if not check_server(args.server, args.port):
        luigi_args.append('--local-scheduler')

    luigi.run(luigi_args)

if __name__ == '__main__':
    main()

