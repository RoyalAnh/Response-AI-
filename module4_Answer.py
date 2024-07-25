import cohere
import os 

class CohereClient:
    def __init__(self, api_key: str):
        self.client = cohere.Client(api_key)
    
    def generate_text(self, prompt: str, max_tokens: int = 50, temperature: float = 0.75) -> str:
        """
        Sử dụng Cohere API để tạo văn bản dựa trên prompt đầu vào.

        :param prompt: Văn bản đầu vào để bắt đầu tạo văn bản.
        :param max_tokens: Số lượng token tối đa cho văn bản tạo ra.
        :param temperature: Tham số điều chỉnh mức độ sáng tạo của văn bản tạo ra.
        :return: Văn bản được tạo ra bởi Cohere API.
        """
        response = self.client.generate(
            model='command-r-plus',  
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.generations[0].text

def read_input_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

def write_output_file(file_path: str, content: str):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    API_KEY = 'API_key'  #tự viết 
    cohere_client = CohereClient(API_KEY)

    conversation_history_file = 'conversation_history.txt'
    
    # Read previous conversation history
    if os.path.exists(conversation_history_file):
        with open(conversation_history_file, 'r', encoding='utf-8') as file:
            conversation_history = file.read().strip()
    else:
        conversation_history = ""
    
    input_text = read_input_file('recognized_text.txt')
    
    # Append new input to conversation history
    prompt = conversation_history + "\nUser: " + input_text + "\nAI:"
    
    generated_text = cohere_client.generate_text(prompt)
    
    # Update conversation history
    conversation_history += "\nUser: " + input_text + "\nAI: " + generated_text
    
    with open(conversation_history_file, 'w', encoding='utf-8') as file:
        file.write(conversation_history)
    
    write_output_file('output.txt', generated_text)
    print("Generated text has been written to output.txt")

def module4():
    main()
