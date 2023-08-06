from typing import List, Tuple

import cv2
import numpy as np


def get_shape(frame: np.ndarray) -> np.ndarray:
    return np.tile(frame.shape[-2::-1], 2)


def plot_bboxes_color(frame: np.ndarray, bboxes: np.ndarray, colors: List[Tuple[int, int, int]]):
    H, W = frame.shape[:2]
    shape = np.array([W, H, W, H])
    for (bbox, color) in zip(bboxes, colors):
        plot_box(frame, bbox, shape, color)


def plot_box(frame, box, shape=None, color=(255, 255, 255), border=True):
    plot(frame, box, shape, color, cv2.rectangle, border)


def plot(frame, points, shape=None, color=(255, 255, 255), function=None, border=True):
    if shape is None:
        shape = get_shape(frame)

    points = np.multiply(points, shape).astype('int')
    if border:
        function(frame, *map(tuple, points.reshape(2, 2)), 0, 4)
    function(frame, *map(tuple, points.reshape(2, 2)), color, 2)