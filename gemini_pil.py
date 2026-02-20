#https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python#generate_text_from_image_and_text_inputs

import PIL.Image
import google.generativeai as genai 
f = open("./data.txt", "r")


img = PIL.Image.open("images/باندات.png")
img2 = PIL.Image.open("images/زمزمية.png")
genai.configure(api_key=" your api - key") # تستطيع الحصول عليه من خلال الدخول للرابط https://aistudio.google.com/app/apikey واتباع نفس الخطوات
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction=f.read(),
)

def genaiImagesProccessing(text, img):
    if text:
        response = model.generate_content(
        [f"اكتب اسم المنتج الذي تتضمنه الصورة وقم بالرد على العميل حول معلوماته واجب على سؤال العميل الذي يسأل به '{text}'",
         img])
        print(response.text)
        return response.text
    else:
        response = model.generate_content(
        ["اكتب اسم المنتج الذي تتضمنه الصورة وقم بالرد على العميل حول معلوماته",
         img])
        print(response.text)
        return response.text

#genaiImagesProccessing( text=[], img=img) 

def genaiTextProccessing(text, history):
      chat_session = model.start_chat(
          history=history)
      response = chat_session.send_message(text)
      print(response.text)
      return response.text
#genaiTextProccessing("مرحبا", [])

