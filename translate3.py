from google.cloud import translate_v2 as translate

from tqdm import tqdm

import os

FLICKR_PATH = '.'

INPUT_FILENAME = 'Flickr8k.token.txt'
# INPUT_FILENAME = 'Flickr8k.lemma.token.txt'
OUTPUT_FILENAME = 'Flickr8k.token.ru.txt'


def main():
    input_filepath = os.path.join(FLICKR_PATH, INPUT_FILENAME)
    output_filepath = os.path.join(OUTPUT_FILENAME)

    translator = translate.Client()

    with open(input_filepath) as tokenfile:
        with open(output_filepath, "w") as translated_file:
            tokenlines = tokenfile.readlines()
            for line in tqdm(tokenlines):
                img_name, caption = line.split("\t")
                caption = caption.strip()

                result = translator.translate(caption, target_language="ru", source_language="en")
                caption_ru = result['translatedText']
                translated_file.write("%s\t%s\n" % (img_name, caption_ru))


if __name__ == '__main__':
    main()
