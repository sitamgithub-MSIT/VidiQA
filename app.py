# Importing the requirements
import warnings
warnings.filterwarnings("ignore")

import gradio as gr
from src.app.response import describe_video


# Video, text query, and input parameters
video = gr.Video(label="Video")
query = gr.Textbox(label="Question", placeholder="Enter your question here")
temperature = gr.Slider(
    minimum=0.01, maximum=1.99, step=0.01, value=0.7, label="Temperature"
)
top_p = gr.Slider(minimum=0, maximum=1, step=0.01, value=0.8, label="Top P")
top_k = gr.Slider(minimum=0, maximum=1000, step=1, value=100, label="Top K")
max_new_tokens = gr.Slider(minimum=1, maximum=4096, step=1, value=512, label="Max Tokens")

# Output for the interface
response = gr.Textbox(label="Predicted answer", show_label=True, show_copy_button=True)

# Examples for the interface
examples = [
    [
        "./videos/sample_video_1.mp4",
        "Here are some frames of a video. Describe this video in detail.",
    ],
    [
        "./videos/sample_video_2.mp4",
        "¿Cuál es el animal de este vídeo? ¿Cuantos animales hay?",
    ],
    ["./videos/sample_video_3.mp4", "Que se passe-t-il dans cette vidéo ?"],
]

# Title, description, and article for the interface
title = "Video Question Answering"
description = "Gradio Demo for the MiniCPM-V 2.6 Vision Language Understanding and Generation model. This model can answer questions about videos in natural language. To use it, simply upload your video, type a question, and click 'submit', or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://github.com/OpenBMB/MiniCPM-V' target='_blank'>Model GitHub Repo</a> | <a href='https://huggingface.co/openbmb/MiniCPM-V-2_6' target='_blank'>Model Page</a></p>"


# Launch the interface
interface = gr.Interface(
    fn=describe_video,
    inputs=[video, query, temperature, top_p, top_k, max_new_tokens],
    outputs=response,
    examples=examples,
    cache_examples=True,
    cache_mode="lazy",
    title=title,
    description=description,
    article=article,
    theme="ParityError/Anime",
    flagging_mode="never",
)
interface.launch(debug=False)
