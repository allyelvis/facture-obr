# Facture Creation and EBMS Posting

This Flask application provides a web form to create invoices (Factures) and post them to the EBMS API.

## Features

- Create invoices with customer and item details.
- Calculate total amounts before and after tax.
- Post the generated invoice to the EBMS API.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install Flask requests pydantic
    ```

## Configuration

1. Open `app.py` and replace `YOUR_EBMS_BEARER_TOKEN` with your actual EBMS bearer token:
    ```python
    EBMS_BEARER_TOKEN = "YOUR_EBMS_BEARER_TOKEN"
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Fill out the form to create an invoice. When you submit the form, the invoice will be created and posted to the EBMS API.

## File Structure
