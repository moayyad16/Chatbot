import openai 
openai.api_key = "sk-0000"


# openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!"}])
def bot(prompt):
    response = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages=[{"role": "assistant", "content": prompt}]) # Each object has a role (either "system", "user", or "assistant") and content
    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'see you', 'goodbye']:
            print("Bot: Goodbye! Have a great day!")
            break
        response = bot(user_input)
        print('Bot: ', response)