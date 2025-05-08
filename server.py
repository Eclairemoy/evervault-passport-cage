from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from passporteye import read_mrz
import pycountry
import pytesseract
import os
import requests

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'images'

type_map = {
    'P': 'Passport',
    'V': 'Visa'
}

@app.route('/upload')
def upload():
    return render_template('page.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return do_mrz()

def get_validity(score):
    if score < 60:
        return "Fraudulent"
    elif score < 80:
        return "Suspicious"
    else:
        return "Valid"

@app.route("/")
def do_mrz():
    mrz = read_mrz("passport.jpg")

    mrz_data = mrz.to_dict()

    document_type = type_map[mrz_data['type'][0]]
    names = mrz_data['names']
    sex = mrz_data["sex"]
    surname = mrz_data["surname"]
    nationality = pycountry.countries.search_fuzzy(mrz_data['nationality'])[0].name
    country = pycountry.countries.search_fuzzy(mrz_data['country'])[0].name
    dob = format_dob(get_dob(mrz_data["date_of_birth"]))
    valid_dob = mrz_data["valid_date_of_birth"]
    valid_expiry_date = mrz_data["valid_expiration_date"]
    valid_number = mrz_data["valid_number"]
    validity_score = mrz_data["valid_score"]

    to_encrypt = {
        "nationality": nationality,
        "dob": dob,
        "surname": surname,
        "sex": sex
    }

    json_res = {
        "nationality": "ev:DEBUG",
        "dob": "ev:DEBUG",
        "surname": "ev:DEBUG",
        "sex": "ev:DEBUG"
    }

    # os.remove('image.jpeg')

    return_doc = {
        "DocumentType": document_type,
        "Name": names,
        "Surname": surname,
        "Nationality": nationality,
        "IssuerCountry": country,
        "DateOfBirth": dob,
        "ValidDateOfBirth": valid_dob,
        "ValidExpirationDate": valid_expiry_date,
        "ValidNumber": valid_number,
        "Validity": get_validity(validity_score),
        "ValidityScore": validity_score,
        "Sanctions": {}
    }

    if names[0:3] == 'EOQ':
        return_doc["Sanctions"] = { "program": "SDN Sanction List", "database": "us_ofac", "note": "Prefers Beamish to Guinness."}

    return return_doc

def get_dob(dob):
    n = 2
    return [dob[i:i+n] for i in range(0, len(dob), n)]

def format_dob(dob):
    return f"{dob[2]}-{dob[1]}-{dob[0]}"