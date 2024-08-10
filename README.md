# DTA-DGT SensorTrack

DTA-DGT SensorTrack is a web application built with Streamlit for managing sensor procurement and replacement workflows. It provides a user-friendly interface to securely log in, filter sensor data, visualize results, and export reports in Excel or PDF formats.

## Features

- **User Authentication**: Secure login with username, password, and OTP verification.
- **Data Filtering**: Filter sensor data by plant, make, model, gas type, and date range.
- **Visualization**: View filtered data and track completed vs. pending procurements or replacements.
- **Export Options**: Download filtered data in Excel or PDF format for detailed analysis.
- **User Management**: Change passwords and reset forgotten passwords.

## Installation

**1. Clone the repository:**
git clone https://github.com/Amit-Raj26/DTA-DGT_SensorTrack.git
cd your_repository

**2. Install dependencies:**
pip install -r requirements.txt

**3. Run the application:**
streamlit run SortXL13.py

## Usage

1. Navigate to the login page and enter your credentials.
2. Select an option (sensor procurement or replacement) and proceed.
3. Upload an Excel file containing sensor data.
4. Use filters to refine data and view results.
5. Download filtered data or reports as needed.

## Technologies Used

- Python
- Streamlit
- Pandas
- wkhtmltopdf (for PDF export)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Built using Streamlit: [streamlit.io](https://streamlit.io)
- Icons from [Flaticon](https://www.flaticon.com)


