# PromptEngine

PromptEngine is a Python library that provides an interface for conducting interview sessions using OpenAI's ChatGPT model. It allows you to interact with the AI assistant to simulate interview conversations and generate responses based on candidate input.

## Installation

You can install PromptEngine using pip:
pip install promptengine


## Prerequisites

Before using PromptEngine, make sure you have the following:

- Python 3.6 or higher
- OpenAI API key
- .env file having following info:
  OPENAI_API_KEY = "Your-key"
  LOG_MODE=DEBUG

## Usage

Here's an example of how to use PromptEngine:

import promptengine

# Create a PromptEngine instance
prompt_engine = promptengine.PromptEngine(redis_instance)

# Store user data for an interview session
interview_id = "interview-1"
username = "John Doe"
position = "Software Engineer"
skills = "Python, JavaScript"
job_description = "A software engineer responsible for developing web applications."
experience = "5 years of experience in software development."

prompt_engine.store_user_data(
    interview_id,
    username,
    position,
    skills,
    job_description,
    experience
)

# Conduct an interview conversation
state = "ONGOING"
candidate_input = "Tell me about your team management experience."

system_message = prompt_engine.chatAI(interview_id, state, candidate_input)

# Convert voice to text
audio_file = "interview_audio.wav"
transcription = prompt_engine.voiceToText(audio_file)

For detailed API documentation and usage examples, please refer to the documentation.

# Contributing
Contributions to PromptEngine are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
PromptEngine was inspired by the need to automate interview simulations and make the process more efficient and interactive.

# Contact
For any questions or inquiries, please contact akybharat02@gmail.com.

We hope you find PromptEngine useful! Enjoy conducting interview sessions with AI assistance.