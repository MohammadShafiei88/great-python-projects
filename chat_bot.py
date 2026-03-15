from difflib import get_close_matches

def get_best_match(user_input: str, questions: dict) -> str:
    questions: list[str] = [q for q in questions]
    matches: list[str] = get_close_matches(user_input, questions, n=1, cutoff=0.6)
    if matches:
        return matches[0]

def chatbot(knowledge: dict) -> None:
    while True:
        user_input: str = input('You: ')
        best_match: str = get_best_match(user_input, knowledge)
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print("Bot: I don\'t understand... Could you try rephrasing that?")
        if user_input.lower() == 'quit' or user_input.lower() == 'exit':
            break


if __name__ == '__main__':
    brain: dict[str, str] = {'hello': 'Hey there!',
                   'how are you?': 'I am good, thanks!',
                   'do you know what the time is?': 'Not at all!',
                   'what time is it?': 'No clue!',
                   'what can you do?': 'I can answer questions!',
                   'ok': 'Great.',
                   'bye': 'Bye bye!',
                   'I hate you!!': 'Me too!'}
    chatbot(knowledge=brain)


