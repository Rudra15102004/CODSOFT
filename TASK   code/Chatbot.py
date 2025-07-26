import re
import random
from datetime import datetime

class SimpleChatBot:
    def __init__(self):
        self.bot_name = "Alex"
        self.user_name = None
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
        potential_name = self.extract_name_from_input(cleaned_input)
        if potential_name and not self.user_name:
            self.user_name = potential_name
            return f"Nice to meet you, {self.user_name}! How can I help you today?"
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

    def start_conversation(self):
        print("=" * 50)
        print(f"  Welcome! I'm {self.bot_name}, your chatbot companion")
        print("  Type 'quit' or 'exit' to end our conversation")
        print("=" * 50)
        print()
        
        while True:
            try:
                user_message = input("You: ").strip()
                
                if not user_message:
                    print(f"{self.bot_name}: Please say something!")
                    continue
                
                if user_message.lower() in ['quit', 'exit', 'bye']:
                    print(f"{self.bot_name}: {random.choice(self.farewell_responses)}")
                    break
                
                bot_response = self.process_user_input(user_message)
                print(f"{self.bot_name}: {bot_response}")
                print()
                
            except KeyboardInterrupt:
                print(f"\n{self.bot_name}: Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"{self.bot_name}: Sorry, something went wrong. Let's try again!")

if __name__ == "__main__":
    chatbot = SimpleChatBot()
    chatbot.start_conversation()