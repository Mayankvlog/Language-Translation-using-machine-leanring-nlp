import streamlit as st
from langdetect import detect
from googletrans import Translator, LANGUAGES
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK resources
nltk.download('punkt')

# Initialize Translator and Stemmer
translator = Translator()
stemmer = PorterStemmer()

def detect_and_translate(text, target_lang):
    # Detect language
    result_lang = detect(text)
    
    # Translate text
    translate_text = translator.translate(text, dest=target_lang).text

    return result_lang, translate_text

def tokenize_and_stem(text):
    # Tokenize text
    tokens = word_tokenize(text)
    
    # Stem tokens
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    
    return ' '.join(stemmed_tokens)

# Streamlit app
st.title('Language Detection, Translation, and Stemming')

# Language selection
languages = list(LANGUAGES.keys())
selected_lang = st.selectbox('Select target language', options=languages, format_func=lambda x: LANGUAGES[x].title())

# Input text
text = st.text_area('Enter text to translate')

if st.button('Translate'):
    if text:
        detected_lang, translation = detect_and_translate(text, selected_lang)
        st.write(f"**Detected Language:** {LANGUAGES[detected_lang].title()}")
        st.write(f"**Translation:** {translation}")
        
        # Tokenize and Stem text
        stemmed_text = tokenize_and_stem(text)
        st.write(f"**Stemmed Text:** {stemmed_text}")
    else:
        st.warning("Please enter some text to translate.")


