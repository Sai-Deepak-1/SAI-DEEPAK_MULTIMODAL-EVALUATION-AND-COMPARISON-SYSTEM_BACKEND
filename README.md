# Multimodal Evaluation and Comparison System

## Overview
The Multimodal Evaluation and Comparison System is a Python-based backend system designed to evaluate and compare multiple language models on various natural language processing (NLP) tasks. This project helps in analyzing the performance of different models, thereby aiding in model selection for specific use cases.

## Features
- RESTful API implementation using FastAPI
- Integration of 4-5 different pre-trained language models from Hugging Face Transformers, such as BERT, RoBERTa, DistilBERT, ALBERT, XLNet, and T5
- Endpoints for:
  - Text Classification
  - Named Entity Recognition (NER)
  - Question Answering
  - Text Summarization
- Endpoint for submitting text input and task type, returning results from all models for that task
- Caching mechanism to store model outputs and improve response times for repeated queries
- Benchmarking feature to run models on provided datasets and return performance metrics (accuracy, F1 score, BLEU score)
- Proper error handling and input validation
- /health endpoint to return service status and usage statistics
- Logging to track usage, performance, and errors
- Rate limiting feature to prevent API abuse
- Bonus features:
  - Simple credential system for API access authorization
  - Endpoint to upload and compare user fine-tuned models

## Requirements
- Python 3.7+
- FastAPI
- Hugging Face Transformers library
- Additional Python libraries as specified in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SAI-DEEPAK_MULTIMODAL-EVALUATION-AND-COMPARISON-SYSTEM_BACKEND.git
   cd SAI-DEEPAK_MULTIMODAL-EVALUATION-AND-COMPARISON-SYSTEM_BACKEND
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

2. Access the API endpoints:
   - `POST /classify`: Text Classification
   - `POST /ner`: Named Entity Recognition (NER)
   - `POST /qa`: Question Answering
   - `POST /summarize`: Text Summarization
   - `POST /evaluate`: Submit text input and task type for model evaluation
   - `GET /benchmark`: Run benchmarking on provided datasets
   - `GET /health`: Check service status and usage statistics

## API Endpoints

- **Text Classification**
- **Named Entity Recognition (NER)**
- **Question Answering**
- **Text Summarization**
- **Evaluate**
- **Benchmark**
- **Health Check**

## Contribution

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
