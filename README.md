# SMS Classifier

A simple yet powerful web application designed to classify SMS messages as either **Spam** or **Ham** (not spam). Built with Python, this project leverages Natural Language Processing (NLP) and Machine Learning to provide accurate predictions.

## 🚀 Features

-   **Real-time Classification**: Instantly classifies SMS messages entered by the user.
-   **Text Preprocessing**: Automatically cleans and processes text (lowercasing, tokenization, stopword removal, stemming) for better accuracy.
-   **Interactive UI**: User-friendly interface built with Streamlit.
-   **Machine Learning**: Utilizes a trained model (likely Naive Bayes or similar) and TF-IDF vectorization.



## 🛠️ Tech Stack

-   **Python**: Core programming language.
-   **Streamlit**: For the web application framework.
-   **Scikit-learn**: For machine learning model and vectorization.
-   **NLTK**: For Natural Language Processing tasks (stopwords, stemming).
-   **Pandas & NumPy**: For data manipulation (used in training).


## 📦 Installation

To run this project locally, follow these steps:

1.  **Clone the repository** (if applicable) or download the source code.

2.  **Install the required dependencies**:
    Ensure you have Python installed. Then run:
    ```bash
    pip install streamlit nltk scikit-learn pandas numpy
    ```

3.  **Download NLTK data**:
    The app requires specific NLTK datasets. You might need to run this once in a Python shell:
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

4.  **Run the Streamlit app**:
    ```bash
    streamlit run web_main.py
    ```


## 🏃 Usage

1.  Navigate to the project directory:
    ```bash
    cd "d:\SMS Classifier"
    ```

2.  Run the Streamlit app:
    ```bash
    streamlit run web_main.py
    ```

3.  The application will open in your default web browser. Enter an SMS message in the text area and click **"Classify Message"** to see the result.

## 📂 Project Structure

-   `web_main.py`: The main Streamlit application script.
-   `main.ipynb`: Jupyter notebook used for data analysis, preprocessing, and model training.
-   `model.pkl`: The trained machine learning model.
-   `vectorizer.pkl`: The TF-IDF vectorizer used to transform input text.
-   `data/`: Directory containing the dataset (`spam.csv`).