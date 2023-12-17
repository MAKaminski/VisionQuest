from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QTextEdit

layout = QVBoxLayout()
textEdit = QTextEdit()
sendButton = QPushButton("Send Prompt")
layout.addWidget(textEdit)
layout.addWidget(sendButton)
window.setLayout(layout)

def on_send_button_clicked():
    prompt = textEdit.toPlainText()
    # Function to handle sending the prompt
    send_prompt_to_openai(prompt)

sendButton.clicked.connect(on_send_button_clicked)