from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup

def parse_spec(url):
    soup = BeautifulSoup(urlopen(url).read().decode("utf-8"), "html.parser")
    suites = define_suite(soup, url)
    return suites

def define_suite(soup, link):
    parent_suite = {
        'name': soup.title.string,
        'link': link,
        'fn_name': soup.title.string.replace(' ', ''),
        'suites': []
    }
    for section in soup('section'):
        if not section.find_parent("section"):
            suite = {
                'name': section.get('id').replace('-', ' ').capitalize(),
                'link': link+section.get('id'),
                'fn_name': section.get('id').replace('-', '_'),
                'spec_id': section.get('id'),
                'subSuites': []
            }
            parent_suite['suites'].append(suite)
        if section.find_parent("section"):
            if section.get('id'):
                parent_id = section.find_parent("section").get('id')
                suite_id = section.get('id')
            else:
                continue
            sub_suite = {
                'name': suite_id.replace('-', ' ').capitalize(),
                'link': link+suite_id,
                'fn_name': suite_id.replace('-', '_'),
                'spec_id': suite_id,
                'tests': []
            }
            statements = find_rfc2119(section)
            for idx, statement in enumerate(statements):
                test = {
                    'name': statement,
                    'link': link+'#:~:text='+urllib.parse.quote(statement).replace('-', '%2D'),
                    'fn_name': suite_id.replace('-', '_')+f'_{idx}',
                }
                sub_suite['tests'].append(test)
            for idx, suite in enumerate(parent_suite['suites'].copy()):
                if suite['spec_id'] == parent_id and len(sub_suite['tests']) > 0:
                    parent_suite['suites'][idx]['subSuites'].append(sub_suite)
    
    parent_suite['suites'] = [suite for suite in parent_suite['suites'] if len(suite['subSuites']) > 0]
    parent_suite = numerate_names(parent_suite)

    return parent_suite

def find_rfc2119(section):
    statements=[]
    for tag in section.find_all('em'):
        if isinstance(tag.get('class'), list) and 'rfc2119' in tag.get('class'):
            if tag.find_parent():
                statements += parse_statement(tag.find_parent())
    statements = list(dict.fromkeys(statements))
    return statements

def parse_statement(statement):
    statement = " ".join(statement.get_text().split())
    statement = statement.replace('\"', "'")
    statement = statement.split('. ')
    statement = statement if isinstance(statement, list) else []
    for item in statement.copy():
        # keywords = ['MAY', 'MUST', 'REQUIRED', 'OPTIONAL', 'SHOULD']
        keywords = ['MUST', 'REQUIRED']
        if all(word not in item for word in keywords):
            statement.remove(item)
    return statement

def remove_duplicates(parent_suite):
    for idx, suite in enumerate(parent_suite['suites']):
        for sub_idx, sub_suite in enumerate(suite['subSuites']):
            for test_idx, test in enumerate(sub_suite['tests']):
                tests = []
                pass
    

def numerate_names(parent_suite):
    for idx, suite in enumerate(parent_suite['suites']):
        _suite_name = parent_suite['suites'][idx]['name']
        parent_suite['suites'][idx]['name'] = f'{idx:02d} {_suite_name}'
        for sub_idx, sub_suite in enumerate(suite['subSuites']):
            _sub_suite_name = parent_suite['suites'][idx]['subSuites'][sub_idx]['name']
            parent_suite['suites'][idx]['subSuites'][sub_idx]['name'] = f'{sub_idx:02d} {_sub_suite_name}'
            for test_idx, test in enumerate(sub_suite['tests']):
                _test_name = parent_suite['suites'][idx]['subSuites'][sub_idx]['tests'][test_idx]['name']
                parent_suite['suites'][idx]['subSuites'][sub_idx]['tests'][test_idx]['name'] = f'{test_idx:02d} {_test_name}'
    return parent_suite
    

def define_sections(soup, sections={}):
    for section in soup('section'):
        section_id = section.get('id')
        sections[section_id] = []
        for tag in section.find_all('em'):
            if isinstance(tag.get('class'), list) and 'rfc2119' in tag.get('class'):
                parent_tag = tag.find_parent()
                if parent_tag:
                    parent_tag = " ".join(parent_tag.get_text().split())
                    if parent_tag not in sections[section_id]:
                        sections[section_id].append(parent_tag)
        if len(sections[section_id]) == 0:
            sections.pop(section_id)
    sections = remove_duplicates(sections.copy())
    sections = split_sentences(sections.copy())
    return sections

def remove_duplicates(sections):
    for section in sections.copy():
        for other_section in sections.copy():
            if other_section == section:
                pass
            for statement in sections[section]:
                if statement in sections[other_section]:
                    sections[section].remove(statement)
    return sections

def split_sentences(sections):
    for section in sections.copy():
        for idx, statement in enumerate(sections[section]):
            statement = statement.replace('\"', "'")
            statement = statement.split('. ')
            statement = statement if isinstance(statement, list) else []
            sections[section].pop(idx)
            sections[section] += statement
    return sections