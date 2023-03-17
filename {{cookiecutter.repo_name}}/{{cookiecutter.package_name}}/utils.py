import os

import pkg_resources
import yaml

base_path = os.path.dirname(os.path.dirname(
    pkg_resources.resource_filename("{{ cookiecutter.package_name }}", 'config')))

pkg_yaml = os.path.join(base_path, 'config', 'config.yml')


def load_pkg_yaml(yaml=pkg_yaml, **kwargs):
    """_summary_

    Args:
        yaml (_type_, optional): _description_. Defaults to pkg_yaml.

    Returns:
        _type_: _description_
    """

    with open(pkg_yaml, 'r') as f:
        y = yaml.safe_load(f)

    if 'subdict' in kwargs.keys():
        return y[kwargs['subdict']]
    else:
        return y
