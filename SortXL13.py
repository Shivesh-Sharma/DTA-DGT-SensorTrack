import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO
import random
import subprocess
import os
import time
# Ensure wkhtmltopdf is installed
if not os.path.exists('setup.sh'):
    st.warning("wkhtmltopdf is not installed. Running setup script...")
    subprocess.run(['bash', 'setup.sh'], check=True)
import pdfkit

st.set_page_config(page_title="DTA-DGT_SensorTrack", layout="wide")

# Placeholder for the OTP (in a real application, this should be handled more securely)
otp_placeholder = st.empty()

# Initial username and password
initial_username = 'RILDTA'
initial_password = 'Rilfng@1234'

# Session state initialization
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'password' not in st.session_state:
    st.session_state.password = initial_password
if 'username' not in st.session_state:
    st.session_state.username = initial_username
if 'otp' not in st.session_state:
    st.session_state.otp = ''
if 'page' not in st.session_state:
    st.session_state.page = 'login'
if 'track_option' not in st.session_state:
    st.session_state.track_option = 'sensor_procurement'

# Function to send OTP
def send_otp():
    st.session_state.otp = str(random.randint(100000, 999999))
    otp_placeholder.text(f"Your OTP is: {st.session_state.otp}")  # This simulates sending the OTP

# Function to render the login form
def login():
    st.markdown("""
    <style>
    .login-form {
        max-width: 400px;
        margin: auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .login-form h2 {
        text-align: center;
        color: #004d99;
    }
    .login-form input {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .login-form button {
        width: 100%;
        padding: 10px;
        background-color: #004d99;
        border: none;
        color: white;
        border-radius: 5px;
        cursor: pointer;
    }
    .login-form button:hover {
        background-color: #003366;
    }
    .login-form .links {
        text-align: center;
        margin-top: 10px;
    }
    .login-form .links a {
        color: #004d99;
        text-decoration: none;
        margin: 0 10px;
    }
    .login-form .links a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="login-form">
        <h2>DTA-DGT SensorTrack Login</h2>
    """, unsafe_allow_html=True)

    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login", key="login_button"):
        if username == st.session_state.username and password == st.session_state.password:
            st.session_state.logged_in = True
            st.session_state.page = 'selection'
            st.success("Logged in successfully")
            st.rerun()  # Ensure the app reruns to reflect the state change
        else:
            st.error("Invalid username or password")

    # Hidden buttons to handle page changes
    if st.button("Change Password", key="change-password-link", on_click=lambda: change_page('change_password')):
        st.experimental_rerun()

    if st.button("Forgot Password", key="forgot-password-link", on_click=lambda: change_page('forgot_password')):
        st.experimental_rerun()

# Function to change the page
def change_page(page):
    st.session_state.page = page

# Function to render the change password form
def change_password():
    st.markdown("""
    <style>
    .change-password-form {
        max-width: 400px;
        margin: auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .change-password-form h2 {
        text-align: center;
        color: #004d99;
    }
    .change-password-form input {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .change-password-form button {
        width: 100%;
        padding: 10px;
        background-color: #004d99;
        border: none;
        color: white;
        border-radius: 5px;
        cursor: pointer;
    }
    .change-password-form button:hover {
        background-color: #003366;
    }
    </style>
    <div class="change-password-form">
        <h2>Change Password</h2>
    """, unsafe_allow_html=True)

    old_password = st.text_input("Old Password", type="password", key="change_old_password")
    new_password = st.text_input("New Password", type="password", key="change_new_password")
    confirm_password = st.text_input("Confirm New Password", type="password", key="change_confirm_password")
    if st.button("Change Password", key="change_password_button"):
        if old_password == st.session_state.password:
            if new_password == confirm_password:
                st.session_state.password = new_password
                st.success("Password changed successfully")
            else:
                st.error("New passwords do not match")
        else:
            st.error("Old password is incorrect")

    if st.button("Go to Login"):
        st.session_state.page = 'login'
        st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# Function to render the forgot password form
