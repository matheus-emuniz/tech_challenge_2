# Genetic Algorithm Password Optimizer

A Streamlit-based web application that uses genetic algorithms to analyze and optimize password strength. This project demonstrates the application of evolutionary algorithms to cybersecurity, specifically password generation and strength analysis.

## 🔍 Overview

This application implements a genetic algorithm that evolves passwords from a dataset of common passwords to generate stronger, more secure passwords. It uses the `zxcvbn` library for password strength evaluation and provides an interactive web interface built with Streamlit.

## ✨ Features

- **Interactive Web Interface**: User-friendly Streamlit dashboard for configuring algorithm parameters
- **Customizable Password Requirements**: Configure length, character types (uppercase, lowercase, digits, special characters)
- **Real-time Evolution Tracking**: Visual charts showing fitness improvement over generations
- **Genetic Algorithm Parameters**: Adjustable mutation rate, population size, tournament size, and generations
- **Password Strength Analysis**: Integration with zxcvbn for robust password strength evaluation
- **Common Password Dataset**: Starts evolution from real-world common passwords for realistic optimization

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/matheus-emuniz/tech_challenge_2.git
cd tech_challenge_2
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source ./venv/bin/activate
```

4. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Configure your password requirements:
   - **Max length**: Set the maximum password length (8-64 characters)
   - **Character types**: Choose which character types to include
   - **Uppercase letters**: A-Z
   - **Lowercase letters**: a-z
   - **Digits**: 0-9
   - **Special characters**: !@#$%^&*()_+-=[]{}|;:,.<>?

4. Configure the genetic algorithm parameters:
   - **Generations**: Number of evolution cycles (1-2000)
   - **Mutation rate**: Probability of character mutation (0.0-1.0)
   - **Tournament size**: Selection pressure parameter (1-10)
   - **Population size**: Number of passwords in each generation (1-500)

5. Click "Submit" to start the evolution process and watch the real-time fitness improvement chart.

## 🧬 How It Works

### Genetic Algorithm Components

1. **Initial Population**: The algorithm starts with a random sample of common passwords from `common_passwords.csv`

2. **Fitness Function**: Each password is evaluated using:
   - Length requirements compliance
   - Character diversity (entropy calculation)
   - Password strength score using the zxcvbn library
   - Required character type presence

3. **Selection**: Tournament selection chooses parents for reproduction

4. **Crossover**: Uniform crossover combines parent passwords to create children

5. **Mutation**: Random character changes occur based on the mutation rate by adding or scrambling characters

6. **Evolution**: The process repeats for the specified number of generations, with fitness tracking displayed in real-time

### Password Strength Evaluation

The application uses the `zxcvbn` library, which provides:
- Pattern matching (keyboard patterns, dictionary words, etc.)
- Realistic crack time estimates
- Feedback for password improvement

## 📁 Project Structure

```
tech_challenge_2/
├── main.py                 # Streamlit web interface
├── genetic_algorithm.py    # Core genetic algorithm implementation
├── requirements.txt        # Python dependencies
├── common_passwords.csv    # Dataset of common passwords for initial population
├── .gitignore             # Git ignore patterns
└── README.md              # This file
```

## 🔧 Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **zxcvbn**: Password strength estimation
- **numpy**: Numerical computations
- **Additional**: See `requirements.txt` for complete list

## 🔍 Technical Details

### Genetic Algorithm Parameters

- **Population Size**: Number of candidate passwords in each generation
- **Generations**: Total number of evolution cycles
- **Mutation Rate**: Probability that each character in a password will be randomly changed
- **Tournament Size**: Number of candidates competing in tournament selection (higher = more selective)

### Fitness Calculation

The fitness function combines multiple factors:
- Password length compliance
- Character entropy (diversity)
- zxcvbn strength score
- Presence of required character types

### Performance Considerations

- Larger population sizes provide better diversity but slower evolution
- Higher mutation rates increase exploration but may slow convergence
- Tournament size affects selection pressure and convergence speed

### Kaggle dataset

The dataset used in this project is from Kaggle and can be found [here](https://www.kaggle.com/datasets/bradleyjones/common-passwords).

---

*Built with ❤️ using Python, Streamlit, and Genetic Algorithms*
