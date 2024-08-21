# Necessary imports
import sys
from typing import Any, Dict
import spaces

# Local imports
from src.utils.video_processing import encode_video
from src.config import (
    device,
    model_name,
    system_prompt,
    sampling,
    stream,
    top_p,
    top_k,
    temperature,
    repetition_penalty,
    max_new_tokens,
)
from src.app.model import load_model_and_tokenizer
from src.logger import logging
from src.exception import CustomExceptionHandling


# Model and tokenizer
model, tokenizer = load_model_and_tokenizer(model_name, device)


@spaces.GPU(duration=120)
def describe_video(video: str, question: str) -> str:
    """
    Describes a video by generating an answer to a given question.

    Args:
        - video (str): The path to the video file.
        - question (str): The question to be answered about the video.

    Returns:
        str: The generated answer to the question.
    """
    try:
        # Encode the video frames
        frames = encode_video(video)

        # Message format for the model
        msgs = [{"role": "user", "content": frames + [question]}]

        # Set decode params for video
        params: Dict[str, Any] = {
            "use_image_id": False,
            "max_slice_nums": 1,  # Use 1 if CUDA OOM and video resolution > 448*448
        }

        # Generate the answer
        answer = model.chat(
            image=None,
            msgs=msgs,
            tokenizer=tokenizer,
            sampling=sampling,
            stream=stream,
            top_p=top_p,
            top_k=top_k,
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            max_new_tokens=max_new_tokens,
            system_prompt=system_prompt,
            **params
        )

        # Log the successful generation of the answer
        logging.info("Answer generated successfully.")

        # Return the answer
        return "".join(answer)

    # Handle exceptions that may occur during answer generation
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
