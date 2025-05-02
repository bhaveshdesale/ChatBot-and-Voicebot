# OpenAi Code

# import streamlit as st
# import openai
# import os
# import pyttsx3
# import torch
# import torchaudio
# from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
# import av
# import numpy as np

# # Set OpenAI API Key
# openai.api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

# # Text to Speech
# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# # ChatGPT response
# def chatgpt_response(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful AI assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response.choices[0].message.content.strip()

# # Speech Recognition setup
# bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
# model = bundle.get_model()
# labels = bundle.get_labels()

# class AudioProcessor(AudioProcessorBase):
#     def __init__(self):
#         self.audio_buffer = []

#     def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
#         audio = frame.to_ndarray()
#         audio = np.mean(audio, axis=0)
#         self.audio_buffer.extend(audio)
#         return frame

#     def get_audio(self):
#         return np.array(self.audio_buffer)

# # Streamlit UI
# st.set_page_config(page_title="💬 ChatBot + Voice Bot", page_icon="🤖", layout="centered")
# st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 ChatGPT Voice Bot</h1>", unsafe_allow_html=True)
# st.write("Chat with AI using **Text or Voice**. Enjoy the magic of ChatGPT + Voice Bot 🔥")

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # ---------- 🚀 Text Chat Section ----------
# st.markdown("## 🚀 Text Chat")

# user_input = st.text_input("💬 Type your message here:")

# if st.button("Send Message"):
#     if user_input:
#         bot_reply = chatgpt_response(user_input)
#         st.session_state.chat_history.append(("You", user_input))
#         st.session_state.chat_history.append(("Bot", bot_reply))
#         speak(bot_reply)
#         st.success("Bot replied and spoken!")

# st.markdown("---")

# # ---------- 🎙️ Voice Chat Section ----------
# st.markdown("## 🎙️ Voice Chat")

# ctx = webrtc_streamer(
#     key="speech",
#     mode=WebRtcMode.SENDRECV,
#     audio_receiver_size=1024,
#     video_receiver_size=0,
#     audio_processor_factory=AudioProcessor,
#     media_stream_constraints={"audio": True, "video": False},
# )

# if ctx and ctx.state.playing:
#     st.info("🎙️ Listening... Speak now and then stop the stream.")

#     if st.button("📝 Process Voice"):
#         audio_data = ctx.audio_processor.get_audio()
#         waveform = torch.tensor(audio_data).float().unsqueeze(0)

#         with torch.inference_mode():
#             emissions, _ = model(waveform)
#         emissions = torch.log_softmax(emissions, dim=-1)
#         tokens = torch.argmax(emissions, dim=-1)

#         text = ""
#         for t in tokens[0]:
#             if t != 0:
#                 text += labels[t]
#         st.success(f"🗣️ You said: {text}")

#         bot_reply = chatgpt_response(text)
#         st.session_state.chat_history.append(("You", text))
#         st.session_state.chat_history.append(("Bot", bot_reply))
#         speak(bot_reply)
#         st.success("Bot replied and spoken!")

# st.markdown("---")

# # ---------- 📝 Chat History Section ----------
# st.markdown("## 📝 Chat History")
# for sender, message in st.session_state.chat_history:
#     if sender == "You":
#         st.markdown(f"<div style='background-color: #DCF8C6; padding:10px; border-radius:10px; margin:5px;'>🧑 <b>{sender}:</b> {message}</div>", unsafe_allow_html=True)
#     else:
#         st.markdown(f"<div style='background-color: #E6E6FA; padding:10px; border-radius:10px; margin:5px;'>🤖 <b>{sender}:</b> {message}</div>", unsafe_allow_html=True)

# st.markdown("---")
# st.markdown("<small>Made By Bhavesh with ❤️ using Streamlit & OpenAI</small>", unsafe_allow_html=True)



# Deep seek Api key

# import streamlit as st
# import os
# import pyttsx3
# import torch
# import torchaudio
# import requests  # For DeepSeek API requests
# from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
# import av
# import numpy as np

# # Set DeepSeek API Key (Replace with your DeepSeek API key)
# deepseek_api_key = st.secrets.get("DEEPSEEK_API_KEY") or os.getenv("DEEPSEEK_API_KEY")

