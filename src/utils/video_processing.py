# Necessary imports
import sys
from PIL import Image
from decord import VideoReader, cpu
from typing import List

# Local imports
from src.logger import logging
from src.exception import CustomExceptionHandling


# Constants
MAX_NUM_FRAMES = 64  # If CUDA OOM, set a smaller number


def encode_video(video_path: str) -> List[Image.Image]:
    """
    Encodes a video file into a list of frames.

    Args:
        video_path (str): The path to the video file.

    Returns:
        list: A list of frames, where each frame is represented as an Image object.
    """

    def uniform_sample(l: List, n: int) -> List:
        """
        Uniformly samples elements from a list.

        Args:
            - l (list): The input list.
            - n (int): The number of elements to sample.

        Returns:
            list: A list of sampled elements.
        """
        gap = len(l) / n
        idxs = [int(i * gap + gap / 2) for i in range(n)]
        return [l[i] for i in idxs]

    try:
        # Read the video file and sample frames
        vr = VideoReader(video_path, ctx=cpu(0))
        sample_fps = round(vr.get_avg_fps() / 1)  # FPS
        frame_idx = [i for i in range(0, len(vr), sample_fps)]

        # Uniformly sample frames if the number of frames is too large
        if len(frame_idx) > MAX_NUM_FRAMES:
            frame_idx = uniform_sample(frame_idx, MAX_NUM_FRAMES)

        # Extract frames from the video
        frames = vr.get_batch(frame_idx).asnumpy()
        frames = [Image.fromarray(v.astype("uint8")) for v in frames]

        # Log the successful encoding of the video
        logging.info("Video encoded successfully.")

        # Return video frames
        return frames

    # Handle exceptions that may occur during video encoding
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