def forgot_password():
    st.markdown("""
    <style>
    .forgot-password-form {
        max-width: 400px;
        margin: auto;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .forgot-password-form h2 {
        text-align: center;
        color: #004d99;
    }
    .forgot-password-form input {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .forgot-password-form button {
        width: 100%;
        padding: 10px;
        background-color: #004d99;
        border: none;
        color: white;
        border-radius: 5px;
        cursor: pointer;
    }
    .forgot-password-form button:hover {
        background-color: #003366;
    }
    </style>
    <div class="forgot-password-form">
        <h2>Forgot Password</h2>
    """, unsafe_allow_html=True)

    phone_number = st.text_input("Enter your phone number", key="forgot_phone_number")
    if st.button("Send OTP", key="forgot_send_otp"):
        send_otp()
    otp = st.text_input("Enter OTP", key="forgot_otp")
    new_password = st.text_input("New Password", type="password", key="forgot_new_password")
    confirm_password = st.text_input("Confirm New Password", type="password", key="forgot_confirm_password")
    if st.button("Reset Password", key="forgot_reset_password"):
        if otp == st.session_state.otp:
            if new_password == confirm_password:
                st.session_state.password = new_password
                st.success("Password reset successfully")
            else:
                st.error("New passwords do not match")
        else:
            st.error("Invalid OTP")

    if st.button("Go to Login"):
        st.session_state.page = 'login'
        st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# Function to render the selection page
def selection_page():
    st.markdown("""
    <style>
    .selection-page {
        max-width: 600px;
        margin: 100px auto;
        padding: 30px;
        background-color: #ffffff;
        border-radius: 20px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
        text-align: center;
    }
    .selection-page h2 {
        color: #004d99;
        font-size: 36px;
        font-family: 'Arial', sans-serif;
        position: relative;
        animation: fadeIn 1s ease-in-out;
        animation-delay: 0.5s;
    }
    .selection-page h2::after {
        content: '';
        display: block;
        width: 100%;
        height: 3px;
        background-color: #004d99;
        position: absolute;
        bottom: -10px;
        left: 0;
        transform: scaleX(0);
        transition: transform 0.3s ease-in-out;
    }
    .selection-page h2:hover::after {
        transform: scaleX(1);
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    <div class="selection-page">
        <h2>Select an option</h2>
    </div>
    """, unsafe_allow_html=True)

    columns = st.columns((20,20))

    with columns[0]:
        sensor_procurement = st.button("Sensor Procurement", use_container_width=True, key="sensor_procurement" )
    with columns[1]:
        sensor_replacement = st.button("Sensor Replacement", use_container_width=True, key="sensor_replacement" )


    if sensor_procurement:
        st.session_state.track_option = 'sensor_procurement'
        st.session_state.page = 'main'
        st.rerun()

    if sensor_replacement:
        st.session_state.track_option = 'sensor_replacement'
        st.session_state.page = 'main'
        st.rerun()

