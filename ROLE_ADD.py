import streamlit as st

import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
import base64
import re
#url ="https://fa-ehpv-dev40-saasfaprod1.fa.ocs.oraclecloud.com:443/xmlpserver/services/ExternalReportWSSService"
def main():
    st.title("NON PROD ROLE APP")

    # Dropdown for selecting a development environment
    selected_environment = st.selectbox("Select Development Environment", ["dev40", "dev46", "dev3"])

    # File upload for Excel file
    excel_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

    if st.button("Submit"):
        if excel_file is not None:
            # Read Excel file
            df = pd.read_excel(excel_file)
            st.success("Excel file successfully loaded.")

            # Display selected environment and DataFrame
            st.write(f"Selected Development Environment: {selected_environment}")
            a=selected_environment
            print(a)
            st.write("DataFrame from Excel:")
            st.write(df)
            takinig_details(df,a)

        else:
            st.warning("Please upload an Excel file.")



def generate_xml_payload(username, role):
    return f"""
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:pub="http://xmlns.oracle.com/oxp/service/PublicReportService">
           <soap:Header/>
           <soap:Body>
              <pub:runReport>
                 <pub:reportRequest>
                    <pub:attributeFormat>xml</pub:attributeFormat>
                    <pub:parameterNameValues>
                       <pub:item>
                          <pub:name>username</pub:name>
                          <pub:values>
                             <pub:item>{username}</pub:item>
                          </pub:values>
                        </pub:item>
                        <pub:item>
                          <pub:name>role</pub:name>
                          <pub:values>
                             <pub:item>{role}</pub:item>
                          </pub:values>
                       </pub:item>
                     </pub:parameterNameValues>
                    <pub:reportAbsolutePath>/~Yousuf.ofadmin@dpwapps.com/INT_FILES/integration-rpt.xdo</pub:reportAbsolutePath>
                    <pub:sizeOfDataChunkDownload>-1</pub:sizeOfDataChunkDownload>
                 </pub:reportRequest>
              </pub:runReport>
           </soap:Body>
        </soap:Envelope>
    """

def takinig_details(file,instance_name):
    #excel_file_path = 'C:/Users/Mohamed.Yousuf/Downloads/ROLEBOT/rolefile.xlsx'  # Replace with the actual path to your Excel file
    df = file
    instance_urls = {
        "dev40": "https://fa-ehpv-dev40-saasfaprod1.fa.ocs.oraclecloud.com:443/xmlpserver/services/ExternalReportWSSService",
        "dev46": "https://fa-ehpv-dev46-saasfaprod1.fa.ocs.oraclecloud.com:443/xmlpserver/services/ExternalReportWSSService",
        "dev60": "https://fa-ehpv-dev60-saasfaprod1.fa.ocs.oraclecloud.com:443/xmlpserver/services/ExternalReportWSSService"
    }

    selected_url = instance_urls.get(instance_name)

    if selected_url is None:
        st.warning("Invalid instance name selected.")
        return
    results = []

    for index, row in df.iterrows():
        username = row['username']
        role = row['role']

        headers = {
            'Content-Type': 'application/soap+xml; charset=utf-8',
            'Authorization': 'Basic YourBase64EncodedCredentials'  # Replace with actual Base64-encoded credentials
        }

        data = generate_xml_payload(username, role)
        #print(data)
        response = requests.post(selected_url, data=data, headers=headers, auth=HTTPBasicAuth('Yousuf.ofadmin@dpwapps.com', 'Oracle@1234$yousuf'))

        if response.status_code == 200:
            a = str(response.content)
            #print(a)
            match = re.search(r'<ns2:reportBytes>(.*?)</ns2:reportBytes>', a, re.DOTALL)

            if match:
                extracted_content = match.group(1)
                decoded_text = base64.b64decode(extracted_content).decode('utf-8')

                role_match = re.search(r'<ROLE_GUID>(.*?)</ROLE_GUID>', decoded_text)
                user_match = re.search(r'<USER_GUID>(.*?)</USER_GUID>', decoded_text)

                if role_match and user_match:
                    role_guid = role_match.group(1)
                    user_guid = user_match.group(1)
                    result_dict = {'Role': role_guid, 'USERNAME': user_guid}
                    results.append(result_dict)
                    Add_Role(user_guid,role_guid)
                    print(f"Processed row {index + 1}: {result_dict}")

                    #df = pd.DataFrame({'Role_GUID': [role_guid], 'User_GUID': [user_guid]})
                    #print(df)
                    #return df


                else:
                    print(f"Pattern not found in the response for row {index + 1}.")
            else:
                print(f"Pattern not found in the response for row {index + 1}.")
        else:
            print(f"Error for row {index + 1}:")
            print(response.content)

    if results:
        result_df = pd.DataFrame(results)
        print("\nFinal DataFrame:")
        print(result_df)
        st.write(result_df)
        return result_df
    else:
        return pd.DataFrame()
def Add_Role(user_guid, role_guid):
    payload = {"Operations":

        [

            {"method": "PATCH", "path": "/Roles/"+role_guid, "bulkId": "clientBulkId1",
             "data": {"members": [{"value": user_guid, "operation": "ADD"}]}}

        ]}

    response = requests.post('https://fa-ehpv-dev40-saasfaprod1.fa.ocs.oraclecloud.com/hcmRestApi/scim/Bulk',
                             auth=HTTPBasicAuth('Yousuf.ofadmin@dpwapps.com', 'Oracle@1234$yousuf'), json=payload)
    print(response)
if __name__ == "__main__":
    main()
