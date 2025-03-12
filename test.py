from openai import OpenAI

# Initialize the OpenAI client with the API key
client = OpenAI()

# WRITE YOUR CODE HERE

# Generating response
def get_bot_response(user_input):
    prompt = f"Please provide a response to the following user input: '{user_input}'"

    response = openai.Completion.create(model="gpt-4o-mini",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    bot_response = response.choices[0].text.strip()
    return bot_response
