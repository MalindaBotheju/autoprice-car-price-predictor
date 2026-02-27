import pandas as pd
import joblib
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the saved model and the column structure
# (Make sure the filename here matches your saved model file exactly)
model = joblib.load('car_model.pkl') 
model_columns = joblib.load('model_columns.pkl')

# --- DYNAMIC CATEGORY EXTRACTION ---
# 1. Brands (Ambassador was dropped because it starts with A)
brands = [col.replace('brand_', '') for col in model_columns if col.startswith('brand_')]
if 'Ambassador' not in brands: brands.append('Ambassador')
brands.sort()

# 2. Fuel Types (CNG was dropped because it starts with C)
fuels = [col.replace('fuel_', '') for col in model_columns if col.startswith('fuel_')]
if 'CNG' not in fuels: fuels.append('CNG')
fuels.sort()

# 3. Seller Types (Dealer was dropped because it starts with D)
seller_types = [col.replace('seller_type_', '') for col in model_columns if col.startswith('seller_type_')]
if 'Dealer' not in seller_types: seller_types.append('Dealer')
seller_types.sort()

# 4. Transmissions (Automatic was dropped because it starts with A)
transmissions = [col.replace('transmission_', '') for col in model_columns if col.startswith('transmission_')]
if 'Automatic' not in transmissions: transmissions.append('Automatic')
transmissions.sort()

# 5. Owners
owners = {
    'First Owner': 1,
    'Second Owner': 2,
    'Third Owner': 3,
    'Fourth & Above Owner': 4,
    'Test Drive Car': 0
}
# -----------------------------------

@app.route('/')
def home():
    # Pass all dynamic lists to the HTML
    return render_template('index.html', brands=brands, fuels=fuels, 
                           seller_types=seller_types, transmissions=transmissions, owners=owners)

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Grab the data from the HTML form
    year = int(request.form['year'])
    km_driven = int(request.form['km_driven'])
    owner = int(request.form['owner'])
    fuel = request.form['fuel']
    seller_type = request.form['seller_type']
    transmission = request.form['transmission']
    brand = request.form['brand']

    # --- NEW: Save the user's choices to send back to the web page ---
    user_input = {
        'year': year,
        'km_driven': km_driven,
        'owner': owner,
        'fuel': fuel,
        'seller_type': seller_type,
        'transmission': transmission,
        'brand': brand
    }
    # -----------------------------------------------------------------

    # 2. Create a dictionary with all 0s for every column the model expects
    input_dict = {col: 0 for col in model_columns}

    # 3. Add the numerical values
    input_dict['year'] = year
    input_dict['km_driven'] = km_driven
    input_dict['owner'] = owner

    # 4. Flip the correct 0s to 1s for the categorical data
    if f"fuel_{fuel}" in input_dict: input_dict[f"fuel_{fuel}"] = 1
    if f"seller_type_{seller_type}" in input_dict: input_dict[f"seller_type_{seller_type}"] = 1
    if f"transmission_{transmission}" in input_dict: input_dict[f"transmission_{transmission}"] = 1
    if f"brand_{brand}" in input_dict: input_dict[f"brand_{brand}"] = 1

    # 5. Convert to Pandas DataFrame
    final_df = pd.DataFrame([input_dict])

    # 6. Make Prediction
    prediction = model.predict(final_df)[0]
    
    # Format the price with commas
    formatted_price = f"₹ {int(prediction):,}"

    # Pass the prediction AND all dynamic lists back to the HTML
    return render_template('index.html', prediction_text=f"Estimated Market Value: {formatted_price}", 
                           brands=brands, fuels=fuels, seller_types=seller_types, 
                           transmissions=transmissions, owners=owners,
                           user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)