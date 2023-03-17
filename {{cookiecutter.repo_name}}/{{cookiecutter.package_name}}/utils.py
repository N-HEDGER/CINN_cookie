import pkg_resources
import yaml

DATA_PATH = pkg_resources.resource_filename(
    "{{ cookiecutter.package_name }}", 'config')
pkg_yaml = os.path.join(DATA_PATH, 'config.yml')


def load_pkg_yaml(yaml=pkg_yaml):
    """_summary_

    Args:
        yaml (_type_, optional): _description_. Defaults to pkg_yaml.

    Returns:
        _type_: _description_
    """

    with open(pkg_yaml, 'r') as f:
        y = yaml.safe_load(f)
    return y