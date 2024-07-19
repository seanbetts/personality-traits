import chainlit as cl
from personality_traits import PERSONALITY_TRAITS, get_personality_prompt
import openai

# Initialize OpenAI client (make sure to set your API key in the environment variables)
openai.api_key = "your-openai-api-key"  # Replace with your actual API key

@cl.on_chat_start
async def start():
    # Send initial message and trait selection options
    await cl.Message(content="Welcome! Please select personality traits for your AI assistant.").send()
    
    trait_options = [
        cl.Option(value=trait, label=PERSONALITY_TRAITS[trait]["description"])
        for trait in PERSONALITY_TRAITS
    ]
    
    res = await cl.AskForSelect(
        content="Choose personality traits:",
        options=trait_options,
        multi=True
    )
    
    if res:
        selected_traits = res
        personality_prompt = get_personality_prompt(selected_traits)
        await cl.Message(content=f"You've selected: {', '.join(selected_traits)}").send()
        await cl.Message(content="Great! Your AI assistant is ready. How can I help you?").send()
        
        # Store the personality prompt in the user session
        cl.user_session.set("personality_prompt", personality_prompt)
    else:
        await cl.Message(content="No traits selected. Using default personality.").send()

@cl.on_message
async def main(message: cl.Message):
    # Retrieve the personality prompt from the user session
    personality_prompt = cl.user_session.get("personality_prompt", "")
    
    # Construct the full prompt
    full_prompt = f"""
    You are an AI assistant with the following personality traits:
    {personality_prompt}

    Please respond to the user's message accordingly.

    User: {message.content}
    AI Assistant:"""

    # Call OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=full_prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Send the response back to the user
    await cl.Message(content=response.choices[0].text.strip()).send()