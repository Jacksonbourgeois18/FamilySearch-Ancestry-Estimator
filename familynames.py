from bs4 import BeautifulSoup
from collections import defaultdict
import requests


payload1 = ""
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en",
    "Accept-Encoding": "gzip, deflate, br",
    "FS-User-Agent-Chain": "tree-person-r9-prod (/tree/person/details/GD1W-23R)",
    "Authorization": "Bearer dbfcf0bc-5589-4be5-a566-873c36b280ce-prod",
    "sentry-trace": "46cb992da394489f8ec718d234dbebcb-a1163c3a6e21f413-0",
    "baggage": "sentry-environment=prod,sentry-release=tree-person-r9^%^402423^%^3A7d2795e5,sentry-public_key=e193e107f9c445f2878a47dee24af4e4,sentry-trace_id=46cb992da394489f8ec718d234dbebcb,sentry-sample_rate=0.001",
    "Origin": "https://www.familysearch.org",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.familysearch.org/tree/person/details/GD1W-23R",
    "Cookie": "fs_anid=a705e79a-cb7d-42a6-aec1-511d0acc293a; fsgeo=108.200.201.127; fs_experiments=u^%^3Dborgir^%^2Ca^%^3Dshared-ui^%^2Cs^%^3D45e9e95de143330dfddf5895fac1b67f^%^2Cv^%^3D11111011110000000000000000011101000100111001001100110111110000010010111111111011111111101100000100101011111010000110011011111100000000^%^2Cb^%^3D93^%^26a^%^3Dhome^%^2Cs^%^3Dea7a67fce90033aa89d45aab9128f76b^%^2Cv^%^3D0000100000110000000001101001011001111110010110001000011110100111111110000100000100111101100000000000000^%^2Cb^%^3D22^%^26a^%^3Dregistration-react^%^2Cs^%^3D62ca60b61c3ef1f09044157240f648fe^%^2Cv^%^3D00^%^2Cb^%^3D74^%^26a^%^3Dtree-v8^%^2Cs^%^3D467fe04e8bfe33465e127a6a772b2e94^%^2Cv^%^3D101100101101100010001111^%^2Cb^%^3D80^%^26a^%^3Dtree-person-r9^%^2Cs^%^3Df04aee2c1e4c0e0d11eab15b88d2717b^%^2Cv^%^3D0^%^2Cb^%^3D94; fslanguage=en; visid_incap_2852034=SgJlGBVwQMe4D/dGwQ7PIjUR3GMAAAAAQUIPAAAAAABMYch0Y1KgqQWJ62XwSrkG; nlbi_2852034=KggVM9IfrTu09/GmFzy7qAAAAACZz3kM7foDqWEIBzv1/NIE; incap_ses_1531_2852034=p+KVbC5DUD+/bWmppDQ/FaAR3GMAAAAAjqyyeeDU83iQY/GXPFI9YA==; nlbi_2852034_2147483392=mmfhRiblD0Fahf4hFzy7qAAAAABkhn6kFa0MKf/5J4WwYpNX; fs_recent_languages=en; fs-revisit=1; fs-tf=1; _gcl_au=1.1.69089949.1675366819; ctsplit=83; AMCV_66C5485451E56AAE0A490D45^%^40AdobeOrg=-2121179033^%^7CMCMID^%^7C72581803612462378260349348087278518770^%^7CMCAID^%^7CNONE^%^7CMCOPTOUT-1675374037s^%^7CNONE^%^7CvVersion^%^7C5.3.0; reese84=3:fh9lEecYstxFcFKOEN+M9A==:pfvDTzMzXa/nOHK2P8PLulaee99uR1ieAEBGQUsCGJVnDF9+CGVLBNO/iZVuEyg5dGDsc6cxWCRccIck1YoUC48OpUpAxUi1zNJ8LVwixZ5XEaLxOqbEItzzXFiVky+1aIjo3es9b/LtIk4jZ/ihyjECChJIV4MEU8Fysa3fWcHCjQBj70WjDOQaqhWvhCiKIv+x5cPaziU0O5rG1OA+qEgdX1T396ClbXcl+5yEJYWCKJkLACSjvX+JPq79TCnAP1fgCYmarVzeRYtYNauBJMGAG6fkQCHMMFt0+5MVPMmHdDuji2CTG12m/9ourcqWIhfarL6Ru+ZLsfaKzbIb8eHfP7/7X1ewSEIBfqSTKjXjJKZ3Hf48eRLivpXqQ/+xZIKJbTWEZUIgCdGAbaKjzFTXYkA87JXLzvPzfOSDa3XrV7N4DOSEz4TkcozA4STc3AkeKX+UA3L9/0jHy4swRA==:bHCYAo2RUzWlyqlOgPhx4lOs1KuMNVeBaPqW9HZcNic=; s_ecid=MCMID^%^7C72581803612462378260349348087278518770; AMCVS_66C5485451E56AAE0A490D45^%^40AdobeOrg=1; s_ppvl=FamilySearch^%^253A^%^2520Home^%^253A^%^2520LiHP-arches^%^2C100^%^2C49^%^2C994^%^2C1920^%^2C994^%^2C1920^%^2C1080^%^2C1^%^2CL; s_ppv=FamilySearch^%^253A^%^2520Tree^%^253A^%^2520Pedigree^%^253A^%^2520Fan^%^2520Chart^%^2C100^%^2C100^%^2C994^%^2C1920^%^2C704^%^2C1920^%^2C1080^%^2C1^%^2CL; s_cc=true; visid_incap_2876314=h0sOf5EGTtOW3rDKjyBYoKQR3GMAAAAAQUIPAAAAAADdhHhKLlCwbdET8lry3dem; nlbi_2876314=b8S8D8IzlBDIF9VhZDbeQwAAAACyE7Cam0UYdm9v0g/5CHhL; incap_ses_1531_2876314=BJLMR53RmWbwB2qppDQ/FaQR3GMAAAAAZXwR6HjR/ucTMFEurk847w==; nlbi_2876314_2147483392=yFapOoyrs0gKtL2BZDbeQwAAAAAQaFVY1dW9ZEE5bM418EYL; dtCookie=v_4_srv_7_sn_BF26C9C4C3876D2DF6D7CC9954DDE121_perc_100000_ol_0_mul_1_app-3A52ca64c87d7a17f1_1_rcs-3Acss_0; fssessionid=dbfcf0bc-5589-4be5-a566-873c36b280ce-prod; JSESSIONID=641C5B90BB273E311AB9D7D551CC2B1E; notice_behavior=implied^|us",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Content-Length": "0",
    "TE": "trailers"
}


