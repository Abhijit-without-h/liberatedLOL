from dsk.api import DeepSeekAPI

# Initialize with your auth token
api = DeepSeekAPI("YOUR_AUTH_TOKEN_HERE")

# Create a new chat session
chat_id = api.create_chat_session()

# Simple chat completion
prompt = "What is Python?"
for chunk in api.chat_completion(chat_id, prompt):
    if chunk['type'] == 'text':
        print(chunk['content'], end='', flush=True)
