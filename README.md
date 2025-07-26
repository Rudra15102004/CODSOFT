# 🤖 CodSoft AI Internship Projects – Rudra Pratap Singh

This repository contains the completed tasks for the **Artificial Intelligence Internship** at **CodSoft**.  
Each task demonstrates the practical application of AI/ML concepts in real-world scenarios.

---

🎮 Tic-Tac-Toe AI (Task 2)

### 📌 Description
An unbeatable Tic-Tac-Toe game implemented in Python using the **Minimax Algorithm**. The AI plays optimally against a human player and ensures it never loses.

### 🧠 Concepts Used
- Game Theory
- Minimax Algorithm
- Recursive Decision Making
- Python Programming

### 🛠 Tech Stack
- Python
- (Optional) Tkinter for GUI

### 🚀 How to Run
1. Make sure Python is installed.
2. Open terminal or command prompt and navigate to the project directory.
3. Run the script using:
   ```bash
   python tic_tac_toe.py
🎯 Objective
To demonstrate classic AI gameplay logic using decision trees and search-based algorithms in a turn-based environment.

##🎬 Task 4: Movie Recommendation System

📌 Description
A content-based movie recommendation system that suggests similar movies based on a user-input movie title. It uses TF-IDF Vectorization to convert movie titles into numerical vectors and cosine similarity to identify related movies.

🧠 Concepts Used
Content-Based Filtering

TF-IDF (Term Frequency-Inverse Document Frequency)

Cosine Similarity

Text Preprocessing & NLP Fundamentals

pandas & scikit-learn

🛠 Tech Stack
Python

pandas

scikit-learn

🚀 How to Run
Install the required libraries:

bash
Copy
Edit
pip install pandas scikit-learn
Open the notebook:

bash
Copy
Edit
jupyter notebook Movie_Recommend.ipynb
or open it in Google Colab.

Run all cells. Use:

python
Copy
Edit
search("Avatar")
to get top recommended results.

🎯 Objective
To showcase how machine learning and natural language processing can be used to build real-world recommendation engines like those used by Netflix or Amazon Prime.

# TASK 1 CHATBOT WITH RULE-BASED RESPONSES

# Rule-Based Chatbot

A simple yet intelligent chatbot built with Python that uses predefined rules and pattern matching to have natural conversations with users.

## Features

- **Smart Pattern Recognition**: Uses regex patterns to understand user input
- **Natural Conversations**: Multiple response variations to avoid repetitive interactions
- **Name Memory**: Remembers and uses your name throughout the conversation
- **Time Queries**: Can tell you the current time when asked
- **Friendly Interface**: Clean console interface with proper formatting
- **Error Handling**: Gracefully handles unexpected inputs and interruptions

## What the Chatbot Can Do

The chatbot responds to various types of input:

### Greetings
- hi, hello, hey, howdy
- good morning, good afternoon, good evening
- what's up, hiya

### Personal Questions
- What's your name?
- How are you?
- How are you doing?
- Who are you?

### Information Requests
- What time is it?
- Current time
- Help requests

### Farewells
- bye, goodbye, see you later
- good night, farewell
- exit, quit

### Name Introduction
- My name is [Your Name]
- I'm [Your Name]
- Call me [Your Name]

## Installation

No external libraries required! Uses only Python standard library.

### Requirements
- Python 3.6 or higher
- Standard libraries: `re`, `random`, `datetime`

## Usage

### Console Version

1. Save the code as `Chatbot.py`
2. Open terminal/command prompt
3. Navigate to the file directory
4. Run the chatbot:

```bash
python Chatbot.py
```

### GUI Version

1. Save the GUI code as `Chatbot.py`
2. Run the GUI version:

```bash
python Chatbot.py
```

## Example Conversation

```
==================================================
  Welcome! I'm Alex, your chatbot companion
  Type 'quit' or 'exit' to end our conversation
==================================================

You: Hello there!
Alex: Hi! How's your day going?

You: My name is Sarah
Alex: Nice to meet you, Sarah! How can I help you today?

You: What's your name?
Alex: My name is Alex! What's yours?

You: How are you doing?
Alex: I'm doing great, thanks for asking! How about you?

You: What time is it?
Alex: It's currently 02:30 PM.

You: bye
Alex: Goodbye, Sarah! Take care!
```

## Technical Details

### Core Components

- **SimpleChatBot Class**: Main chatbot logic and conversation handling
- **Pattern Matching**: Uses regex for input recognition
- **Response System**: Random selection from predefined response lists
- **Name Extraction**: Identifies and remembers user names from conversation

### Key Methods

- `clean_input()`: Preprocesses user input for better matching
- `extract_name_from_input()`: Finds user names in conversation
- `check_greeting()`, `check_farewell()`: Pattern matching functions
- `process_user_input()`: Main logic for generating responses
- `start_conversation()`: Handles the conversation loop

## Customization

You can easily customize the chatbot by modifying these lists in the code:

### Adding New Responses
```python
self.greeting_responses = [
    "Hello there! Nice to meet you!",
    "Hi! How's your day going?",
    # Add your custom greetings here
]
```

### Adding New Patterns
```python
def check_new_pattern(self, user_input):
    patterns = [
        r'\byour_keyword\b',
        # Add regex patterns here
    ]
    # Add matching logic
```

## Development Notes

This chatbot was built as part of an AI internship project at CodSoft. It demonstrates:

- Rule-based AI principles
- Pattern matching techniques
- Natural language processing basics
- User interaction design
- Clean code practices

## Future Enhancements

Possible improvements you could add:

- Weather information integration
- Simple math calculations
- More personality traits
- Conversation history saving
- Multi-language support
- Voice input/output

## Troubleshooting

### Common Issues

**Problem**: Chatbot doesn't recognize input
- **Solution**: Check if your input matches the defined patterns, try rephrasing

**Problem**: Name not being remembered
- **Solution**: Use clear introduction format like "My name is [Name]"

**Problem**: Time not displaying correctly
- **Solution**: Ensure your system time is set correctly

### Error Messages

- `Please say something!` - You entered empty input
- `Sorry, something went wrong` - Unexpected error occurred
- Default responses - Input not recognized by any pattern

## Contributing

Feel free to fork this project and add your own features! Some ideas:

- Add more conversation topics
- Improve pattern matching
- Add emotional responses
- Create themed versions (gaming, movies, etc.)

## License

This project is open source and available under the MIT License.

---

**Created for CodSoft AI Internship**  
*A simple demonstration of rule-based chatbot development*

Made with ❤️ by Rudra Pratap Singh
