QueryPDF AI

PDF AI is an intelligent application that automatically answers questions about the contents of PDF files. By leveraging advanced natural language processing techniques and OpenAI embeddings, PDF AI provides accurate responses to user queries.
Features

    Automatic Question Answering: Simply upload your PDF file, and PDF AI will process the text and generate answers to your questions.
    Text Chunking: PDF AI breaks down the PDF text into smaller, manageable chunks for efficient processing.
    Semantic Similarity Matching: The application identifies text chunks that are semantically similar to the user's question, ensuring accurate and relevant responses.
    User-Friendly Interface: PDF AI comes with a user-friendly graphical interface powered by Streamlit, allowing easy interaction and seamless usage.

Technologies Used

    Python
    OpenAI Embeddings
    Streamlit
    PyPDF2
    Langchain

Installation

    Clone the repository:

bash

git clone https://github.com/your-username/pdf-ai.git

    Install the required dependencies:

bash

pip install -r requirements.txt

    Set up the OpenAI API key:

    Rename the .env.example file to .env.
    Open the .env file and replace YOUR_OPENAI_API_KEY with your actual OpenAI API key.

Usage

    Run the application:

bash

streamlit run app.py

    Access the application by opening the provided URL in your browser.

    Upload your PDF file using the provided file uploader.

    Ask questions about the PDF content using the text input field.

    PDF AI will generate the answers based on the uploaded PDF file and display them on the interface.

Contributing

Contributions to PDF AI are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.
License

This project is licensed under the MIT License.