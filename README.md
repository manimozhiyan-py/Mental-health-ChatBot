# `Mental Health Chatbot with LLM Integration`
---
This project aims to create a sophisticated mental health chatbot using cutting-edge language models and Rasa for intelligent conversation management. The chatbot is designed to provide empathetic and context-aware responses to users facing emotional distress, making it a supportive tool for mental wellness. The project integrates various technologies including fine-tuning of LLaMA-2, API integration with Flask and Ngrok, custom action endpoints, and a user-friendly interface built with Streamlit.

## `Key Features`

- Context-aware responses for sensitive topics.
    
- Modular design for easy scalability and customization.
    
- Real-time communication through Rasa’s action server.
    
- Seamless integration with LLM for personalized responses.
    
- Modern, minimalistic user interface with Streamlit.
    

## Project Modules

1. **Fine-Tuning (LLM with LLaMA-2)** - Customizing the language model to understand mental health contexts better.
    
2. **API Integration (Flask and Ngrok)** - Bridging the frontend and backend for real-time communication.
    
3. **Rasa** - Powerful NLU framework for intent classification and response generation.
    
4. **Custom Action Endpoint** - Integrating personalized responses from the LLM into Rasa workflows.
    
5. **User Interface with Streamlit** - Simple, intuitive web interface for seamless user interaction.
    

## Installation

1. Clone the repository.
    
2. Set up a virtual environment and install required packages.
    
3. Configure the LLM API and Rasa server.
    
4. Run the Streamlit frontend.
    

```bash
# Clone the repository
git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot

# Set up virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

- Run the Rasa server:
	

```bash
rasa run --enable-api
```

- Start the action server:(in another terminal)
    

```bash
rasa run actions
```

- Launch the Streamlit interface:(in another terminal)
    

```bash
streamlit run app.py
```

## Architecture

The chatbot follows a modular architecture:

- Rasa for intent recognition and dialogue management.
    
- Custom action server for generating LLM responses.
    
- Streamlit for frontend presentation.
    

## Future Improvements

- Add sentiment analysis for mood-based response variation.
    
- Integrate voice support for a more natural user experience.
    
- Improve response generation with enhanced context tracking.
    
- Implement a feedback system for continuous improvement.
    

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for enhancements.

## License

This project is licensed under the MIT License.