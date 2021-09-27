import os
import argparse

from _constants import *

from totcommon.executable import TOTExecutable

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Automates cubemap generation in-game.')

    parser.add_argument('input', type=ascii,
                        help='The name of the map to build (without extension).')

    parser.add_argument('-e', '--exe', required=True,
                        metavar='path', type=ascii, default='',
                        help='Where the game .exe is located')
    parser.add_argument('-g', '--game', required=True,
                        metavar='path', type=ascii, default='',
                        help='The mod folder to be loaded')

    parser.add_argument('-s', '--steam', metavar='path', type=ascii,
                        nargs='?', default=None, const=None,
                        help='Where the steam.exe is located')
    parser.add_argument('-a', '--appid',  metavar='N', type=int,
                        nargs='?', default=None, const=None,
                        help='The steam AppId to be launched')

    parser.add_argument('-v', '--version', action='version', version=VERSION)

    args = parser.parse_args()

    with TOTExecutable(NAME, ORGNAME, URL, VERSION, BUILD_DATE):

        mapName = eval(args.input)
        gameExe = os.path.normpath(eval(args.exe))
        gameDir = os.path.normpath(eval(args.game))

        if (args.steam):
            steamExe = os.path.normpath(eval(args.steam))
        else:
            steamExe = None

        steamId = args.appid
