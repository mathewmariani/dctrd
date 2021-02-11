import sys, getopt
import json

from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment

def timestamp_to_ms(timestamp):
	t = list(map(int, timestamp.split(":")))
	return t[0]*60*1000+t[1]*1000+t[2]

def convert_text_to_audiosegment(tts):
	mp3_fp = BytesIO()
	text = tts["text"]
	lang = tts["lang"]
	slow = tts["slow"]
	tts = gTTS(text=text, lang=lang, slow=slow).write_to_fp(mp3_fp)
	mp3_fp.seek(0)
	return AudioSegment.from_mp3(mp3_fp)	

def dctrd_desc_defaults(desc):
	assert ("song" in desc), "A song is required"
	if not ("tags" in desc):
		desc["tags"] = None
	if not ("segments" in desc):
		desc["segments"] = []
	else:
		for segment in desc["segments"]:
			assert ("start" in segment), "A start timestamp is required"
			assert ("end" in segment), "An end timestamp is required"
			if "tts" in segment:
				assert ("text" in segment["tts"]), "TTS requires text"
				if not ("lang" in segment["tts"]):
					segment["tts"]["lang"] = "en"
				if not ("slow" in segment["tts"]):
					segment["tts"]["slow"] = False

def dctrd_create_song(desc, outfile):
	print("Loading orginal song...")
	song = AudioSegment.from_mp3(desc["song"])

	print("Mixing doctored song...")
	combined = AudioSegment.empty()
	for segment in desc["segments"]:
		start = timestamp_to_ms(segment["start"])
		end = timestamp_to_ms(segment["end"])
		combined += song[start:end]
		if "tts" in segment:
			combined += convert_text_to_audiosegment(segment["tts"])

	print("Exporting doctored song...")
	combined.export(outfile, format="mp3", tags=desc["tags"])

def dctrd_make_song(infile, outfile):
	print("Loading JSON...")
	with open(infile) as f:
		desc = json.load(f)

	dctrd_desc_defaults(desc)
	dctrd_create_song(desc, outfile)
	print("Done!")

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["input=", "output="])
	except getopt.GetoptError:
		sys.exit(2)
	for opt, arg in opts:
		if opt == "-h":
			sys.exit()
		elif opt in ("-i", "--input"):
			infile = arg
		elif opt in ("-o", "--output"):
			outfile = arg

	assert infile, "an input file is required"
	assert outfile, "an ouput file is required"

	dctrd_make_song(infile, outfile)

if __name__ == "__main__":
	main(sys.argv[1:])