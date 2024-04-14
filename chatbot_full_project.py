import openai
import gradio as gr
from datetime import datetime


openai.api_key = "sk-0000"

# Define initial state and action space
messages = [{"role": "system", "content": "You are an expert"}]

def bot(prompt, user_feedback):
    global messages  
    
    # Append user's message to conversation history
    messages.append({"role": "user", "content": prompt})
    
    # Get the chatbot's response
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    
    # Save feedback to file
    if user_feedback.strip():
        save_feedback(user_feedback)

    # Save the convversation
    save_the_conversation(prompt, response)

    # The response
    response = response.choices[0].message.content
    # Update conversation history with bot's response
    messages.append({"role": "system", "content": response})

    
    return response

def save_the_conversation(quastion, anser):
    timesramp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(r"C:\Users\moayyad\Desktop\Conversation.txt", 'a') as f:
        f.write(f"{timesramp}: {quastion} => {anser}\n")


def save_feedback(feedback):
    # Timestamp for when the feedback was received
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(r'C:\Users\moayyad\Desktop\Feedback.txt', 'a') as f:
        f.write(f"{timestamp}: {feedback}\n")
    print("Feedback saved:", feedback)

# Gradio interface
iface = gr.Interface(
    fn=bot, 
    inputs='text',   
    outputs='text', 
    title='Chatbot',
    description="Enter your message",
    additional_inputs='text') #Feedback input 

iface.launch()