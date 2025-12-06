from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

class OpenAIHandler:
    def __init__(self):
        """Initialize OpenAI client with API key from .env or secrets"""
        # Load environment variables
        load_dotenv()
        
        # Try to get API key from .env first, then secrets.toml
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            try:
                api_key = st.secrets["OPENAI_API_KEY"]
            except:
                raise ValueError("OPENAI_API_KEY not found in .env or secrets.toml")
        
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-3.5-turbo"
    
    def get_streaming_response(self, messages):
        """Get streaming response from OpenAI API"""
        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=True,
                temperature=0.7,
                max_tokens=1000
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            yield f"Error: {str(e)}"
    
    def get_response(self, messages):
        """Get non-streaming response from OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