querystring = {"includePhotos":"true"}
payload2 = ""
headers2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en",
    "Accept-Encoding": "gzip, deflate, br",
    "FS-User-Agent-Chain": "tree-person-r9-prod (/tree/person/details/GD1W-23R)",
    "Authorization": "Bearer dbfcf0bc-5589-4be5-a566-873c36b280ce-prod",
    "sentry-trace": "46cb992da394489f8ec718d234dbebcb-bf85b027e478598e-0",
    "baggage": "sentry-environment=prod,sentry-release=tree-person-r9^%^402423^%^3A7d2795e5,sentry-public_key=e193e107f9c445f2878a47dee24af4e4,sentry-trace_id=46cb992da394489f8ec718d234dbebcb,sentry-sample_rate=0.001",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.familysearch.org/tree/person/details/GD1W-23R",
    "Cookie": "fs_anid=a705e79a-cb7d-42a6-aec1-511d0acc293a; fsgeo=108.200.201.127; fs_experiments=u^%^3Dborgir^%^2Ca^%^3Dshared-ui^%^2Cs^%^3D45e9e95de143330dfddf5895fac1b67f^%^2Cv^%^3D11111011110000000000000000011101000100111001001100110111110000010010111111111011111111101100000100101011111010000110011011111100000000^%^2Cb^%^3D93^%^26a^%^3Dhome^%^2Cs^%^3Dea7a67fce90033aa89d45aab9128f76b^%^2Cv^%^3D0000100000110000000001101001011001111110010110001000011110100111111110000100000100111101100000000000000^%^2Cb^%^3D22^%^26a^%^3Dregistration-react^%^2Cs^%^3D62ca60b61c3ef1f09044157240f648fe^%^2Cv^%^3D00^%^2Cb^%^3D74^%^26a^%^3Dtree-v8^%^2Cs^%^3D467fe04e8bfe33465e127a6a772b2e94^%^2Cv^%^3D101100101101100010001111^%^2Cb^%^3D80^%^26a^%^3Dtree-person-r9^%^2Cs^%^3Df04aee2c1e4c0e0d11eab15b88d2717b^%^2Cv^%^3D0^%^2Cb^%^3D94; fslanguage=en; visid_incap_2852034=SgJlGBVwQMe4D/dGwQ7PIjUR3GMAAAAAQUIPAAAAAABMYch0Y1KgqQWJ62XwSrkG; nlbi_2852034=KggVM9IfrTu09/GmFzy7qAAAAACZz3kM7foDqWEIBzv1/NIE; incap_ses_1531_2852034=p+KVbC5DUD+/bWmppDQ/FaAR3GMAAAAAjqyyeeDU83iQY/GXPFI9YA==; nlbi_2852034_2147483392=mmfhRiblD0Fahf4hFzy7qAAAAABkhn6kFa0MKf/5J4WwYpNX; fs_recent_languages=en; fs-revisit=1; fs-tf=1; _gcl_au=1.1.69089949.1675366819; ctsplit=83; AMCV_66C5485451E56AAE0A490D45^%^40AdobeOrg=-2121179033^%^7CMCMID^%^7C72581803612462378260349348087278518770^%^7CMCAID^%^7CNONE^%^7CMCOPTOUT-1675374037s^%^7CNONE^%^7CvVersion^%^7C5.3.0; reese84=3:fh9lEecYstxFcFKOEN+M9A==:pfvDTzMzXa/nOHK2P8PLulaee99uR1ieAEBGQUsCGJVnDF9+CGVLBNO/iZVuEyg5dGDsc6cxWCRccIck1YoUC48OpUpAxUi1zNJ8LVwixZ5XEaLxOqbEItzzXFiVky+1aIjo3es9b/LtIk4jZ/ihyjECChJIV4MEU8Fysa3fWcHCjQBj70WjDOQaqhWvhCiKIv+x5cPaziU0O5rG1OA+qEgdX1T396ClbXcl+5yEJYWCKJkLACSjvX+JPq79TCnAP1fgCYmarVzeRYtYNauBJMGAG6fkQCHMMFt0+5MVPMmHdDuji2CTG12m/9ourcqWIhfarL6Ru+ZLsfaKzbIb8eHfP7/7X1ewSEIBfqSTKjXjJKZ3Hf48eRLivpXqQ/+xZIKJbTWEZUIgCdGAbaKjzFTXYkA87JXLzvPzfOSDa3XrV7N4DOSEz4TkcozA4STc3AkeKX+UA3L9/0jHy4swRA==:bHCYAo2RUzWlyqlOgPhx4lOs1KuMNVeBaPqW9HZcNic=; s_ecid=MCMID^%^7C72581803612462378260349348087278518770; AMCVS_66C5485451E56AAE0A490D45^%^40AdobeOrg=1; s_ppvl=FamilySearch^%^253A^%^2520Home^%^253A^%^2520LiHP-arches^%^2C100^%^2C49^%^2C994^%^2C1920^%^2C994^%^2C1920^%^2C1080^%^2C1^%^2CL; s_ppv=FamilySearch^%^253A^%^2520Tree^%^253A^%^2520Pedigree^%^253A^%^2520Fan^%^2520Chart^%^2C100^%^2C100^%^2C994^%^2C1920^%^2C704^%^2C1920^%^2C1080^%^2C1^%^2CL; s_cc=true; visid_incap_2876314=h0sOf5EGTtOW3rDKjyBYoKQR3GMAAAAAQUIPAAAAAADdhHhKLlCwbdET8lry3dem; nlbi_2876314=b8S8D8IzlBDIF9VhZDbeQwAAAACyE7Cam0UYdm9v0g/5CHhL; incap_ses_1531_2876314=BJLMR53RmWbwB2qppDQ/FaQR3GMAAAAAZXwR6HjR/ucTMFEurk847w==; nlbi_2876314_2147483392=yFapOoyrs0gKtL2BZDbeQwAAAAAQaFVY1dW9ZEE5bM418EYL; dtCookie=v_4_srv_7_sn_BF26C9C4C3876D2DF6D7CC9954DDE121_perc_100000_ol_0_mul_1_app-3A52ca64c87d7a17f1_1_rcs-3Acss_0; fssessionid=dbfcf0bc-5589-4be5-a566-873c36b280ce-prod; JSESSIONID=641C5B90BB273E311AB9D7D551CC2B1E; notice_behavior=implied^|us",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}


def scrape_ancestors(id, generation, tree):
    url1 = f"https://www.familysearch.org/service/tree/tree-data/history-list/cis.user.MMSX-QJTL/person/{id}"
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
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}
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
