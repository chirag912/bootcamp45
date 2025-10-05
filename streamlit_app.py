import openai
import streamlit as st

# Retrieve the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

def generate_invoice_description(customer_name, product, quantity, unit_price, invoice_amount):
    prompt = f"Generate an invoice description for the customer '{customer_name}' who purchased {quantity} units of {product} at {unit_price} per unit, totalling {invoice_amount}."
    
    # Make a call to OpenAI to generate the description
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Or use "" for better output
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    
    # Return the generated invoice description
    return response.choices[0].text.strip()

def calculate_invoice_amount(quantity, unit_price):
    return quantity * unit_price

# Streamlit UI
st.title("AI-Powered Invoice Generator")

# User input form
customer_name = st.text_input("Customer Name")
product = st.text_input("Product")
quantity = st.number_input("Quantity", min_value=1)
unit_price = st.number_input("Unit Price", min_value=0.0, format="%.2f")

if st.button("Generate Invoice"):
    # Calculate the invoice amount
    invoice_amount = calculate_invoice_amount(quantity, unit_price)

    # Generate the invoice description using OpenAI
    invoice_description = generate_invoice_description(customer_name, product, quantity, unit_price, invoice_amount)

    # Display results
    st.subheader("Invoice Summary")
    st.write(f"**Customer Name**: {customer_name}")
    st.write(f"**Product**: {product}")
    st.write(f"**Quantity**: {quantity}")
    st.write(f"**Unit Price**: ${unit_price}")
    st.write(f"**Invoice Amount**: ${invoice_amount}")
    st.write(f"**Invoice Description**: {invoice_description}")
