import openai
import gradio

openai.api_key = "sk-0000"

messages = [{"role": "system", "content": "You are an experts"}]
def bot(prompt):
    messages.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages=messages)
    
    return response.choices[0].message.content

WEB = gradio.Interface(fn=bot, inputs='text', outputs='text', title='Chat Bot')
WEB.launch()