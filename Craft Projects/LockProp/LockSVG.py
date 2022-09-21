try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

BOARD_WIDTH = "60cm"
BOARD_HEIGHT = "60cm"
BOARD_SIZE = (BOARD_WIDTH, BOARD_HEIGHT)
dwg.add()
