import os
import sys
# import the unpack module
from wowsunpack import WoWsUnpack

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s <path to WoWs folder>" % sys.argv[0])
        sys.exit(1)
    game_path = sys.argv[1]
    unpack = WoWsUnpack(game_path)
    unpack.reset()
    unpack.unpackGameParams()
    unpack.decodeGameParams()

    unpack.unpackGameMaps()
    unpack.decodeLanguages()

    unpack.unpackGameIcons()
    unpack.packAppAssets(output_path='app/assets')
