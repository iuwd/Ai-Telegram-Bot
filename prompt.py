import json
import google.generativeai as genai


# --- Configuration ---
genai.configure(api_key="Gemini API TOKEN")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction=[ 
  "Don't use rude words.",
    )

# --- Functions ---
def ai(prompt):
  print(prompt)
  response = model.generate_content(prompt)
  while(True):
    if response._done:
      return(response.text)
