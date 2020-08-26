# Description: this script is used to extract all the clickable links
# that found from the given URL.
# Stores the links in different set: Same Hostname; Same Domain;
# Different Domain
# Author : Dung Ho


import re
import requests
import argparse
from bs4 import BeautifulSoup
from urllib.request import urlparse, urljoin


def is_valid(url):
    """
    Function checks whether 'url' is a valid URL.

    :param url: a given URL.

    :return: a boolean value.
    """

    if urlparse(url).scheme == 'http' or urlparse(url).scheme == 'https':
        return bool(urlparse(url).netloc) and bool(urlparse(url).scheme)

    else:

        return False


def get_links(url):
    """
    Function gets all the link from the given url.

    :param url: the given URL

    :return: print out the results based on the Hostname and Domain.
    """

    # Initialize
    same_hostname = set()       # Set of links which are same hostname
    same_domain = set()         # Set of links which are same domain
    different_domain = set()    # Set of links which are different domain

    # Returns Hostname
    hostname = urlparse(url).netloc
    split_hostname = re.split(r'\.', hostname)
    # Returns Domain name
    # 2 index from the right side
    domain = '.'.join(split_hostname[-2:])
    # Returns Top Level Domain
    # First index from the right side
    tld = ''.join(split_hostname[-1:])
    # Returns PATH
    path = urlparse(url).path

    # 'html.parser' is telling BeauifulSoup this is an HTML document
    result = BeautifulSoup(requests.get(url).content, 'html.parser')
    for a_tag in result.findAll('a'):
        link = a_tag.attrs.get('href')
        if link == '' or link is None:
            continue
        # Join the URL if it's relative
        link = urljoin(url, link)
        parsed_link = urlparse(link)
        # Checks if it is a valid Scheme, removes URL GET parameters
        # and URL fragments
        if is_valid(link):
            link = (
                parsed_link.scheme + '://' +
                parsed_link.netloc +
                parsed_link.path
            )
        else:
            continue
        # Checks and adds if same or not same Domain name
        if hostname not in link:
            if domain not in link:
                if link not in different_domain:
                    different_domain.add(link)
            else:
                if link not in same_domain:
                    same_domain.add(link)
                    continue
        # Add if same Hostname
        if hostname == urlparse(link).netloc:
            same_hostname.add(link)

    # Print results
    print('{:<10s} {:<5s}'.format('TLD: ', tld))
    print('{:<10s} {:<5s}'.format('DOMAIN: ', domain))
    print('{:<10s} {:<5s}'.format('HOSTNAME: ', hostname))
    print('{:<10s} {:<5s}'.format('PATH: ', path))

    print('LINKS: ')
    print(
        '{:<3} {} {} links'.format('', 'Same hostname: ', len(same_hostname))
    )
    for link1 in same_hostname:
        print('{:<6} {}'.format('', link1))

    print('{:<3} {} {} links'.format('', 'Same domain: ', len(same_domain)))
    for link2 in same_domain:
        print('{:<6} {}'.format('', link2))

    print(
        '{:<3} {} {} links'.format(
            '', 'Different domain: ', len(different_domain)
        )
    )
    for link3 in different_domain:
        print('{:<6} {}'.format('', link3))


def main():
    """
    Executes the get_link function with specific URL via CommandLine Interface.
    Return the results from get_link function.

    """
    parser = argparse.ArgumentParser(
        description='This tool is used for getting all the link from the' +
        ' given URL and storing in differrent set:-Same Hostname' +
        ' -Same Domain -Different Domain'
    )
    parser.add_argument(
        '--url', help='The URL to get links from.' +
        ' The URL format: http(s)://test.testdomain.org/xyz'
    )

    args = parser.parse_args()
    url = args.url

    if is_valid(url):
        get_links(url)

    else:

        print('Please input a valid URL!!!')


if __name__ == '__main__':
    main()
