# <a href="https://apresapparel.herokuapp.com/">Après Apparel</a>

![responsive_screenshot]()

This [project](https://apresapparel.herokuapp.com/) is my fourth milestone project (Full Stack Frameworks with Django) in Full Stack Software Development course run by [Code Institute](https://codeinstitute.net/)

Après Apparel is an outdoor lifestyle brand founded by my friend, Stephen Rice, with the main aim of supplying apparel & accessories to suit 
your outdoor lifestyle.

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)
    - [**Known Issues**](#known-issues)
    - [**Automated Testing**](#automated-testing)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

---

## UX
 
This e-commerce site is made for those who love adventuring and the outdoors!
We also have a section dedicated to athletes we support & follow, and the team members behind the Après Apparel brand.

"**_As a user, I would like to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark: *view the site* from **any device** *(mobile, tablet, desktop)*.
- :white_check_mark: *view all products* as a **Guest**.
- :white_check_mark: *view individual product details* as a **Guest**.
- :white_check_mark: *add products to my shopping bag* as a **Guest**.
- :white_check_mark: *remove products from my shopping bag* as a **Guest**.
- :white_check_mark: *manage products in my shopping bag* as a **Guest**
- :white_check_mark: *sort/order products* by **name, category, price, rating**.
- :white_check_mark: *search products* by **name, category, description**.
- :white_check_mark: **limit** the number of *products* to display by name (alphabetical sorting), product category type, or see *all products*.
- :white_check_mark: *create* my **own profile** with secure email verification as a **User**.
- :white_check_mark: *update* & *manage* my **email address, password, delivery information** as a **Registered User**.
- :white_check_mark: *view* **bag subtotal** whilst browsing the store as a **Guest/User**.
- :white_check_mark: *view* **bag contents** whilst browsing the store as a **Guest/User**.
- :white_check_mark: *add* **products** as a **Store Owner/Admin**.
- :white_check_mark: *edit* **products** as a **Store Owner/Admin**.
- :white_check_mark: *delete* **products** as a **Store Owner/Admin**.
- :white_check_mark: be able to **log out**.


## Features
 
### Existing Features

**Register Account** 
- Anybody can register for free and create their own unique account. There is built-in authentication and authorization to check certain criteria is met before an account is validated. All passwords are hashed for security purposes!

**Log In to Account**
- Log in to existing account securely with Allauth (Django Integrated set of Applications) that addresses sewcure authentication, registration, email confirmation & account management.

**Manage Account**
- Existing users are able to manage details associated with that account such as adding/updating delivery information, account password and primary emails.

**Log Out of Account**
- Existing users can choose to log out if they are finished using the website. 

**View all Products**
- Both registered users & guests can view all existing products available on the site. 

**Search all Products**
- Both registered users & guests can search existing products available on site via search bar on desktop view & mobile.

**Filter Products**
- Both registered users & guests can filter existing products available on site by name, sizes, price, category, rating.

**Manage Products**
- Registered users can view account order history & all associated information such as date/price/item/qty/order number. They can also manage any items in their shopping bag.

**Add Products**
- [CRUD] Store Owners / Superusers can add new products to the website or update/delete current products. Certain defensive programming measures have been implemented such as only granting this permission to registered superusers/store owners.

**Admin**
- Django Admin application that allows superusers / store owners to manually create, update or delete any existing models or products from the store.

**About Us**
- Section designated to showcasing sponsored athletes & the team behind the Après Apparel brand.