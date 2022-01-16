
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

# Book store
> An example of book storage based on ORM (sqlalchemy) and fastapi.

## Tools

### Production
- python 3.6+
- [fastapi](https://fastapi.tiangolo.com/)
- [sqlalchemy](https://www.sqlalchemy.org)

### Development

- [travis](https://travis-ci.org/)
- [pytest](https://pypi.org/project/pytest/)
- [black](https://black.readthedocs.io/en/stable/)
- [flake8](http://flake8.pycqa.org/en/latest/)

## Usage

### Quick start

```bash
git clone git@github.com:vyahello/book-store.git
cd book-store
python3 -m venv venv 
. venv/bin/activate
pip install -r requirements.txt
python main.py
```

Then please open http://0.0.0.0:8000 in your browser.

**[⬆ back to top](#book-store)**

## Development notes

### API 

Please check http://0.0.0.0:8000/docs swagger documentation in your browser.

### Database migration with alembic
TBD

### Testing

Generally, `pytest` tool is used to organize testing procedure.

Please follow next command to run unittests:
```bash
pytest
```

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `flake8`) and unittests (`pytest`) will be run automatically after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-source-code.sh
```

### Meta

Author – _Vladimir Yahello_. 

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing

I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (git checkout -b feature/fooBar)
6. Commit your changes (git commit -am 'Add some fooBar')
7. Push to the branch (git push origin feature/fooBar)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/vyahello/book-store/issues) page. 
If you have ideas you want to change/implement please do not hesitate and create an issue.

**[⬆ back to top](#book-store)**