# # Text to Speech
# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# # ✅ DeepSeek API request
# def deepseek_response(prompt):
#     url = "https://api.deepseek.com/v1/chat/completions"  # ✅ Correct DeepSeek endpoint
    
#     headers = {
#         "Authorization": f"Bearer {deepseek_api_key}",
#         "Content-Type": "application/json"
#     }
    
#     data = {
#         "model": "deepseek-chat",  # ✅ Correct model ID
#         "messages": [{"role": "user", "content": prompt}]
#     }

#     response = requests.post(url, json=data, headers=headers)
    
#     if response.status_code == 200:
#         response_json = response.json()
#         return response_json['choices'][0]['message']['content'].strip()
#     else:
#         return f"Error: {response.status_code} - {response.text}"

# # Speech Recognition setup
# bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
# model = bundle.get_model()
# labels = bundle.get_labels()

# class AudioProcessor(AudioProcessorBase):
#     def __init__(self):
#         self.audio_buffer = []

#     def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
#         audio = frame.to_ndarray()
#         audio = np.mean(audio, axis=0)
#         self.audio_buffer.extend(audio)
#         return frame

#     def get_audio(self):
#         return np.array(self.audio_buffer)

# # Streamlit UI
# st.set_page_config(page_title="💬 ChatBot + Voice Bot", page_icon="🤖", layout="centered")
# st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 ChatBot Voice Bot</h1>", unsafe_allow_html=True)
# st.write("Chat with AI using **Text or Voice**. Enjoy the magic of DeepSeek AI + Voice Bot 🔥")

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # ---------- 🚀 Text Chat Section ----------
# st.markdown("## 🚀 Text Chat")

# user_input = st.text_input("💬 Type your message here:")

# if st.button("Send Message"):
#     if user_input:
#         bot_reply = deepseek_response(user_input)
#         st.session_state.chat_history.append(("You", user_input))
#         st.session_state.chat_history.append(("Bot", bot_reply))
#         speak(bot_reply)
#         st.success("Bot replied and spoken!")

# st.markdown("---")

# # ---------- 🎙️ Voice Chat Section ----------
# st.markdown("## 🎙️ Voice Chat")

# ctx = webrtc_streamer(
#     key="speech",
#     mode=WebRtcMode.SENDRECV,
#     audio_receiver_size=1024,
#     video_receiver_size=0,
#     audio_processor_factory=AudioProcessor,
#     media_stream_constraints={"audio": True, "video": False},
# )

# if ctx and ctx.state.playing:
#     st.info("🎙️ Listening... Speak now and then stop the stream.")

#     if st.button("📝 Process Voice"):
#         audio_data = ctx.audio_processor.get_audio()
#         waveform = torch.tensor(audio_data).float().unsqueeze(0)

#         with torch.inference_mode():
#             emissions, _ = model(waveform)
#         emissions = torch.log_softmax(emissions, dim=-1)
#         tokens = torch.argmax(emissions, dim=-1)

#         text = ""
#         for t in tokens[0]:
#             if t != 0:
#                 text += labels[t]
#         st.success(f"🗣️ You said: {text}")

#         bot_reply = deepseek_response(text)
#         st.session_state.chat_history.append(("You", text))
#         st.session_state.chat_history.append(("Bot", bot_reply))
#         speak(bot_reply)
#         st.success("Bot replied and spoken!")

# st.markdown("---")

# # ---------- 📝 Chat History Section ----------
# st.markdown("## 📝 Chat History")
# for sender, message in st.session_state.chat_history:
#     if sender == "You":
#         st.markdown(f"<div style='background-color: #DCF8C6; padding:10px; border-radius:10px; margin:5px;'>🧑 <b>{sender}:</b> {message}</div>", unsafe_allow_html=True)
#     else:
#         st.markdown(f"<div style='background-color: #E6E6FA; padding:10px; border-radius:10px; margin:5px;'>🤖 <b>{sender}:</b> {message}</div>", unsafe_allow_html=True)

# st.markdown("---")
# st.markdown("<small>Made By Bhavesh with ❤️ using Streamlit & DeepSeek</small>", unsafe_allow_html=True)





