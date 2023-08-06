import openai

KEY='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'
openai.api_key = KEY


file = open("1.mp3",'rb')

result = openai.Audio.transcribe(
 api_key=KEY,
 model='whisper-1',
 file=file,
 response_format='text'
)


result2 = openai.Audio.translate(
 api_key=KEY,
 model='whisper-1',
 file=file,
 response_format='text'
)

print(result)
print(result2)