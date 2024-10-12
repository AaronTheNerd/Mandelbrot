Color = list[int]


def get_colormap(name: str) -> list[Color]:
    colormaps = {
        "plain": [[255, 255, 255]],
        "candy": [[255, 0, 0], [255, 255, 255]],
        "wiki": [
            [0, 7, 100],
            [32, 107, 203],
            [237, 255, 255],
            [255, 170, 0],
            [0, 2, 0],
        ],
    }
    return colormaps[name] if name in colormaps else colormaps["plain"]