# Gemini Api key
# import streamlit as st
# import os
# import pyttsx3
# import torch
# import torchaudio
# import requests
# from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
# import av
# import numpy as np

# # Set Gemini API Key (Replace with your Gemini API key)
# gemini_api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

# # Text to Speech
# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# # ✅ Gemini API request
# def gemini_response(prompt):
#     url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={gemini_api_key}"
    
#     headers = {
#         "Content-Type": "application/json"
#     }
    
#     data = {
#         "contents": [
#             {
#                 "parts": [{"text": prompt}]
#             }
#         ]
#     }

#     response = requests.post(url, json=data, headers=headers)
    
#     if response.status_code == 200:
#         response_json = response.json()
#         return response_json['candidates'][0]['content']['parts'][0]['text'].strip()
#     else:
#         return f"Error: {response.status_code} - {response.text}"

# # Speech Recognition setup
# bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
# model = bundle.get_model()
# labels = bundle.get_labels()

# class AudioProcessor(AudioProcessorBase):
#     def __init__(self):
#         self.audio_buffer = []

#     def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
#         audio = frame.to_ndarray()
#         audio = np.mean(audio, axis=0)
#         self.audio_buffer.extend(audio)
#         return frame

#     def get_audio(self):
#         return np.array(self.audio_buffer)

# # Streamlit UI
# st.set_page_config(page_title="💬 ChatBot + Voice Bot", page_icon="🤖", layout="centered")
# st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 ChatBot Voice Bot (Gemini API)</h1>", unsafe_allow_html=True)
# st.write("Chat with AI using **Text or Voice**. Powered by Google Gemini AI + Voice Bot 🔥")

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # ---------- 🚀 Text Chat Section ----------
# st.markdown("## 🚀 Text Chat")

# user_input = st.text_input("💬 Type your message here:")

# if st.button("Send Message"):
#     if user_input:
#         bot_reply = gemini_response(user_input)
#         st.session_state.chat_history.append(("You", user_input))
#         st.session_state.chat_history.append(("Bot", bot_reply))
#         speak(bot_reply)
#         st.success("Bot replied and spoken!")

# st.markdown("---")

# # ---------- 🎙️ Voice Chat Section ----------
# st.markdown("## 🎙️ Voice Chat")

# ctx = webrtc_streamer(
#     key="speech",
#     mode=WebRtcMode.SENDRECV,
#     audio_receiver_size=1024,
#     video_receiver_size=0,
#     audio_processor_factory=AudioProcessor,
#     media_stream_constraints={"audio": True, "video": False},
# )

# if ctx and ctx.state.playing:
#     st.info("🎙️ Listening... Speak now and then stop the stream.")

#     if st.button("📝 Process Voice"):
#         audio_data = ctx.audio_processor.get_audio()
#         waveform = torch.tensor(audio_data).float().unsqueeze(0)

#         with torch.inference_mode():
#             emissions, _ = model(waveform)
#         emissions = torch.log_softmax(emissions, dim=-1)
#         tokens = torch.argmax(emissions, dim=-1)

#         text = ""
#         for t in tokens[0]:
#             if t != 0:
#                 text += labels[t]
#         st.success(f"🗣️ You said: {text}")

#         bot_reply = gemini_response(text)
#         st.session_state.chat_history.append(("You", text))
#         st.session_state.chat_history.append(("Bot", bot_reply))
#         speak(bot_reply)
#         st.success("Bot replied and spoken!")

# st.markdown("---")

# # ---------- 📝 Chat History Section ----------
# st.markdown("## 📝 Chat History")
# for sender, message in st.session_state.chat_history:
#     if sender == "You":
#         st.markdown(f"<div style='background-color: #DCF8C6; padding:10px; border-radius:10px; margin:5px;'>🧑 <b>{sender}:</b> {message}</div>", unsafe_allow_html=True)
#     else:
#         st.markdown(f"<div style='background-color: #E6E6FA; padding:10px; border-radius:10px; margin:5px;'>🤖 <b>{sender}:</b> {message}</div>", unsafe_allow_html=True)

