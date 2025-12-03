# Quickstart for Calculator UI

This guide explains how to set up and run the Calculator UI application.

## Prerequisites

- Python 3.9
- pip

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies**:
    Create a `requirements.txt` file with the following content:
    ```
    streamlit
    pytest
    ```
    Then run:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  **Start the Streamlit app**:
    ```bash
    streamlit run src/app.py
    ```

2.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## Running Tests

1.  **Execute pytest**:
    ```bash
    pytest
    ```
