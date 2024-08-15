# Phishing Website Detector

## Overview

**Phishing Website Detector** is a web application that classifies websites as either "Phishing" or "Legitimate" based on the URL provided. It uses a machine learning model to analyze various features of the URL, such as length, special characters, and redirection count, to determine the likelihood of the website being a phishing site.

## Features

- **Custom Machine Learning Model:** A machine learning model developed and trained from scratch using a dataset of phishing and legitimate URLs.
- **URL Feature Extraction:** The application analyzes several characteristics of the URL, such as its length, the presence of special characters, and the number of redirections.
- **Real-Time Classification:** Users can instantly check the legitimacy of a website by simply pasting its URL into the app.
- **Error Handling:** The application gracefully handles errors during URL processing, providing clear feedback to the user.

## Technologies Used

- **Frontend:** Streamlit
- **Backend:** Python
- **Machine Learning:** Custom model built using Scikit-learn library
- **Model Storage:** Pickle (for saving and loading the model)
- **HTTP Requests:** Requests library for handling URL redirection checks

## Installation

1. **Clone the repository:**
   ```python
   git clone https://github.com/yourusername/phishing-website-detector.git

2. **Navigate to the project directory:**
   ```python
   cd phishing-website-detector

3. **Install the dependencies:**
   ```python
   pip install -r requirements.txt
   ```
4. **Add the Machine Learning Model:**
Ensure that your custom-trained machine learning model (model.pkl) is placed in the root directory of the project.

5. **Run the app:**
   ```python
   streamlit run app.py
   ```

## Usage

1. **Paste the URL:**
Enter the URL of the website you want to analyze in the input field.
2. **Predict:** Click the "Predict" button to start the analysis. The application will process the URL and extract relevant features.
3. **View the Result**: Based on the extracted features, the application will classify the website as either "Phishing" or "Legitimate." The result is displayed directly on the interface.
4. **Error Messages:** If there's an issue with processing the URL (e.g., network errors, invalid URL), the application will display an appropriate error message.

## How the Model Works

### Feature Extraction
The model evaluates several key features of the URL, including:

- Length of the URL
- Number of dots (.)
- Number of hyphens (-)
- Number of underscores (_)
- Number of slashes (/)
- Number of question marks (?)
- Number of equals signs (=)
- Number of at symbols (@)
- Number of ampersands (&)
- Number of exclamation marks (!)
- Number of spaces
- Number of tilde symbols (~)
- Number of commas (,)
- Number of plus signs (+)
- Number of asterisks (*)
- Number of hash symbols (#)
- Number of dollar signs ($)
- Number of percent signs (%)
- **Redirection Count:** The number of times the URL redirects to another page.

### Classification
The extracted features are fed into the custom machine learning model, which predicts whether the website is phishing or legitimate.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow the steps below:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Contact

For any questions or suggestions, feel free to reach out:

- **Email:** [royrudra164@gmail.com](mailto:royrudra164@gmail.com)
- **LinkedIn:** [Rudra Roy](https://www.linkedin.com/in/rudra03/)
