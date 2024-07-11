from flask import Flask, render_template, request, jsonify
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List
import requests

app = Flask(__name__)

class Item(BaseModel):
    product_code: str
    description: str
    quantity: int
    unit_price: float
    total_price: float

class Facture(BaseModel):
    invoice_number: str
    date: datetime
    customer_name: str
    customer_address: str
    customer_nif: str
    items: List[Item]
    total_ht: float
    tax_rate: float
    total_ttc: float
    payment_method: str
    company_nif: str
    company_vat_subject: bool

EBMS_API_URL = "https://ebms.obr.gov.bi:9443/ebms_api/getInvoice"
EBMS_BEARER_TOKEN = "YOUR_EBMS_BEARER_TOKEN"

def post_to_ebms(facture: Facture):
    headers = {
        "Authorization": f"Bearer {EBMS_BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(EBMS_API_URL, headers=headers, json=facture.dict())
    return response.status_code, response.text

@app.route('/', methods=['GET', 'POST'])
def facture_form():
    if request.method == 'POST':
        invoice_number = request.form['invoice_number']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        customer_name = request.form['customer_name']
        customer_address = request.form['customer_address']
        customer_nif = request.form['customer_nif']
        items = [
            Item(
                product_code=request.form['product_code'],
                description=request.form['description'],
                quantity=int(request.form['quantity']),
                unit_price=float(request.form['unit_price']),
                total_price=float(request.form['total_price'])
            )
        ]
        total_ht = float(request.form['total_ht'])
        tax_rate = float(request.form['tax_rate'])
        total_ttc = total_ht * (1 + tax_rate)
        payment_method = request.form['payment_method']
        company_nif = request.form['company_nif']
        company_vat_subject = 'company_vat_subject' in request.form

        facture = Facture(
            invoice_number=invoice_number,
            date=date,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_nif=customer_nif,
            items=items,
            total_ht=total_ht,
            tax_rate=tax_rate,
            total_ttc=total_ttc,
            payment_method=payment_method,
            company_nif=company_nif,
            company_vat_subject=company_vat_subject
        )

        status_code, response_text = post_to_ebms(facture)
        if status_code == 200:
            return f"Facture Created and Posted Successfully: {facture.json(indent=2)}"
        else:
            return f"Failed to Post Facture: {response_text}", status_code

    return render_template('facture_form.html')

if __name__ == '__main__':
    app.run(debug=True)
