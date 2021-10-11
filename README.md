# greetings
Detects a known face and greets.

## Requirements

* Python 3.7
* OpenCV 3.4
* mediapipe 0.8

## Quick Start

1. Clone repo

```sh
git clone https://github.com/briandiaz/greetings.git
cd greetings
```


2. Create a virtual environment

```sh
python3 -m venv .venv
source .venv/bin/activate
````


3. Install dependencies

```sh
python3 -m pip install -r requirements.txt
```


4. Place photos from people you want to greet at `/assets` path.
* Image filename must be the name of the person. eg. brian.png, messi.png


5. Run project

```sh
python3 main.py
```



**Note**: If you're on a Linux system and the voice output is not working with this library, then you should install espeak, ffmpeg and libespeak1:

```sh
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```



# Author

Brian Díaz / [@briandiaz](https://www.briandiaz.me/)
