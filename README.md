# fe_project
## Overview
This is a database project aimed to model the time series dataset from individual buildings from [OEDI](https://data.openei.org/submissions/4520). We use Python and Django to model the data with a SQLite backend.

## Installation
### Django
Ensure that you have Django installed, see [docs](https://docs.djangoproject.com/en/4.2/intro/install/) for instructions
### Python
Ensure that you have Python installed, see [docs](https://www.python.org/downloads/) for instructions
### Python Packages
```bash
pip install -r requirements.txt
```
### Back to Django
```bash
python manage.py migrate
```

```bash
python oedi/parsers.py
```

```bash
python manage.py shell
```
#### Once in shell
```python
from fe_project.oedi.models import *
OEDIBuildingEnergyUsage.objects.all()
```
