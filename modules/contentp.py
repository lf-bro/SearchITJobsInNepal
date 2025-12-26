# AIzaSyDlyaLHwuBlyBTIbZud43__Uj4VHg2S41s

from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyDlyaLHwuBlyBTIbZud43__Uj4VHg2S41s")

def contentGen (info) :
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"You need to give me summerized and short and quick info based on following. Give me as json as following keys title, position, summery, skills, salary, type (fulltime, parttime, remote). {info}"
    )
    return response.text

