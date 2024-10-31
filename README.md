# python-playwright-demo

This is a POC showing how Python can be used to drive playwright tests, that perform basic checks
of websites and capture screenshots of items that need manual verification. These screen shots are
then combined into a powerpoint document to simplify manual verification.

The expectation is that a final version will make full use of Playwright's assertion and visual check support and then python tooling to automate as much of the manual processing as possible.

## Usage

1. run the test suite `pytest --output-subdir=<DIR_NAME>` this saves the screenshots in the specified subdirectory of the projects output dir
2. run the powerpoint creation tool `python create_powerpoint.py <DIR_NAME>`
3. see the powerpoint you created `open output/<DIR_NAME>.pptx`

## How to

### Record a new test

run `npx playwright codegen amazon.co.uk` replace amazon,co.uk with the url to start from.
Once you've completed the test you can export it as python by chosing python from the target window

![target image](./assets/playwright-target.png)

### Run tests with browser output

Once the tests are recorded you can see what they are doing by running `pytest --browser webkit --headed`

### Resources to develop this further

Python playwright plugin:
* https://playwright.dev/python/docs/test-runners

Playwight Assertions:
* https://playwright.dev/docs/test-snapshots
* https://playwright.dev/docs/test-assertions

Create Powerpoint with python:
* https://python-pptx.readthedocs.io
* https://towardsdatascience.com/creating-presentations-with-python-3f5737824f61