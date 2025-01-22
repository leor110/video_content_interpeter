import google.generativeai as genai
import time


# /change Gemini_API_KEY with your own key from this link --> https://aistudio.google.com/app/apikey
genai.configure(api_key="AIzaSyDPdRDJZdZppDZLjDoQ4Qd2aE6mThupSiE")
model = genai.GenerativeModel("gemini-1.5-flash")


# Upload the video and print a confirmation.
video_file_name = "Dog.mp4"
print(f"Uploading file...")
video_file = genai.upload_file(path=video_file_name)
print(f"Completed upload: {video_file.uri}")


# Check whether the file is ready to be used.
while video_file.state.name == "PROCESSING":
    print('.', end='')
    time.sleep(10)
    video_file = genai.get_file(video_file.name)

if video_file.state.name == "FAILED":
    raise ValueError(video_file.state.name)

# Create the prompt.
prompt = "Summarize this video"

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Make the LLM request.
print("Making LLM inference request...")
response = model.generate_content([video_file, prompt],
                                  request_options={"timeout": 600})
print(response.text)
