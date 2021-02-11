# dctrd.py
A tiny song splicing module written in Python3.

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
		"start": "00:00:000",
		"end": "01:32:350",
		"tts": {
			"text": "Mathew Mariani",
			"lang": "en",
			"slow": false
		}
	}, {
		"start": "01:33:000",
		"end": "03:38:000"
	}]
}
```

## License
This library is free software; you can redistribute it and/or modify it under
the terms of the MIT license. See [LICENSE](LICENSE) for details.