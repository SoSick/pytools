# encoding: utf-8
#
# doesn't work
#
import os
import argparse
from inc import EPILOG

def ParseCommandLine():
    parser = argparse.ArgumentParser(
        description="Change current directory to target folder.",
        epilog=EPILOG,
        )
    parser.add_argument(
        "folder",
        metavar="FOLDER",
        nargs=1,
        help="Target folder.",
        )
    return parser, parser.parse_args()

def Main():
    parser, opt = ParseCommandLine()
    folder = opt.folder[0]
    
    if os.path.isdir(folder):
        os.chdir(folder)
    else:
        print("%s is not a folder."%(folder))
        os.sys.exit(1)

if __name__ == '__main__':
    Main()
