import os
import sys

from keyelements.src.commands import command
from keyelements.src.carparking import Parking


def run():
    parking = Parking()

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            parking_lot = Parking()
            with open(file_path, 'r') as file:
                for line in file.readlines():
                    result = command(line, parking_lot)
                    print(result)
    else:
        while True:
            cmd = input()
            if cmd:
                result = command(cmd, parking)
                print(result)


if __name__ == '__main__':
    run()
