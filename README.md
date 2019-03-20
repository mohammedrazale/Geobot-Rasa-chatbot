# Geobot-Rasa-chatbot
A simple chat bot using Rasa_NLU and Rasa core 
It could give you the geocoordinates of location by the help of open street map data

What is Rasa

Rasa is an open source Conversational AI framework. What I like about Rasa is you are not tied to a pre-built model or usecase (Dialogflow etc.). So you can customize it to your usecase which can be a market differentiator. Rasa is not a rule based framework (e.g. Botkit) and you don’t need to worry about putting your data in someone else’s cloud as in Dialogflow, Microsoft LUIS or Amazon Lex.

Rasa has two main components — Rasa NLU and Rasa Core.

How to use this repo

This is how to use it:
Training the NLU model

To train and test the model run:
 
    python nlu_model.py

Training the Rasa Core model


Start the custom action server by running:

    python -m rasa_core_sdk.endpoint --actions actions

Open a new terminal and train the Rasa Core model by running:

    python dialogue_management_model.py

Talk to the chatbot once it's loaded.




Reference:
An excellent tutorial from Justina on how to build a simple Chatbot using Rasa,
Rasa core and Rasa NLU documentation,
Open street map Nominatim
