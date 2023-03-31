from newspaper import Article
import streamlit as st
import nltk
nltk.download('punkt')
st.title("Article Summarizer")
url =st.text_input('Paste the article link below',"")
language={"English":"en","Hindi":"hi"}
selected_lang=st.selectbox("Language of the article", language)
if st.button("Summarize"):
    my_article = Article(url, selected_lang)
    my_article.download()
    my_article.parse()
    st.header(my_article.title)
    # NLP on the article
    my_article.nlp()
    # Extract summary
    st.markdown(my_article.summary)
    # Extract keywords
    st.markdown('Keywords: '+','.join([i for i in (my_article.keywords)]))
