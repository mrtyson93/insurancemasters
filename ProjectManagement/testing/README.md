# How to run the testing?

You need a couple prerequisite installs for this to work, those are pytest and selenium.
You can install both of those by running

```bash
$ pip install selenium
$ pip install pytest
```

After installing, to run the tests, you first need to start up the flask app locally, then while in the testing directory, all you need to do is run the command

```bash
$ pytest
```

This command automatically picks up any tests from files that are named "test\_\*"
