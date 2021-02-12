# dctrd.py
A tiny song tts splicing module written in Python3.

## Dependencies
 - [gtts](https://pypi.org/project/gTTS/)
 - [pydub](https://pypi.org/project/pydub/)

## Usage
An `.mp3` file should be provided by the user.
You can run the module through your terminal by doing:
```
./dctrd.py -i input_file.json -o output_file.mp3
```

## Example
```json
{
	"song": "Shania-Twain-That-Dont-Impress-Me-Much.mp3",
	"tags": {
		"artist": "Various artists",
		"album": "Best of 2011",
		"comments": "This album is awesome!"
	},
	"segments": [{
		"skip": false,
		"begin": "01:32:320",
		"length": "00:01:040",
		"tts": {
			"text": "Brad Pitt",
			"lang": "en",
			"slow": false
		}
	}]
}
```

## License
This library is free software; you can redistribute it and/or modify it under
the terms of the MIT license. See [LICENSE](LICENSE) for details.