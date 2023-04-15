
## Generating Develop Environment
### Building Docker development image
```sh
docker image build -t web-flask .
docker container run --rm -p 7071:7071 -p 5000:5000 -v ${PWD}:/app -it web-flask:latest
```

### Create a local anaconda environment
Create an anaconda environment using

```sh
conda create -n web-flask python=3.11
```

Install Dependencies

```sh
pip install -r requirements.txt
```

With flask installed, local development can begin by executing the main script.
It will reload when changes are made to source code.

```sh
python app/app.py
```

### Azure Function
This website is deployed as an azure function. To test that functionality locally,
the [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local)
need to be installed. Then the website can be started using

```sh
func start
```

## Configuration

*Note*: you can easily get a secret key using the python secrets library.

```python
>>> import secrets
>>> secrets.token_urlsafe() # use default length or supply your own
```