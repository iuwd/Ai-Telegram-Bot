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
  "You are a bot that helps people with educational problems.", 
  "Don't use rude words.",
  "GAT is a national test for a highschooler in the Kingdom of Saudi Arabia, It is close to the SAT but has some differences." ],
)

# --- Functions ---
def ai(prompt):
  print(prompt)
  response = model.generate_content(prompt)
  while(True):
    if response._done:
      return(response.text)
