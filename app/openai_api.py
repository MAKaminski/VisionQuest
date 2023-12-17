import requests

def send_prompt_to_openai(prompt):
    api_key = 'YOUR_OPENAI_API_KEY'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        'model': 'text-davinci-003',  # Or another model
        'prompt': prompt,
        'max_tokens': 150
    }
    response = requests.post('https://api.openai.com/v1/engines/davinci/completions', json=data, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        # Handle the response (e.g., show it in the UI)
    else:
        # Handle error
        
def handle_openai_response(response_data):
# Update the UI with the response
# This could be showing the response in a new widget or a dialog

# Update the on_send_button_clicked function to handle the response
def on_send_button_clicked():
    prompt = textEdit.toPlainText()
    response_data = send_prompt_to_openai(prompt)
    handle_openai_response(response_data)