import requests
import streamlit as st


# title
st.write("OTM Validation Tool")

# user input
user_input = st.text_input("OTM message")

st.write(user_input)

# url = 'https://otm5-documentation-api.services.simacan.com/api/v5/validate/consignments'
# myobj = {
#     'goods': [
#         {
#             'entity' : {
#                 'quantity': 1,
#                 'type': 'items'
#             },
#             "associationType": "inline"
#         },
#     ],
#     "actions": [
#
#         {
#
#             "entity":
#
#                 {
#
#                     "location":
#
#                         {
#
#                             "entity":
#
#                                 {
#
#                                     "geoReference":
#
#                                         {
#                                             "street": "valutaboulevard",
#                                             "houseNumber": "16",
#                                             "postalCode": "1234AB",
#                                             "type": "addressGeoReference"
#                                         }
#                                 },
#                             "associationType": "inline"
#                         },
#                     "startTime": "2020-04-03T10:00:00Z",
#                     "actionType": "load"
#                 },
#             "associationType": "inline"
#
#         },
#         {
#
#             "entity":
#
#                 {
#
#                     "location":
#
#                         {
#
#                             "entity":
#
#                                 {
#
#                                     "geoReference":
#
#                                         {
#                                             "street": "Boris Pasternaklaan",
#                                             "houseNumber": "22",
#                                             "postalCode": "9999ZZ",
#                                             "type": "addressGeoReference"
#                                         }
#                                 },
#                             "associationType": "inline"
#                         },
#                     "startTime": "2020-04-03T10:12:00Z",
#                     "actionType": "unload"
#                 },
#             "associationType": "inline"
#         }
#
#     ],
# }
#
# x = requests.put(url, json = myobj)
# print(x.ok)
#
# print("x:",x)