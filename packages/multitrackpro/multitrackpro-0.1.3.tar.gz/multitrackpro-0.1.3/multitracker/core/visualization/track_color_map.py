from typing import Hashable


class TrackColorMap:
    """object to store and retrieve the color assigned to each object track"""

    TABLEAU_20 = [
        (31, 119, 180),
        (174, 199, 232),
        (255, 127, 14),
        (255, 187, 120),
        (44, 160, 44),
        (152, 223, 138),
        (214, 39, 40),
        (255, 152, 150),
        (148, 103, 189),
        (197, 176, 213),
        (140, 86, 75),
        (196, 156, 148),
        (227, 119, 194),
        (247, 182, 210),
        (127, 127, 127),
        (199, 199, 199),
        (188, 189, 34),
        (219, 219, 141),
        (23, 190, 207),
        (158, 218, 229),
    ]

    def __init__(self):
        self.palette_index = 0
        self.track_color_map = {}

    def get(self, track_id: Hashable):
        """Get color for the given track ID, otherwise assign the track the next color in our color palette"""
        if track_id in self.track_color_map:
            return self.track_color_map[track_id]

        self.track_color_map[track_id] = self.TABLEAU_20[self.palette_index]
        self.palette_index = (self.palette_index + 1) % 20
        color = self.track_color_map[track_id]
        return color

    def clear(self):
        self.palette_index = 0
        self.track_color_map = {}
