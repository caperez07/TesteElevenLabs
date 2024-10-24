from elevenlabs.client import ElevenLabs
from elevenlabs import play, save, stream, Voice, VoiceSettings

client = ElevenLabs(api_key="sk_db56eb1be139553f29a0432261e41a413e6147be57f626a7")

audio = client.generate(
   text="Oi, eu sou um teste!!",
   voice="River"
)

play(audio)
save(audio, "output.mp3")