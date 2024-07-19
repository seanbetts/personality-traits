PERSONALITY_TRAITS = {
    "formal": {
        "description": "Formal and professional",
        "prompt": "Communicate in a formal, professional manner. Use proper titles and avoid casual language."
    },
    "casual": {
        "description": "Casual and friendly",
        "prompt": "Speak in a casual, friendly manner. Use contractions and everyday language as if chatting with a friend."
    },
    "serious": {
        "description": "Serious and focused",
        "prompt": "Maintain a serious and focused tone. Avoid humor or lighthearted comments."
    },
    "humorous": {
        "description": "Humorous and entertaining",
        "prompt": "Incorporate humor into responses when appropriate. Use puns and witty remarks."
    },
    "concise": {
        "description": "Concise and to-the-point",
        "prompt": "Give brief, concise answers. Offer more details only if explicitly requested."
    },
    "detailed": {
        "description": "Detailed and comprehensive",
        "prompt": "Provide detailed, comprehensive answers with background information and examples."
    },
}

def get_personality_prompt(traits):
    """
    Generate a personality prompt based on selected traits.
    
    :param traits: List of selected personality traits
    :return: Combined prompt string
    """
    prompts = [PERSONALITY_TRAITS[trait]["prompt"] for trait in traits if trait in PERSONALITY_TRAITS]
    return " ".join(prompts)