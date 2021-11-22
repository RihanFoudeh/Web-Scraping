import requests

from bs4 import BeautifulSoup


wikipedia_URL = "https://en.wikipedia.org/wiki/History_of_Mexico"


def get_citations_needed_count(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find_all('a', title='Wikipedia:Citation needed')

    return (len(result))

########################################################################


def get_citations_needed_report(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find_all('a', title='Wikipedia:Citation needed')

    all_p_contain_citation = []

    for p in result:
        all_p_contain_citation.append(p.parent.parent.parent.text)

    return '\n'.join(all_p_contain_citation)


if __name__ == '__main__':

    print(get_citations_needed_report(wikipedia_URL))
    print(get_citations_needed_count(wikipedia_URL))

########################################################################
