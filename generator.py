from jinja2 import Environment, PackageLoader, select_autoescape
from parser import parse_spec

SPECIFICATIONS = {
    'did-core': 'https://www.w3.org/TR/did-core/',
    'vc-di-eddsa': 'https://www.w3.org/TR/vc-di-eddsa/',
    'vc-di-ecdsa': 'https://www.w3.org/TR/vc-di-ecdsa/',
    'vc-data-model-v1': 'https://www.w3.org/TR/vc-data-model/',
    'vc-data-model-v2': 'https://www.w3.org/TR/vc-data-model-2.0/',
    'vc-data-integrity': 'https://www.w3.org/TR/vc-data-integrity/',
    'controller-document': 'https://www.w3.org/TR/controller-document/',
    'vc-bitstring-status-list': 'https://www.w3.org/TR/vc-bitstring-status-list/',
}

for spec in SPECIFICATIONS:
    parsed_spec = parse_spec(SPECIFICATIONS[spec])

    env = Environment(
        loader=PackageLoader("loader"),
        autoescape=select_autoescape()
    )
    test_suite_template = env.get_template("mocha-test-suite.jinja")
    test_suite = test_suite_template.render(parent_suite=parsed_spec, link=SPECIFICATIONS[spec])
    with open(f'test_suites/mocha/{spec}.js', 'w+') as f:
        f.write(test_suite)

    env = Environment(
        loader=PackageLoader("loader"),
        autoescape=select_autoescape()
    )
    test_suite_template = env.get_template("pytest-test-suite.jinja")
    test_suite = test_suite_template.render(parent_suite=parsed_spec, link=SPECIFICATIONS[spec])
    with open(f'test_suites/pytest/test_{spec.replace("-", "_")}.py', 'w+') as f:
        f.write(test_suite)




