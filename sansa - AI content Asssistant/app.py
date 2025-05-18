# import streamlit as st
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain.schema.messages import HumanMessage, AIMessage, SystemMessage
# import os
# load_dotenv()
# import warnings
# warnings.filterwarnings("ignore")
# api_key=os.getenv("Groq_api_key")


# LLM=ChatGroq(
#         api_key=api_key,\
#         model="gemma2-9b-it",
#         temperature=1
#     )



# import streamlit as st
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history=[
        
#         SystemMessage(content="You are an AI assistant designed to help users create high-quality content for various purposes, such as blog posts, social media, articles, and more. Your name is ROCKY. Any non-content-related question should be ignored.")
        
#         ]
    

# import streamlit as st

# st.set_page_config(
#     page_title="My Chat App",       # Browser tab title
#     page_icon="💬",                 # Favicon
#     layout="wide",                  # "centered" or "wide"
#     initial_sidebar_state="expanded"  # Or "collapsed"
# )

# st.title("Welcome to My Chat App")
# st.write("This is a demo page configured with Streamlit's page settings.")

# query = st.chat_input("Type your message here...")
# st.markdown("""
#     <style>
#         .chat-container {
#             display: flex;
#             flex-direction: column;
#         }
#         .chat-message {
#             max-width: 70%;
#             padding: 5px 10px;
#             border-radius: 12px;
#             margin: 8px;
#         }
#         .human_message {
#             align-self: flex-end;
#             background: linear-gradient(135deg, #dfe9f3, #ffffff);
#             color: #1a1a1a;
#             border: 1px solid #cdd9e5;
#             text-align: right;
#         }
#         .ai_message {
#             align-self: flex-start;
#             background: linear-gradient(135deg, #fef6e4, #f1f7ed);
#             color: #2c2c2c;
#             border: 1px solid #e5d3b3;
#         }
#     </style>
# """, unsafe_allow_html=True)

# if query:
    
#         human_message=HumanMessage(content=query)
#         st.session_state.chat_history.append(human_message)

#         with st.spinner("generating........"):
#             response=LLM.invoke(st.session_state.chat_history)
#             result=response.content
#         if result:
#             ai_message=AIMessage(content=result)
#             st.session_state.chat_history.append(ai_message)


#         st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
#         for message in st.session_state.chat_history:
#             if isinstance(message, HumanMessage):
#                 st.markdown(f"<div class='chat-message human_message'>👤 You: {message.content}</div>", unsafe_allow_html=True)
#             elif isinstance(message, AIMessage):
#                 st.markdown(f"<div class='chat-message ai_message'>🤖 ROCKY AI: {message.content}</div>", unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#         st.session_state.chat_history = st.session_state.chat_history[-100:]
    



# if st.button("Clear Chat"):
#     st.session_state.chat_history = [
#         SystemMessage(content="""You are an AI assistant designed to help users create high-quality content for various purposes, such as blog posts, social media, articles, and more. Your name is ROCKY. Any non-content-related question should be ignored.
# """)
#     ]
#     st.rerun()

import streamlit as st
st.set_page_config(
    page_title="Sansa",
    page_icon="💗",           # Emoji or path to a .png/.ico file
    layout="wide",           # "wide" or "centered"
    initial_sidebar_state="expanded"  # Or "collapsed"
)
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema.messages import HumanMessage, AIMessage, SystemMessage
import os
import warnings

# Environment setup
load_dotenv()
warnings.filterwarnings("ignore")


api_key = st.sidebar.text_input("Enter your API Key:", type="password")





# Sidebar Model Selection
st.sidebar.title("🧠 Model Selector")
selected_model = st.sidebar.selectbox(
    "Choose a model:",
    ["llama3-70b-8192",  "deepseek-r1-distill-llama-70b","llama3-8b-8192"],
    index=1
)


# Load LLM 
if api_key:
    LLM = ChatGroq(
        api_key=api_key,
        model=selected_model,
        temperature=1
    )
else:
    print("Load your API key")



# Session state for chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are an AI assistant named Sansa. You help users create high-quality content like blog posts, social captions, articles, etc. You ignore irrelevant questions.")
    ]

# Styling
st.markdown("""
    <style>
        .chat-container {
            display: flex;
            flex-direction: column;
        }
        .chat-message {
            max-width: 70%;
            padding: 5px 10px;
            border-radius: 12px;
            margin: 8px;
        }
        .user-message {
            align-self: flex-end;
            background: linear-gradient(135deg, #E3FDF5, #FFE6FA);
            color: #333;
            border: 1px solid #A6DCEF;  /* Reduced border */
            text-align: right;
        }
        .ai-message {
            align-self: flex-start;
            background: linear-gradient(135deg, #FFF6E0, #D0F2FF);
            color: #000;
            border: 1px solid #FFC26F;  /* Reduced border */
        }
    </style>
""", unsafe_allow_html=True)

# Chat Title
st.title(" 💗 Sansa - AI Content Assistant")
st.caption("Ask me to help write blog intros, social media captions, or article summaries!")

# Chat messages UI
query=st.chat_input("chat here")

if query:
        try:
                human_message = HumanMessage(content=query)
                st.session_state.chat_history.append(human_message)
        
                with st.spinner("Hi i am Sansa ... 💗💗💗"):
                    response = LLM.invoke(st.session_state.chat_history)
                    result = response.content
        
                if result:
                    ai_message = AIMessage(content=result)
                    st.session_state.chat_history.append(ai_message)
        
                # Display all chat messages
                st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
                for message in st.session_state.chat_history:
                    if isinstance(message, HumanMessage):
                        st.markdown(f"<div class='chat-message user-message'>👤 You: {message.content}</div>", unsafe_allow_html=True)
                    elif isinstance(message, AIMessage):
                        st.markdown(f"<div class='chat-message ai-message'> 💗 Sansa : {message.content}</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
        
                # Limit message history
                st.session_state.chat_history = st.session_state.chat_history[-100:]
        
        except Exception as e:
                st.success("load your api key")



# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = [
        SystemMessage(content="You are an AI assistant named Sansa. You help users create high-quality content like blog posts, social captions, articles, etc. You ignore irrelevant questions.")
    ]
    st.rerun()
