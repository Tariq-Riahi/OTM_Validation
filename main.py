import json

import requests
import streamlit as st
import json


# title
st.write("OTM Validation Tool")

# options
option = st.selectbox(
    'Which OTM message do you want to validate?',
    ('consignments', 'transportOrders', 'goods'))

# user input
user_input = st.text_input("OTM message")

# validate button
validate = st.button('Validate', type='primary')


if validate:
    myobj = json.loads(user_input)

    url = 'https://otm5-documentation-api.services.simacan.com/api/v5/validate/' + option
    resp = requests.put(url, json = myobj)

    if resp.ok:
        st.write("Your OTM5 message is valid.")
    else:
        st.write(resp.text)
