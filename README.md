# Spam-Ham Detection

A Machine Learning and Natural Language Processing (NLP) project that classifies text messages as **Spam** or **Ham (legitimate)**.

The project processes text messages, extracts meaningful features from the text, and uses a Machine Learning classification model to determine whether a message is potentially unwanted or legitimate.

---

## 📌 Overview

Spam messages are unwanted messages that may contain advertisements, fraudulent offers, phishing attempts, or malicious links.

This project applies **Natural Language Processing and Machine Learning** to automatically classify messages into two categories:

- 🚨 **Spam** — Unwanted or potentially suspicious message
- ✅ **Ham** — Normal and legitimate message

The project demonstrates an end-to-end NLP workflow, from text preprocessing and feature extraction to model training and prediction.

---

## 🎯 Objectives

- Build an automated Spam/Ham classification system.
- Apply NLP techniques to text data.
- Clean and preprocess raw messages.
- Convert text into numerical features suitable for Machine Learning.
- Train and evaluate a classification model.
- Predict whether a new message is Spam or Ham.

---

## 🧠 How It Works

```text
              User Message
                    │
                    ▼
            Text Preprocessing
                    │
          ┌─────────┴─────────┐
          │                   │
     Lowercasing         Remove Noise
          │                   │
          └─────────┬─────────┘
                    ▼
             Tokenization
                    │
                    ▼
          Feature Extraction
                    │
                    ▼
             ML Classifier
                    │
              ┌─────┴─────┐
              ▼           ▼
            SPAM          HAM
```

---

## 🔄 Machine Learning Workflow

```text
Dataset
   │
   ▼
Data Loading
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Text Preprocessing
   │
   ▼
Feature Extraction
   │
   ▼
Train / Test Split
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Trained Model
   │
   ▼
New Message
   │
   ▼
Spam / Ham Prediction
```

---

## 📝 Natural Language Processing

The text data is processed before being passed to the Machine Learning model.

Typical preprocessing steps include:

### 1. Lowercasing

Converts all text to lowercase so that words such as:

```text
"FREE"
"Free"
"free"
```

are treated consistently.

### 2. Removing Unnecessary Characters

Unwanted punctuation, symbols, and other noise can be removed from the message.

### 3. Tokenization

The message is divided into individual words or tokens.

```text
"Congratulations you won a prize"

        ↓

["Congratulations", "you", "won", "a", "prize"]
```

### 4. Stopword Removal

Common words that provide limited classification information can be removed.

### 5. Stemming / Normalization

Words can be reduced to their root form to reduce vocabulary size.

---

## 🔢 Feature Extraction

Machine Learning algorithms cannot directly understand raw text.

Therefore, the processed text is converted into numerical features using a text vectorization technique.

### TF-IDF

**Term Frequency-Inverse Document Frequency (TF-IDF)** represents text numerically by assigning importance to words based on their frequency within a message and across the dataset.

```text
Raw Message
     ↓
Text Cleaning
     ↓
Tokenization
     ↓
TF-IDF Vectorization
     ↓
Numerical Feature Vector
     ↓
Machine Learning Model
```

---

## 🤖 Machine Learning Model

The processed and vectorized messages are used to train a classification model.

The model learns patterns that distinguish spam messages from legitimate messages.

For example, messages containing patterns such as:

```text
"Congratulations"
"Winner"
"Free"
"Prize"
"Claim now"
```

may contain stronger spam-related signals, while ordinary conversational messages are more likely to be classified as ham.

> **Note:** Replace this section with the exact classifier used in your notebook, such as Multinomial Naive Bayes, Logistic Regression, Random Forest, SVM, etc.

---

## 📊 Model Evaluation

The classifier can be evaluated using several metrics:

| Metric | Purpose |
|---|---|
| **Accuracy** | Overall percentage of correct predictions |
| **Precision** | How many predicted spam messages were actually spam |
| **Recall** | How many actual spam messages were detected |
| **F1-Score** | Balance between precision and recall |
| **Confusion Matrix** | Shows correct and incorrect classifications |

For spam detection, **precision and recall are particularly important** because both false spam classifications and missed spam messages matter.

---

## 📂 Project Structure

```text
Spam-Ham-Detection/
│
├── dataset/
│   └── Dataset files
│
├── notebook/
│   └── NLP / model development notebook
│
├── models/
│   └── Trained model files
│
├── app.py
│   └── Prediction application
│
├── requirements.txt
│   └── Project dependencies
│
├── screenshots/
│   └── Application screenshots
│
├── LICENSE
└── README.md
```

> Update the structure above to match the actual files in your repository.

---

## 🛠️ Tech Stack

### Programming

- Python

### Machine Learning

- Scikit-learn

### NLP

- NLTK
- Text preprocessing
- TF-IDF / text vectorization

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Development

- Jupyter Notebook
- Git
- GitHub

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/duttabikram/Spam-Ham-Detection.git
```

### 2. Navigate to the project

```bash
cd Spam-Ham-Detection
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

If the project contains a Streamlit application:

```bash
streamlit run app.py
```

If the project is notebook-based, open the notebook using Jupyter:

```bash
jupyter notebook
```

Then open the project notebook and execute the cells sequentially.

---

## 💡 Example

### Input

```text
Congratulations! You have won a free prize.
Click here to claim your reward.
```

### Output

```text
🚨 SPAM
```

Another example:

### Input

```text
Hey, are you coming to college tomorrow?
```

### Output

```text
✅ HAM
```

---

## 🚀 Future Improvements

- Improve classification performance using advanced NLP techniques.
- Compare multiple Machine Learning algorithms.
- Perform hyperparameter tuning.
- Use word embeddings such as Word2Vec or GloVe.
- Experiment with transformer-based models.
- Add real-time message classification.
- Improve the user interface.
- Deploy the application online.
- Add probability/confidence scores to predictions.
- Support both SMS and email spam detection.

---

## ⚠️ Limitations

The model's predictions depend on the quality and diversity of the training dataset.

A message may occasionally be classified incorrectly, particularly when it contains unusual wording, new spam patterns, or language that differs significantly from the training data.

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Bikram Dutta
