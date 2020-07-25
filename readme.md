
# Steps

1. install python 3 (https://www.python.org/downloads/)
2. install pip (https://pip.pypa.io/en/stable/installing/)
3. install venv (https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
4. clone this repo, and cd the repo directory
5. create environment (`cd .. && virtualenv covid-ds-backend`)
6. activate the environment (`cd covid-ds-backend && source bin/activate`)
7. install dependencies (`pip install -r requirements.txt`)
8. run `docker-compose up -d`
9. Configure in PyCharm community IDE a new Flask app using `app.py` file as entrypoint

Code editor: PyCharm community

# First steps

in `app.py` you'll see the available requests. Initially the mongodb is empty to fill it run:

```bash
curl -X POST http://localhost:5000/load
```

That is going to load the file `data.json` in mongodb as two collections: countries and series.

Now you can retrieve countries or series:

`curl http://localhost:5000/country/AFG`
 
`curl http://localhost:5000/series/country/AFG`