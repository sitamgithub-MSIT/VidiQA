# VidiQA

Video Question Answering is the task of answering open-ended questions based on a video clip. They output natural language responses to natural language questions about the content of a video clip. This project uses one of the popular multimodal models, [**MiniCPM-V-2_6**](https://huggingface.co/openbmb/MiniCPM-V-2_6) from the Hugging Face model hub for video question answering.

[**MiniCPM-V-2_6**](https://huggingface.co/openbmb/MiniCPM-V-2_6) is the latest model in the MiniCPM-V series, built on **SigLip-400M** and **Qwen2-7B** with a total of 8B parameters. It introduces new features for multi-image and video understanding. It also supports multilingual capabilities and produces fewer tokens than most models, improving inference speed, first-token latency, memory usage, and power consumption. It is easy to use in various ways, including CPU inference, quantized models, and online demos.

## Project Structure

The project is structured as follows:

- `src`: The folder that contains the source code for the project.

  - `app`: The folder that contains the source code for the main functionality of the application.

    - `model.py`: The file that contains the code for loading the model and the tokenizer.
    - `response.py`: The file that contains the function for generating the response for the input video and question.

  - `utils`: The folder that contains the utility function for the project.
    - `video_processing.py`: This file contains the functions for processing the video input.

  - `config.py`: This file contains the configuration for the used model.
  - `logger.py`: This file contains the logging configuration for the project.
  - `exception.py`: This file contains the exception handling for the project.

- `app.py`: The main file that contains the Gradio application for video question answering.
- `requirements.txt`: The file containing the project's required dependencies.
- `LICENSE`: The license file for the project.
- `README.md`: The README file that contains information about the project.
- `assets`: The folder that contains the screenshots for working on the application.
- `images`: The folder that contains the images for testing the application.

## Tech Stack

- Python (for the programming language)
- PyTorch (for the deep learning framework)
- Hugging Face Transformers Library (for the visual question-answering model)
- Gradio (for the web application)
- Hugging Face Spaces (for hosting the gradio application)

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/VidiQA.git`
2. Change the directory: `cd VidiQA`
3. Create a virtual environment: `python -m venv tutorial-env`
4. Activate the virtual environment: `tutorial-env\Scripts\activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run the Gradio application: `python app.py`

Now, open up your local host and see the web application running. For more information, please refer to the Gradio documentation [here](https://www.gradio.app/docs/interface). Also, a live version of the application can be found [here](https://huggingface.co/spaces/sitammeur/VidiQA).

**Note**: The application is hosted on Hugging Face Spaces running on a GPU. For local use, you are expected to have a GPU for running the application. If you do not have a GPU, you can explore the CPU inference option provided by the model [here](https://huggingface.co/collections/openbmb/minicpm-65d48bf958302b9fd25b698f).

## Usage

The web application allows you to upload a video and input a question. The model will analyze the video frames and generate an answer based on the content of the video and the question. This can assist in video summarization, enhance video retrieval by identifying specific scenes or actions, and support visually impaired individuals by describing video content. The application is also useful in educational settings for providing detailed explanations or context based on video material.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you want to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀
