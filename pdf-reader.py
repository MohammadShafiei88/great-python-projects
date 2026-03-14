import re
from collections import Counter
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path: str) -> list[str]:
    with open(pdf_path, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)
        print('pages: ', len(reader.pages))
        print('-'*20)

        pdf_text : list[str] = [ pages.extract_text() for pages in reader.pages]
        return pdf_text

def count_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        #print(split_text)
        all_words += [word for word in split_text if word]

    return Counter(all_words)


def main():
    extract_text: list[str] = extract_text_from_pdf('sample.pdf')
    counter: Counter = count_words(extract_text)
    for word, count in counter.most_common(5):
        print(f'{word:7}: {count}')

if __name__ == '__main__':
    main()





