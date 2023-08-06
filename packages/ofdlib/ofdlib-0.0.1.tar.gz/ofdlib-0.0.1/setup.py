# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['ofdlib']
install_requires = \
['lxml>=4.9.2,<5.0.0',
 'numpy>=1.17.0,<2.0.0',
 'pydantic>=1.10.8,<2.0.0',
 'rich>=13.4.2,<14.0.0']

setup_kwargs = {
    'name': 'ofdlib',
    'version': '0.0.1',
    'description': '',
    'long_description': '# OFD\n\nOFD 文档解析库,开发中...\n\n- [x] Reader\n- [ ] Writer\n- [ ] Convertor\n\n## OFD 解析\n\n```python\nfrom ofdlib import Reader\n\nfile = "your_path_of_ofd_document.ofd"\nofd = Reader(file)\n\nprint(ofd.OFD)\nprint(ofd.documents)\n\nfor page in ofd.documents[0].pages():\n    print(page)\n    page.show()\n\n```\n\n## 参考资料\n\n[jyh2012/ofd-parser](https://github.com/jyh2012/ofd-parser)\n[DLTech21/ofd.js](https://github.com/DLTech21/ofd.js)\n[ofdrw/ofdrw](https://github.com/ofdrw/ofdrw)\n',
    'author': 'hbh112233abc',
    'author_email': 'hbh112233abc@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
