# translate_demo.py — optional code path for Lab G.
#
# The lab is designed to be done entirely in the GCP Console (no code required).
# This script is provided for trainees who want to see the same pretrained API
# called from Python instead of the console demo widget.
#
# Setup (only if you want to run this):
#   pip install google-cloud-translate
#   gcloud auth application-default login
#   (Cloud Translation API must already be enabled on your ai-lab-day2 project)

from google.cloud import translate_v2 as translate


def main():
    client = translate.Client()

    text_en = "The training today was excellent."
    result = client.translate(text_en, target_language="am")
    print(f"EN -> AM: {result['translatedText']}")

    text_am = "\u12a0\u1218\u1230\u130d\u1293\u1208\u1201"  # "Thank you" in Amharic
    result2 = client.translate(text_am, target_language="en")
    print(f"AM -> EN: {result2['translatedText']}")


if __name__ == "__main__":
    main()
