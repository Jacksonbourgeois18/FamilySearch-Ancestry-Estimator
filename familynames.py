from bs4 import BeautifulSoup
from collections import defaultdict
import requests


payload1 = ""
headers1 = {}


querystring = {"includePhotos":"true"}
payload2 = ""
headers2 = {}

user_id = ""

def scrape_ancestors(id, generation, tree):
    url1 = f"https://www.familysearch.org/service/tree/tree-data/history-list/cis.user.{user_id}/person/{id}"
    r1 = requests.request("PUT", url1, data=payload1, headers=headers1)
    data1 = r1.json()
    name = data1.get('data').get('name')
    url2 = f"https://www.familysearch.org/service/tree/tree-data/r9/family-members/person/{id}"
    r2 = requests.request("GET", url2, data=payload2, headers=headers2, params=querystring)
    data2 = r2.json()
    print(name, generation)
    if not data2.get('parents') or generation >= 10:
        tree.append([name, generation])
        return
    parent1id = data2.get('parents')[0].get('parent1').get('id')
    parent2id = data2.get('parents')[0].get('parent2').get('id')
    tree.append([name, generation])
    if parent1id == 'UNKNOWN':
        tree.append([name, generation + 1])
    else:
        scrape_ancestors(parent1id, generation + 1, tree)
    if parent2id == 'UNKNOWN':
        tree.append([name, generation + 1])
    else:
        scrape_ancestors(parent2id, generation + 1, tree)


# Scraping is broken into four parts in order to avoid timeouts. Each grandparent's tree is scraped individually,
# while parents and the root are added manually
def assemble_tree():
    family_tree = []
    you = input('Type your name: ')
    parent1 = input('Type name of first parent: ')
    parent2 = input('Type name of second parent: ')
    gparentid1 = input('Type Family Search ID of first grandparent: ')
    gparentid2 = input('Type Family Search ID of second grandparent: ')
    gparentid3 = input('Type Family Search ID of third grandparent: ')
    gparentid4 = input('Type Family Search ID of fourth grandparent: ')
    family_tree.append([you, 0])
    family_tree.append([parent1, 1])
    scrape_ancestors(gparentid1, 2, family_tree)
    scrape_ancestors(gparentid2, 2, family_tree)
    family_tree.append([parent2, 1])
    scrape_ancestors(gparentid3, 2, family_tree)
    scrape_ancestors(gparentid4, 2, family_tree)
    return family_tree


titles = ['Junior', 'Jr', 'Jr.', 'JR', 'JR.', 'Senior', 'Sr', 'Sr.', 'SR', 'SR.', 'i', 'ii', 'iii', 'I', 'II', 'III']
special_char_dict = {
    'à': 'a',
    'é': 'e',
    'è': 'e',
    'î': 'i',
    'ö': 'o',
    'ü': 'u',
    'ç': 'c',
    'ñ': 'n',
    'ÿ': 'y'
}


def format_names(names):
    formatted = []
    for person in names:
        name = person[0].split()
        if name[-1] in titles:
            name.pop(-1)
        formatted.append([name[-1], person[1]])
    for person in formatted:
        for i, char in enumerate(person[0]):
            if char in special_char_dict:
                person[0] = person[0][:i] + special_char_dict[char] + person[0][i+1:]
    return formatted


def get_terminals(tree):
    terminals = []
    previous = [None, -1]
    for person in tree:
        if person[1] <= previous[1]:
            terminals.append(previous)
        previous = person
    terminals.append(previous)
    return terminals


def scrape_origins(name_list):
    output_list = []
    headers = {}
    for person in name_list:
        possible = []
        url = f'https://www.familysearch.org/en/surname?surname={person[0]}'
        data = requests.get(url, headers=headers).text
        soup = BeautifulSoup(data, 'html.parser')
        countries = soup.find_all('h3', class_='countryTitleText')
        if len(countries) == 0:
            output_list.append(['UNKNOWN', person[1]])
            continue
        for country in countries:
            possible.append(country.text)
        while possible[0] == 'United States' or possible[0] == 'Canada':
            possible.pop(0)
        output_list.append([possible[0], person[1]])
        print(person, possible[0])
    return output_list


def def_value():
    return 0


def determine_admixture(weighted_countries):
    ancestry_dict = defaultdict(def_value)
    for place in weighted_countries:
        ancestry_dict[place[0]] += 1 / 2 ** place[1]
    return ancestry_dict


def main():
    full_family_tree = assemble_tree()
    endpoint_lastnames = format_names(get_terminals(full_family_tree))
    country_list = scrape_origins(endpoint_lastnames)
    result = determine_admixture(country_list)
    return result


print(main())
