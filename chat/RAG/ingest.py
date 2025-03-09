from  google.generativeai  import genai

client = genai.Client(api_key="AIzaSyBR1LOMFem4oCaq9Xw17RYqFm48d9InJgY")

result = client.models.embed_content(
        model="text-embedding-004",
        contents="What is the meaning of life? this is yassine ")

print(result.embeddings)
