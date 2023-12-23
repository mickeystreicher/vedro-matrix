# vedro-matrix

`vedro-matrix` is a Python package that extends the `vedro` framework, enabling parameterized testing with matrix combinations. It simplifies the process of creating and managing multiple test scenarios, especially when dealing with combinations of different test parameters like browsers, screen resolutions, user types, etc.

## Installation

Install `vedro-matrix` using pip:

```sh
$ pip install vedro-matrix
```

## Usage

To use `vedro-matrix`, import the `params_matrix` decorator from the package and apply it to your test scenarios in a `vedro` test suite.

### Example

Here is an example of how to use `vedro-matrix` to test a web page's rendering on different browsers and resolutions:

```python
import vedro
from vedro_matrix import params_matrix

class Scenario(vedro.Scenario):
    subject = "Open /about page ({browser}, {resolution})"

    @params_matrix(
        ["chrome", "firefox"],
        ["1024x720", "1920x1080"],
    )
    def __init__(self, browser, resolution):
        self.browser = browser
        self.resolution = resolution

    def when_user_opens_page(self):
        self.page = open_about_page(self.browser, self.resolution)

    def then_it_should_show_main_content(self):
        assert self.page.main_content.is_visible()
```

This script will generate and run 4 separate test scenarios:

1. Open /about page (chrome, 1024x720)
2. Open /about page (chrome, 1920x1080)
3. Open /about page (firefox, 1024x720)
4. Open /about page (firefox, 1920x1080)

### Running Tests

Run the scenarios using the `vedro` command:

```sh
$ vedro run
```

You should see an output similar to the following, indicating that all scenarios have passed:

```sh
Scenarios
*
 ✔ Open /about page (chrome, 1024x720)
 ✔ Open /about page (chrome, 1920x1080)
 ✔ Open /about page (firefox, 1024x720)
 ✔ Open /about page (firefox, 1920x1080)

# --seed 79b84f2d-e98c-47bf-b057-acdf597c4143
# 4 scenarios, 4 passed, 0 failed, 0 skipped (1.51s)
```
