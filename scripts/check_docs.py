"""Verify the documentation and the specific risk of removing legacy resources."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
BASE_URL = 'https://trustoverip.github.io/dtgwg-htx-tf/'
PREFIX = '/dtgwg-htx-tf/'
STATIC = {'.html', '.css', '.js', '.json', '.png', '.jpg', '.jpeg', '.svg', '.gif', '.pptx'}


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.edit = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get('id'):
            self.ids.add(values['id'])
        if tag == 'a' and values.get('id') == 'edit-this-page':
            self.edit = values.get('href')
        for key in ('href', 'src'):
            if values.get(key):
                self.links.append(values[key])


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def check(baseline):
    failures = []
    old_paths = git('ls-tree', '-r', '--name-only', '-z', baseline).decode().split('\0')
    static_paths = [
        p for p in old_paths
        if p and Path(p).suffix.lower() in STATIC
        and not any(part.startswith(('_', '.')) for part in Path(p).parts)
    ]
    for name in static_paths:
        original = git('show', f'{baseline}:{name}')
        for label, path in [('source', ROOT / name), ('published file', SITE / name)]:
            if not path.is_file() or path.read_bytes() != original:
                failures.append(f'Existing {label} changed or missing: {name}')

    pages = sorted((SITE / 'docs').rglob('*.html'))
    if not pages:
        failures.append('No documentation HTML was built.')
    pages += [SITE / 'index.html']
    parsed = {}
    for path in pages:
        if not path.is_file():
            failures.append(f'Missing page: {path.relative_to(SITE)}')
            continue
        text = path.read_text()
        if '{{' in text or '{%' in text:
            failures.append(f'Unrendered Liquid in {path.relative_to(SITE)}')
        parsed[path] = Page(text)

    for path, page in list(parsed.items()):
        current_url = urljoin(BASE_URL, path.relative_to(SITE).as_posix())
        for href in page.links:
            url = urlsplit(urljoin(current_url, href))
            if url.scheme not in ('http', 'https') or url.netloc != 'trustoverip.github.io':
                continue
            if not url.path.startswith(PREFIX):
                continue
            relative = unquote(url.path[len(PREFIX):])
            target = SITE / relative
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                failures.append(f'Broken local link in {path.relative_to(SITE)}: {href}')
                continue
            if url.fragment and target.suffix == '.html':
                if target not in parsed:
                    parsed[target] = Page(target.read_text())
                if unquote(url.fragment) not in parsed[target].ids:
                    failures.append(f'Missing anchor in {path.relative_to(SITE)}: {href}')
        if '/docs/' in str(path) and not page.edit:
            failures.append(f'Missing edit link: {path.relative_to(SITE)}')
        if page.edit:
            expected = 'https://github.com/trustoverip/dtgwg-htx-tf/edit/main/'
            source = unquote(page.edit.removeprefix(expected))
            if not page.edit.startswith(expected) or not (ROOT / source).is_file():
                failures.append(f'Incorrect edit link in {path.relative_to(SITE)}: {page.edit}')

    families = (ROOT / 'docs/patterns/index.md').read_text()
    moments = (ROOT / 'docs/taxonomy/moments.md').read_text()
    if set(re.findall(r'id="p(\d+)"', families)) != {f'{n:02}' for n in range(1, 19)}:
        failures.append('The catalogue must retain P01–P18.')
    if set(re.findall(r'id="t(\d+)"', moments)) != {str(n) for n in range(1, 14)}:
        failures.append('The moment index must retain T1–T13.')
    search_path = SITE / 'assets/js/search-data.json'
    if not search_path.is_file():
        failures.append('Search data was not generated.')

    if failures:
        print('\n'.join(sorted(set(failures))))
        return 1
    print(f'PASS: {len(static_paths)} existing static files preserved byte-for-byte; '
          f'{len(pages)} new HTML pages and their links checked; '
          'edit links, search data, 18 families and 13 moments verified.')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--baseline', required=True)
    sys.exit(check(parser.parse_args().baseline))
