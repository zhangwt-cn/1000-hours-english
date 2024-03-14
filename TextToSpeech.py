from openai import OpenAI

# get local file cotent, for example: 2024/02-27


path = "2024/03-15/"
material_file = "english.md"
material_path = path + material_file
material_content = ""
with open(material_path, "r") as file:
    material_content = file.read()

if material_content == "":
    print("File not found or empty")
    exit(1)


client = OpenAI()
response = client.audio.speech.create(
    model="tts-1-hd",
    voice="echo",
    input=material_content,
    response_format="flac"
)


response.write_to_file("{}material.flac".format(path))
