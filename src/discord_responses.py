import random
import sys
import openai

USE_OPENAI = True


def get_response(message: str) -> str:
    p_message = message.lower()

    if USE_OPENAI:
        # openai responses
        sys.path.insert(0, '../../secret_config')
        from discord_bot_secret import OPENAI_API_TOKEN
        openai.api_key = OPENAI_API_TOKEN

        print(f"OpenAI prompt: {p_message}")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{p_message}\n",
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        print(f"OpenAI response: {response.choices[0].text}")
        return response.choices[0].text

    else:
        # basic responses
        if p_message == 'hello':
            return 'Hey there!'

        if p_message == 'roll':
            return str(random.randint(1, 6))

        if p_message == '!help':
            return '`This is a help message that you can modify.`'

        return 'I didn\'t understand what you wrote. Try typing "!help".'

