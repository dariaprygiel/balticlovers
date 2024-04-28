## Automated testing suite for Balticlovers.pl 

This project is aimed at automating test cases for an ecommerce store **[Balticlovers.pl](balticlovers.pl)**, using Selenium and Python. The test cases cover various functionalities of the store, such as user registration, contact form submission, product browsing, and checkout process.

These test cases were crafted to ensure thorough examination of a live product environment, considering good standards by refraining from actions that could disrupt the store's operations, such as creating fictitious accounts or placing spurious orders.

The project was developed as part of the credit for postgraduate studies in the course: _Automation Tester in Selenium_. 

### Test cases

* Loading the homepage **_balticlovers.pl_** (#001)
* Displaying the product in the default carousel view **_NEW IN BALTICLOVERS_** (#002)
* Submitting the contact form (#003 - #005)
* Adding the product to the wishlist (#006)
* Verifying the increment of items in the shopping cart (#007)
* Loading the registration page (#008)
* Registering a new user (#009 - #012)
* Placing an order (#013 - #015)

### Setup

1. **Clone the repository:**

    ```bash
    git clone 
    ```

2. **Download and install the appropriate webdriver:**

    Depending on the browser you want to automate, download the appropriate webdriver and add it to your system's PATH.

### Usage

1. **Run the test cases:**

    ```bash
    python balticlovers_suite_test.py
    ```

   This will execute all the test cases and provide the test results.

### Acknowledgements

- The online store **[Balticlovers.pl](balticlovers.pl)**
- The whole team at Flowrite; for support and cheering in this development journey
- For **[Shuvro](https://github.com/shuvro)**; for encouraging me to develop my skills first and for planting that seed of eagerness to learn! 