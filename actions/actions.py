import logging
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)  # This will show logs with DEBUG level and above

class ActionForwardToNgrok(Action):
    def name(self) -> str:
        return "action_forward_to_ngrok"

    def run(self, dispatcher, tracker, domain):
        # Get the message from the user
        user_message = tracker.latest_message.get('text')

        # Log the incoming message
        logger.debug(f"tracker.latest_message = {tracker.latest_message}")
        logger.debug(f"User message received: {user_message}")

        # Check if message is empty or None
        if not user_message:
            llm_response = "No message received"
            # Log the "No message received" scenario
            logger.warning("No message received from the user.")
        else:
            # Call LLM API (using a placeholder URL for example)
            try:
                response = requests.post("https://192d-35-247-82-220.ngrok-free.app/chat", json={"message": user_message})
                if response.status_code == 200:
                    llm_response = response.json().get("response", "Sorry, I couldn't get a response.")
                    # Log the LLM response
                    logger.debug(f"LLM response: {llm_response}")
                else:
                    llm_response = "There was an error communicating with the LLM."
                    # Log error response
                    logger.error(f"Failed to get response from LLM. Status Code: {response.status_code}")
            except Exception as e:
                llm_response = "Sorry, I encountered an error while processing your request."
                # Log the exception
                logger.error(f"Error calling LLM API: {e}")

        # Send LLM response to user
        dispatcher.utter_message(text=llm_response)

        # Log the final message being sent
        logger.debug(f"Sent message to user: {llm_response}")

        return []

