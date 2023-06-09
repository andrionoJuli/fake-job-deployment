import re
import tldextract
import nltk
from urllib.parse import urlparse
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def basic_cleaning(text):
    """Perform cleaning of textual data by removing links, punctuation, special characters, words containing numbers
    and converting text to lower case """
    # Convert text to lowercase
    text = text.lower()

    # Remove links
    text = re.sub('https?://\S+|www\.\S+', '', text)

    # Remove punctuation
    text = re.sub('[^a-zA-Z0-9\s]', '', text)

    # Remove special characters
    text = re.sub('[^0-9a-zA-Z\s]', '', text)

    # Remove words containing numbers
    text = re.sub('\w*\d\w*', '', text)

    return text


# Initialize the tokenizer
tokens = RegexpTokenizer(r'\w+')


# Tokenization function to return the text after tokenization
def tokenize_text(text):
    """Perform tokenization to the passed text and return the text as a list of tokens."""
    return tokens.tokenize(text)


# Setting up the stopwords dictionary
stop_wordsEn = set(stopwords.words('english'))


# Function to remove the stopwords in the tokens
def remove_stopwords(tokens):
    """Remove stopwords from the passed list of tokens and return the output."""
    return [word for word in tokens if word not in stop_wordsEn]


# Initiate the lemmatizer
wNetLemmatizer = WordNetLemmatizer()


# Function to return the text after lemmatization
def lemmatize_token(tokens):
    """Return the token to its base root and return the output."""
    return [wNetLemmatizer.lemmatize(token) for token in tokens]


# list of acceptable tlds of the URL
tlds = ['com', 'cn', 'de', 'us', 'uk', 'org', 'ru', 'jp', 'br', 'it', 'au', 'ca', 'pl', 'fr', 'ir', 'in', 'es', 'kr',
        'nl', 'ch', 'se', 'my', 'sg', 'id']


def is_jobstreet_url(url):
    """Check if the given URL is a valid JobStreet URL with a proper TLD or ccTLD."""
    extracted = tldextract.extract(url)
    if extracted.domain == 'jobstreet' and any(extracted.suffix.endswith('.' + tld) for tld in tlds):
        parsed_url = urlparse(url)
        if "/job/" in parsed_url.path:
            return True
    return False



