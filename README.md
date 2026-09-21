# Nugen AI Knowledge Assistant

A lightweight AI application built as part of the **Nugen Intelligence hands-on assessment**.

The project demonstrates integration with a deployed Nugen aligned model, programmatic inference, evaluation, and development of a simple AI application using Python.

## Overview

The application sends user questions to a deployed Nugen model through the Nugen API and displays:

- Generated answer
- Confidence score
- Prompt token usage
- Completion token usage
- Total token usage

The project also includes an evaluation workflow containing multiple domain-specific questions to test the model's understanding and identify potential limitations.

## Architecture

```text
User Question
      ↓
Python Application
      ↓
Nugen API
      ↓
Deployed Aligned Model
      ↓
Answer + Confidence Score + Token Usage
```

## Project Structure

```text
nugen-assessment/
│
├── app.py
├── test_inference.py
├── evaluation_questions.json
├── requirements.txt
├── .gitignore
├── README.md
├── .env
└── .venv/
```

> `.env` and `.venv/` are excluded from Git and should never be committed.

## Technologies Used

- Python
- Nugen API
- REST API
- Requests
- python-dotenv
- JSON
- PowerShell

## Setup

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure the API key

Create a `.env` file in the project root:

```env
NUGEN_API_KEY=your_api_key_here
```

Do not commit the `.env` file or expose the API key publicly.

## Run the Application

```powershell
python app.py
```

The application will prompt:

```text
Ask a question:
```

Enter a question and the application will send it to the deployed Nugen model.

The response includes:

- Answer
- Confidence score
- Prompt tokens
- Completion tokens
- Total tokens

## Model Evaluation

An evaluation dataset containing 8 questions was created to test:

1. Normal RAG understanding
2. RAG pipeline
3. Retrieval methods
4. RAG failure modes
5. RAG vs fine-tuning
6. Ambiguous terminology
7. Retrieved-context quality
8. Simple workflow vs multi-agent system

Run the evaluation with:

```powershell
python test_inference.py
```

## Evaluation Findings

The evaluation demonstrated that the deployed model can provide relevant answers to several RAG-related questions.

However, it also exposed an important limitation: the acronym **RAG** can be interpreted in unrelated ways.

During testing, the model interpreted RAG as:

- Retrieval-Augmented Generation
- Relational Algebra
- Reliability, Availability, and Maintainability
- Regularization and Generalization

This happened even when the model returned relatively high confidence scores.

### Important Observation

A high confidence score does not necessarily mean that the answer is correct for the intended domain.

For example, some incorrect interpretations received confidence scores above 80%.

This demonstrates why model evaluation should consider actual answer correctness and domain relevance rather than relying only on a confidence score.

## Key Results

### Successful

- Nugen platform setup completed.
- API key configured successfully.
- Domain documents uploaded.
- Alignment project created successfully.
- Aligned model deployed successfully.
- API authentication verified.
- Inference endpoint tested successfully.
- Automated evaluation implemented.
- Working Python application created.
- Confidence score and token usage captured from API responses.

### Observed Limitation

The main limitation identified during testing was **domain ambiguity around the acronym "RAG"**.

The model performed well when the question explicitly established the intended meaning, but ambiguous or certain RAG-related questions could trigger unrelated interpretations.

This finding was discovered through targeted evaluation rather than assuming that successful API responses automatically represented successful domain alignment.

## Design Decision

The application intentionally remains lightweight.

The goal of the assessment was to demonstrate:

- Understanding of the Nugen platform
- API integration
- Model deployment and inference
- Evaluation methodology
- Practical AI application development
- Ability to identify model limitations

A large frontend, database, multi-agent architecture, or unnecessary framework dependencies were intentionally avoided because they were not required for the assessment objective.

## Security

API credentials are stored in `.env`.

The `.gitignore` file excludes:

```text
.env
.venv/
__pycache__/
*.pyc
```

Never commit API keys, tokens, or other secrets to the repository.

## Future Improvements

Possible future improvements include:

- Adding explicit domain context to ambiguous queries
- Expanding the evaluation dataset
- Adding automated answer-quality evaluation
- Adding structured logging
- Adding retry and error-handling strategies
- Building a lightweight web interface if required

These improvements were kept outside the current assessment scope to maintain a focused implementation.

## Assessment Outcome

This project demonstrates an end-to-end workflow:

```text
Domain Documents
      ↓
Nugen Alignment
      ↓
Model Deployment
      ↓
API Integration
      ↓
Inference
      ↓
Evaluation
      ↓
Failure Analysis
      ↓
Working AI Application
```

The assessment was approached as an engineering exercise: the model was tested, its behavior was analyzed, and limitations were documented rather than hidden.
