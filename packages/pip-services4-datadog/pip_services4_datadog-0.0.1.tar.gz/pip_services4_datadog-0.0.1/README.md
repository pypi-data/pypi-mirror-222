# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> DataDog components for Pip.Services in Python

This module is a part of the [Pip.Services](http://pipservices.org) polyglot microservices toolkit.
It contains the DataDog logger and performance counters components.

The module contains the following packages:
- **Build** - contains a class used to create DataDog components by their descriptors.
- **Clients** - contains constants and classes used to define REST clients for DataDog
- **Count** - contains a class used to create performance counters that send their metrics to a DataDog service
- **Log** - contains a class used to create loggers that dump execution logs to a DataDog service.

<a name="links"></a> Quick links:

* [Configuration](https://www.pipservices.org/recipies/configuration)
* [API Reference](https://pip-services3-python.github.io/pip-services4-datadog-python/index.html)
* [Change Log](CHANGELOG.md)
* [Get Help](https://www.pipservices.org/community/help)
* [Contribute](https://www.pipservices.org/community/contribute)

## Use

Install the Python package as
```bash
pip install pip-services4-datadog
```

## Develop

For development you shall install the following prerequisites:
* Python 3.7+
* Visual Studio Code or another IDE of your choice
* Docker

Install dependencies:
```bash
pip install -r requirements.txt
```

Run automated tests:
```bash
python test.py
```

Generate API documentation:
```bash
./docgen.ps1
```

Before committing changes run dockerized build and test as:
```bash
./build.ps1
./test.ps1
./clear.ps1
```

## Contacts

The Python version of Pip.Services is created and maintained by
- **Sergey Seroukhov**
- **Danil Prisiazhnyi**
