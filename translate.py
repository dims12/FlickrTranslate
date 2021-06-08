# from google_trans_new import google_translator
from time import sleep

import httpcore
from googletrans import Translator
from httpcore import NetworkError

from tqdm import tqdm

import os

API_KEY = 'AIzaSyBN2tHuRePkOFatM92-cgbBZ4SRigpYMdk'
FLICKR_PATH = '/NAS/data/SpeechCorpora/Flickr8k'

INPUT_FILENAME = 'Flickr8k.token.txt'
# INPUT_FILENAME = 'Flickr8k.lemma.token.txt'
OUTPUT_FILENAME = 'Flickr8k.token.ru.txt'
RETRIES = 10
SLEEP_429 = 1


def translate():
    input_filepath = os.path.join(FLICKR_PATH, INPUT_FILENAME)
    output_filepath = os.path.join(OUTPUT_FILENAME)
    # translator = google_translator()
    translator = Translator()

    with open(input_filepath) as tokenfile:
        with open(output_filepath, "w") as translated_file:
            tokenlines = tokenfile.readlines()
            for line in tqdm(tokenlines):
                img_name, caption = line.split("\t")
                caption = caption.strip()

                again = 0
                SLEEP_429 = 5
                while again < RETRIES:
                    try:
                        caption_ru = translator.translate(caption, src='en', dest='ru')
                        if caption_ru._response.status_code == 429:
                            print("Sleeping %d..." % SLEEP_429)
                            sleep(SLEEP_429)
                            SLEEP_429 *= 2
                            continue
                        else:
                            caption_ru = caption_ru.text
                            break
                    except NetworkError as e:
                        print("Sleeping before retry...")
                        again += 1
                        sleep(10)

                if again < RETRIES:
                    translated_file.write("%s\t%s\n" % (img_name, caption_ru))
                else:
                    print("Skipped '%s' due to an error" % caption)


if __name__ == '__main__':
    translate()