# st.markdown("---")
# st.markdown("<small>Made By Bhavesh with ❤️ using Streamlit & Google Gemini</small>", unsafe_allow_html=True)



# Without lllm
import streamlit as st
import os
import pyttsx3
import torch
import torchaudio
import requests
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import av
import numpy as np

# Text to Speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ✅ Simple logic-based chatbot response (No API needed)
def logic_bot_response(prompt):
    prompt = prompt.lower()

    if any(greet in prompt for greet in ["hi", "hello", "hey"]):
        return "Hello! How can I help you today? 😊"
    elif "your name" in prompt:
        return "I'm ChatBot Voice Bot, your friendly assistant! 🤖"
    elif "how are you" in prompt:
        return "I'm doing great, thank you! How about you? 🌟"
    elif "who made you" in prompt or "created you" in prompt:
        return "I was created by Bhavesh using Streamlit and Python! 🚀"
    elif "bye" in prompt or "goodbye" in prompt:
        return "Goodbye! Have a nice day! 👋"
    elif "weather" in prompt:
        return "I'm not connected to live weather right now, but I hope it's sunny where you are! ☀️"
    elif "time" in prompt:
        import datetime
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')} ⏰"
    elif "date" in prompt:
        import datetime
        return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')} 📅"
    else:
        return "Sorry, I didn't get that. Can you please ask something else? 🤔"

# Speech Recognition setup
bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
model = bundle.get_model()
labels = bundle.get_labels()

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.audio_buffer = []

    def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
        audio = frame.to_ndarray()
        audio = np.mean(audio, axis=0)
        self.audio_buffer.extend(audio)
        return frame

    def get_audio(self):
        return np.array(self.audio_buffer)

# Streamlit UI Config
st.set_page_config(page_title="💬 ChatBot + Voice Bot", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .chat-bubble {
        padding: 12px 16px;
        border-radius: 12px;
        margin: 8px 0;
        max-width: 80%;
        word-wrap: break-word;
        font-size: 16px;
        line-height: 1.4;
    }
    .user {
        background-color: #0084FF; /* Messenger Blue */
        color: white;
        text-align: right;
        margin-left: auto;
    }
    .bot {
        background-color: #F1F0F0; /* Light grey bubble */
        color: black;
        text-align: left;
        margin-right: auto;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 ChatBot + VoiceBot </h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Chat with AI using <b>Text</b> or <b>Voice</b></p>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.markdown("## 🚀 Text Chat")

user_input = st.text_input("💬 Type your message here:")

if st.button("Send Message"):
    if user_input:
        bot_reply = logic_bot_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", bot_reply))
        speak(bot_reply)
        st.success("✅ Bot replied and spoken!")

st.markdown("---")


st.markdown("## 🎙️ Voice Chat")

ctx = webrtc_streamer(
    key="speech",
    mode=WebRtcMode.SENDRECV,
    audio_receiver_size=1024,
    video_receiver_size=0,
    audio_processor_factory=AudioProcessor,
    media_stream_constraints={"audio": True, "video": False},
)

if ctx and ctx.state.playing:
    st.info("🎙️ Listening... Speak now and then stop the stream.")

    if st.button("📝 Process Voice"):
        audio_data = ctx.audio_processor.get_audio()
        waveform = torch.tensor(audio_data).float().unsqueeze(0)

        with torch.inference_mode():
            emissions, _ = model(waveform)
        emissions = torch.log_softmax(emissions, dim=-1)
        tokens = torch.argmax(emissions, dim=-1)

        text = ""
        for t in tokens[0]:
            if t != 0:
                text += labels[t]
        st.success(f"🗣️ You said: {text}")

        bot_reply = logic_bot_response(text)
        st.session_state.chat_history.append(("You", text))
        st.session_state.chat_history.append(("Bot", bot_reply))
        speak(bot_reply)
        st.success("✅ Bot replied and spoken!")

st.markdown("---")

# ---------- 📝 Chat History Section ----------
st.markdown("## 📝 Chat History")

for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"<div class='chat-bubble user'>🧑 <b>{sender}:</b> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble bot'>🤖 <b>{sender}:</b> {message}</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center; font-size: small;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