# Function to render the main page
def main():
    # Custom logo and title
    st.write("""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <img src="https://1000logos.net/wp-content/uploads/2021/08/Reliance-Industries-Limited-RIL-Logo.jpg" width="200" height="125" style="margin-bottom: 10px;">
        </div>
        """, unsafe_allow_html=True)

    html_string = '<h1>DTA_DGT-SensorTrack</h1>'
    st.markdown(html_string, unsafe_allow_html=True)
    subheader_text = "Procurement" if st.session_state.track_option == 'sensor_procurement' else "Replacement"
    html_string = f'<h2 class="subheader"><em>Precision Tracking for Seamless Sensor Procurement and Replacement</em></h2>'
    st.markdown(html_string, unsafe_allow_html=True)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = 'login'
        st.rerun()

    with st.expander("How to Use This App"):
        st.markdown("""
            Welcome to DTA_DGT-SensorTrack! Here's a step-by-step guide to help you navigate through the app:

            **1. Upload Your Excel File**
            - Click on the 'Choose an Excel file' button.
            - Select the Excel file from your local storage.

            **2. Filter Your Data**
            - Use the filters on the sidebar to narrow down your data:
              - **Plant**: Select the plant from the dropdown menu.
              - **Make**: Choose the make of the sensor.
              - **Model**: Pick the model of the sensor.
              - **Gas Type**: Select the type of gas.
              - **Date Range**: Select the procurement or replacement date range.

            **3. View and Download Filtered Data**
            - The filtered data will be displayed on the main page.
            - Use the checkboxes to show the filtered data, completed procurements/replacements, or remaining procurements/replacements.
            - You can remove columns by selecting them in the multiselect dropdown.
            - Use the 'Download Options' in the sidebar to download the filtered data in Excel or PDF format.

            **4. Manage Your Account**
            - Use the buttons to log out, change password, or reset password if needed.

        """)



    def local_css():
        css = """
        <style>
        body {
            font-family: "Arial", sans-serif;
            background-color: #f5f5f5;
        }
        h1, h2, h3 {
            color: #004d99;
        }
        .subheader {
            margin-right: 100px;  /* Adjust this value to shift more or less */
        }
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

    local_css()

    uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")
    if uploaded_file:
        df = pd.read_excel(uploaded_file)

        # Convert 'Sensor Validity' to datetime
        df['Sensor Validity'] = pd.to_datetime(df['Sensor Validity'], format='%Y-%m-%d', errors='coerce')

        # Ensure 'Sensor Procurement' is numeric and then convert to datetime
        df['Sensor Procurement'] = pd.to_numeric(df['Sensor Procurement'], errors='coerce')
        df['Sensor Procurement'] = pd.to_datetime(df['Sensor Procurement'], origin='1899-12-30', unit='D', errors='coerce')

        # Directly convert 'Sensor Replacement Date' to datetime
        df['Sensor Replacement Date'] = pd.to_datetime(df['Sensor Replacement Date'], format='%m/%d/%Y', errors='coerce')

        st.write("## Uploaded Data Preview:")
        st.dataframe(df, height=250, width=1200)
        
        st.sidebar.header("Filtering Preferences")

        plant = st.sidebar.selectbox("Select Plant", ['All'] + df['PLANT'].unique().tolist())
        make = st.sidebar.selectbox("Select Make", ['All'] + df['MAKE'].unique().tolist())
        model = st.sidebar.selectbox("Select Model", ['All'] + df['MODEL'].unique().tolist())
        gas_type = st.sidebar.selectbox("Select Gas Type", ['All'] + df['GAS TYPE'].unique().tolist())

        date_label = "Sensor Procurement" if st.session_state.track_option == 'sensor_procurement' else "Sensor Replacement Date"

        if st.session_state.track_option == 'sensor_replacement':
            replacement_option = st.sidebar.selectbox("Replacement Option", ['See Current Replacements', 'See Future Replacements'])

            if replacement_option == 'See Current Replacements':
                date_label = "Sensor Replacement Date"
                output_text = "Replacements Done"
            else:
                date_label = "Sensor Validity"
                output_text = "Upcoming Replacements"


        date_range = st.sidebar.date_input(f"Select {date_label} Range", [])

        filtered_df = df.copy()
        if plant != 'All':
            filtered_df = filtered_df[filtered_df['PLANT'] == plant]
        if make != 'All':
            filtered_df = filtered_df[filtered_df['MAKE'] == make]
        if model != 'All':
            filtered_df = filtered_df[filtered_df['MODEL'] == model]
        if gas_type != 'All':
            filtered_df = filtered_df[filtered_df['GAS TYPE'] == gas_type]

        if date_range:
            if len(date_range) == 2:
                start_date, end_date = date_range
                filtered_df = filtered_df[(filtered_df[date_label] >= pd.Timestamp(start_date)) & (filtered_df[date_label] <= pd.Timestamp(end_date))]

        if st.session_state.track_option == 'sensor_replacement':
            if replacement_option == 'See Current Replacements':
                st.sidebar.write(f"### {output_text}: {filtered_df.shape[0]}")
            else:
                if len(date_range) == 2:
                    st.sidebar.write(f"### {output_text}: {filtered_df.shape[0]}")
        else:
            st.sidebar.write(f"### Total Procurements Count: {filtered_df.shape[0]}")

        # Making copy of filtered data to avoid errors
        trimmed_filtered_df = filtered_df

        if st.checkbox("Show Filtered Data"):
            # Multiselect dropdown for selecting columns to display or remove
            display_or_exclude = st.radio(
                "Choose whether to display or exclude columns:",
                options=["Display columns", "Exclude columns"],
                key="display_exclude_option"
            )
            if display_or_exclude == "Display columns":
                # Multiselect dropdown for selecting columns to display
                columns_to_display = st.multiselect(
                    "Select columns to display:",
                    options=trimmed_filtered_df.columns.tolist(),
                    key="Filtered_DF"
                )

                if columns_to_display:
                    # Filter the DataFrame to include only the selected columns
                    trimmed_filtered_df = trimmed_filtered_df[columns_to_display]


            else:
                # Multiselect dropdown for selecting columns to remove
                columns_to_remove = st.multiselect(
                    "Select columns to remove:",
                    options=trimmed_filtered_df.columns.tolist()
                )

                # Remove selected columns
                trimmed_filtered_df = trimmed_filtered_df.drop(columns=columns_to_remove)

            # Display the DataFrame
            st.dataframe(trimmed_filtered_df, height=250, width=1200)

        # Calculate the counts based on the selected tracking option
        if st.session_state.track_option == 'sensor_procurement':
            procurement_done_data = filtered_df[filtered_df['procurement done'] == 'Y']
            procurement_left_data = filtered_df[filtered_df['procurement done'] == 'N']
            total_procurement_done = procurement_done_data.shape[0]
            total_procurement_left = procurement_left_data.shape[0]
            st.sidebar.write(f"### Procurements Completed: {total_procurement_done}")
            st.sidebar.write(f"### Procurements Pending: {total_procurement_left}")

            # Making copy of Procurement done data to avoid errors
            trimmed_procurement_done = procurement_done_data

            # Making copy of Procurement left data to avoid errors
            trimmed_procurement_left = procurement_left_data


            if st.checkbox("Show completed procurements"):

                # Multiselect dropdown for selecting columns to display or remove
                display_or_exclude1 = st.radio(
                    "Choose whether to display or exclude columns:",
                    options=["Display columns", "Exclude columns"],
                    key="display_exclude_option1"
                )
                if display_or_exclude1 == "Display columns":
                    # Multiselect dropdown for selecting columns to display
                    columns_to_display1 = st.multiselect(
                        "Select columns to display:",
                        options=trimmed_procurement_done.columns.tolist(),
                        key="procurements_done1"
                    )

                    if columns_to_display1:
                        # Filter the DataFrame to include only the selected columns
                        trimmed_procurement_done = trimmed_procurement_done[columns_to_display]



                else:
                    # Multiselect dropdown for selecting columns to remove
                    columns_to_remove1 = st.multiselect(
                        "Select columns to remove:",
                        options=trimmed_procurement_done.columns.tolist(),
                        key="procurements_done"
                    )

                    # Remove selected columns
                    trimmed_procurement_done = trimmed_procurement_done.drop(columns=columns_to_remove1)

                # Display the DataFrame
                st.dataframe(trimmed_procurement_done, height=250, width=1200)

            if st.checkbox("Show remaining procurements"):

                # Multiselect dropdown for selecting columns to display or remove
                display_or_exclude2 = st.radio(
                    "Choose whether to display or exclude columns:",
                    options=["Display columns", "Exclude columns"],
                    key="display_exclude_option2"
                )
                if display_or_exclude2 == "Display columns":
                    # Multiselect dropdown for selecting columns to display
                    columns_to_display2 = st.multiselect(
                        "Select columns to display:",
                        options=trimmed_procurement_left.columns.tolist(),
                        key="procurements_left1"
                    )

                if columns_to_display2:
                    # Filter the DataFrame to include only the selected columns
                    trimmed_procurement_done = trimmed_procurement_done[columns_to_display]

                else:
                    # Multiselect dropdown for selecting columns to remove
                    columns_to_remove2 = st.multiselect(
                        "Select columns to remove:",
                        options=trimmed_procurement_left.columns.tolist(),
                        key="procurements_left"
                    )

                    # Remove selected columns
                    trimmed_procurement_left = trimmed_procurement_left.drop(columns=columns_to_remove2)

                # Display the DataFrame
                st.dataframe(trimmed_procurement_left, height=250, width=1200)



        def convert_df_to_excel(df):
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')

            date_columns = ['Sensor Replacement Date','Sensor Validity', 'Sensor Procurement']
            for col in date_columns:
                if col in df.columns:
                    df[col] = df[col].dt.strftime('%Y-%m-%d')

            df.to_excel(writer, index=False, sheet_name='Sheet1')

            workbook  = writer.book
            worksheet = writer.sheets['Sheet1']

            center_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})

            for column in df:
                column_width = max(df[column].astype(str).map(len).max(), len(column)) + 2
                col_idx = df.columns.get_loc(column)
                worksheet.set_column(col_idx, col_idx, column_width, center_format)

            writer.close()
            processed_data = output.getvalue()
            return processed_data

        def convert_df_to_pdf(df):
            start_time = time.time()
            date_columns = ['Sensor Validity', 'Sensor Procurement']
            for col in date_columns:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], errors='coerce')

            for col in date_columns:
                if col in df.columns:
                    df[col] = df[col].dt.strftime('%Y-%m-%d')

            html = f"""
            <html>
            <head>
                <style>
                    table {{
                        width: 100%;
                        border-collapse: collapse;
                    }}
                    th, td {{
                        border: 1px solid black;
                        padding: 5px;
                        text-align: left;
                        word-wrap: break-word;
                    }}
                    th {{
                        background-color: #f2f2f2;
                        text-align: center;
                    }}
                    td:nth-child({df.columns.get_loc('Sensor Validity') + 1}) {{
                        min-width: 100px;
                    }}
                </style>
            </head>
            <body>
                <h1 style="text-align: center;">DTA-DGT_Report</h1>
                {df.to_html(index=False)}
            </body>
            </html>
            """
            path_to_wkhtmltopdf = '/usr/bin/wkhtmltopdf'
            config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

            html_ready_time = time.time()
            print(f"Time to prepare HTML: {html_ready_time - start_time} seconds")

            pdf = pdfkit.from_string(html, False, configuration=config)

            pdf_ready_time = time.time()
            print(f"Time to generate PDF: {pdf_ready_time - html_ready_time} seconds")
            return pdf

        # Sidebar for download options
        st.sidebar.header("Export Options")

        # Dropdown for selecting data type based on track_option
        if st.session_state.track_option == 'sensor_procurement':
            data_option = st.sidebar.selectbox(
                "Select Data to Download",
                options=[
                    "Filtered Data",
                    "Procurements Completed",
                    "Procurements Pending"
                ]
            )
        elif st.session_state.track_option == 'sensor_replacement':
            data_option = "Filtered Data"
            
        # Dropdown for selecting file format
        format_option = st.sidebar.selectbox(
            "Select File Format",
            options=["Excel", "PDF"]
        )

        # Prepare the data based on the selected option
        if data_option == "Filtered Data":
            data = trimmed_filtered_df
        if st.session_state.track_option == 'sensor_procurement':
            if data_option == "Procurements Done":
                data = trimmed_procurement_done
            if data_option == "Procurements Left":
                data = trimmed_procurement_left
        elif st.session_state.track_option == 'sensor_replacement':
            if data_option == "Replacements Done":
                data = trimmed_replacement_done
            if data_option == "Replacements Left":
                data = trimmed_replacement_left

        # Convert the data to the selected format
        if format_option == "Excel":
            file_data = convert_df_to_excel(data)
            file_name = 'Filtered DGT Data.xlsx'
            mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        else:  # PDF
            file_data = convert_df_to_pdf(data)
            file_name = 'Filtered DGT Data.pdf'
            mime_type = 'application/pdf'

        # Display the download button
        st.sidebar.download_button(
            label=f"Download {format_option} file",
            data=file_data,
            file_name=file_name,
            mime=mime_type
        )



if __name__ == "__main__":
    if st.session_state.page == 'login':
        login()
    elif st.session_state.page == 'selection':
        selection_page()
    elif st.session_state.page == 'main':
        main()
    elif st.session_state.page == 'change_password':
        change_password()
    elif st.session_state.page == 'forgot_password':
        forgot_password()
