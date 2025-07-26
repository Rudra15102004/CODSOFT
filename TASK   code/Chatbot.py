import tkinter as tk
from tkinter import scrolledtext, messagebox
import re
import random
from datetime import datetime

class ChatBotGUI:
    def __init__(self):
        self.bot_name = "Alex"
        self.user_name = None
        
        # Response variations for natural conversation
        self.greeting_responses = [
            "Hello there! Nice to meet you!",
            "Hi! How's your day going?",
            "Hey! Great to see you here!",
            "Hello! I'm Alex, your friendly chatbot.",
            "Hi there! What brings you here today?"
        ]
        
        self.farewell_responses = [
            "Goodbye! Take care!",
            "See you later! Have a great day!",
            "Bye! It was nice talking with you!",
            "Farewell! Come back anytime!",
            "Take care! Until next time!"
        ]
        
        self.how_are_you_responses = [
            "I'm doing great, thanks for asking! How about you?",
            "Pretty good! Just here to help and chat.",
            "I'm fantastic! Ready to assist you with anything.",
            "Doing well! What about yourself?",
            "I'm good! Thanks for checking on me."
        ]
        
        self.name_responses = [
            f"My name is {self.bot_name}! What's yours?",
            f"I'm {self.bot_name}, nice to meet you!",
            f"You can call me {self.bot_name}. And you are?",
            f"I go by {self.bot_name}! What should I call you?"
        ]
        
        self.help_responses = [
            "I can chat with you about various topics! Try asking me about my name, how I'm doing, or just say hello!",
            "I'm here to have a friendly conversation. You can greet me, ask questions, or just chat!",
            "I can respond to greetings, answer basic questions about myself, and have casual conversations with you!",
            "Just talk to me naturally! I understand greetings, basic questions, and casual chat."
        ]
        
        self.default_responses = [
            "I'm not sure I understand that. Could you try rephrasing?",
            "Hmm, I didn't quite get that. Can you say it differently?",
            "That's interesting, but I'm not sure how to respond to that.",
            "I'm still learning! Can you try asking something else?",
            "Sorry, I don't have a good response for that. What else would you like to talk about?"
        ]
        
        # Setup the GUI
        self.setup_gui()
        
    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title(f"Chat with {self.bot_name}")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Create main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(
            main_frame, 
            wrap=tk.WORD, 
            width=70, 
            height=20,
            bg='white',
            fg='black',
            font=('Arial', 10)
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg='#f0f0f0')
        input_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Message input field
        self.message_entry = tk.Entry(
            input_frame, 
            font=('Arial', 11),
            relief=tk.RAISED,
            bd=1
        )
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.message_entry.bind('<Return>', self.send_message_event)
        
        # Send button
        self.send_button = tk.Button(
            input_frame, 
            text="Send", 
            command=self.send_message,
            bg='#4CAF50',
            fg='white',
            font=('Arial', 10, 'bold'),
            relief=tk.RAISED,
            bd=2,
            width=8
        )
        self.send_button.pack(side=tk.RIGHT)
        
        # Control buttons frame
        control_frame = tk.Frame(main_frame, bg='#f0f0f0')
        control_frame.pack(fill=tk.X)
        
        # Clear chat button
        self.clear_button = tk.Button(
            control_frame,
            text="Clear Chat",
            command=self.clear_chat,
            bg='#ff6b6b',
            fg='white',
            font=('Arial', 9),
            relief=tk.RAISED,
            bd=1
        )
        self.clear_button.pack(side=tk.LEFT, padx=(0, 5))
        
        # Exit button
        self.exit_button = tk.Button(
            control_frame,
            text="Exit",
            command=self.close_application,
            bg='#666666',
            fg='white',
            font=('Arial', 9),
            relief=tk.RAISED,
            bd=1
        )
        self.exit_button.pack(side=tk.RIGHT)
        
        # Initial welcome message
        self.display_message(f"{self.bot_name}", f"Hello! I'm {self.bot_name}, your chatbot companion. How can I help you today?")
        
        # Focus on input field
        self.message_entry.focus()

    def display_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def send_message_event(self, event):
        self.send_message()

    def send_message(self):
        user_message = self.message_entry.get().strip()
        
        if not user_message:
            return
        
        # Display user message
        self.display_message("You", user_message)
        
        # Clear input field
        self.message_entry.delete(0, tk.END)
        
        # Process and display bot response
        bot_response = self.process_user_input(user_message)
        self.display_message(f"{self.bot_name}", bot_response)

    def clear_chat(self):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.display_message(f"{self.bot_name}", "Chat cleared! How can I help you?")

    def close_application(self):
        result = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if result:
            self.root.destroy()

    def clean_input(self, user_input):
        cleaned = re.sub(r'\s+', ' ', user_input.strip().lower())
        return cleaned

    def extract_name_from_input(self, user_input):
        patterns = [
            r"my name is (\w+)",
            r"i'm (\w+)",
            r"i am (\w+)",
            r"call me (\w+)",
            r"it's (\w+)",
            r"(\w+) here"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, user_input.lower())
            if match:
                return match.group(1).capitalize()
        return None

    def check_greeting(self, user_input):
        greeting_patterns = [
            r'\b(hi|hello|hey|howdy|greetings)\b',
            r'\bgood (morning|afternoon|evening)\b',
            r'\bwhat\'?s up\b',
            r'\bhiya\b'
        ]
        
        for pattern in greeting_patterns:
            if re.search(pattern, user_input):
                return True
        return False

    def check_farewell(self, user_input):
        farewell_patterns = [
            r'\b(bye|goodbye|see you|farewell|exit|quit)\b',
            r'\btalk to you later\b',
            r'\bcatch you later\b',
            r'\bgood night\b'
        ]
        
        for pattern in farewell_patterns:
            if re.search(pattern, user_input):
                return True
        return False

    def check_name_question(self, user_input):
        name_patterns = [
            r'\bwhat\'?s your name\b',
            r'\bwho are you\b',
            r'\byour name\b',
            r'\bwhat should i call you\b'
        ]
        
        for pattern in name_patterns:
            if re.search(pattern, user_input):
                return True
        return False

    def check_how_are_you(self, user_input):
        status_patterns = [
            r'\bhow are you\b',
            r'\bhow\'?re you doing\b',
            r'\bhow do you feel\b',
            r'\bare you (okay|alright|good|fine)\b'
        ]
        
        for pattern in status_patterns:
            if re.search(pattern, user_input):
                return True
        return False

    def check_help_request(self, user_input):
        help_patterns = [
            r'\bhelp\b',
            r'\bwhat can you do\b',
            r'\bwhat are you\b',
            r'\bassist\b'
        ]
        
        for pattern in help_patterns:
            if re.search(pattern, user_input):
                return True
        return False

    def check_time_question(self, user_input):
        time_patterns = [
            r'\bwhat time\b',
            r'\bcurrent time\b',
            r'\btime is it\b'
        ]
        
        for pattern in time_patterns:
            if re.search(pattern, user_input):
                return True
        return False

    def get_current_time(self):
        current_time = datetime.now().strftime("%I:%M %p")
        return f"It's currently {current_time}."

    def process_user_input(self, user_input):
        cleaned_input = self.clean_input(user_input)
        
        # Check if user is introducing themselves
        potential_name = self.extract_name_from_input(cleaned_input)
        if potential_name and not self.user_name:
            self.user_name = potential_name
            return f"Nice to meet you, {self.user_name}! How can I help you today?"
        
        # Handle different types of input
        if self.check_farewell(cleaned_input):
            if self.user_name:
                return f"Goodbye, {self.user_name}! " + random.choice(self.farewell_responses)
            return random.choice(self.farewell_responses)
        
        elif self.check_greeting(cleaned_input):
            if self.user_name:
                return f"Hello again, {self.user_name}! " + random.choice(self.greeting_responses)[6:]
            return random.choice(self.greeting_responses)
        
        elif self.check_name_question(cleaned_input):
            return random.choice(self.name_responses)
        
        elif self.check_how_are_you(cleaned_input):
            return random.choice(self.how_are_you_responses)
        
        elif self.check_help_request(cleaned_input):
            return random.choice(self.help_responses)
        
        elif self.check_time_question(cleaned_input):
            return self.get_current_time()
        
        return random.choice(self.default_responses)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    chatbot_gui = ChatBotGUI()
    chatbot_gui.run()