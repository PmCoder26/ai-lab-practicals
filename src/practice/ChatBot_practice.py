import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')

knowledge_base = {
    'internet_issue': [
        'Check you router is turned on.',
        'Restart your router',
        'Contact you internet service provider'
    ],
    'software_installation': [
        'Check you system is compatible with the software or not',
        'Install the latest version',
        'Update your OS',
        'Download from the authorized and official website only.'
    ]
}

issue_keywords = {
    'internet_issue': ['internet', 'network', 'wifi', 'router', 'connect'],
    'software_installation': ['install', 'software', 'crash', 'setup', 'download']
}

class Chatbot:

    def _init__(self):
        self.stemmer = PorterStemmer()
        self.knowledge_base = knowledge_base
        self.issue_keywords = issue_keywords

    def preprocess_input(self, user_input):
        tokens = word_tokenize(user_input)
        stemmed_words = [self.stemmer.stem(word) for word in tokens]
        return stemmed_words

    def diagnose_issue(self, user_input):
        words = self.preprocess_input(user_input)
        for issue, keywords in self.issue_keywords.items():
            if any(self.stemmer.stem(keyword) in words for keyword in keywords):
                return self.provide_solution(issue)
        return "Unable to resolve the issue."

    def provide_solution(self, issue):
        solutions = self.knowledge_base.get(issue)
        return solutions


chatbot = Chatbot()
chatbot.diagnose_issue("Internet issue")

