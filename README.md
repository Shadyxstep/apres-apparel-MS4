# <a href="https://apres-apparel.herokuapp.com/">Après Apparel</a>

![responsive_screenshot](media/readme-imgs/amiresponsive-apres.JPG)

This [project](https://apres-apparel.herokuapp.com/) is my fourth milestone project (Full Stack Frameworks with Django) in Full Stack Software Development course run by [Code Institute](https://codeinstitute.net/)

Après Apparel is an outdoor lifestyle brand founded by my friend, Stephen Rice, with the main aim of manifesting a positive brand image & culture amongst those who lead active lifestyles whilst also supplying apparel & accessories to suit 
those lifestyles.
The approach of this business relies heavily on creating community & a culture around the brand and team members, rather than being detached and strictly ecommerce for products.
The Après Apparel vision is to build a strong following around the brand & its values on social media & to hopefully use that platform to give back and support that community.

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Icons**](#icons)
        - [**Typography**](#typography)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Version Control & Project Management**](#version-control)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)
    - [**Tools**](#tools)
    - [**Resources**](#resources)

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

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development Diploma Course, specifically the **Full Stack Frameworks** module.
The objective for this project is to "Create a web application that allows users to browse & purchase products, register/login/logout & provide delivery information securely, display team members behind the brand & real athletes we wish to support in future." 

This e-commerce site is made for those who love adventuring, sports and the outdoors!
We also have a section dedicated to athletes we support & follow, and the team members behind the Après Apparel brand, with social media links provided
for any curious visitors to site to check out.

"**_As a anonymous user, I would like to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark: *view the site* from **any device** *(mobile, tablet, desktop)*.
- :white_check_mark: *view all products* as a **Guest** and **Registered User**.
- :white_check_mark: *view individual product details* as a **Guest** and **Registered User**.
- :white_check_mark: *add products to my shopping bag* as a **Guest** and **Registered User**.
- :white_check_mark: *remove products from my shopping bag* as a **Guest** and **Registered User**.
- :white_check_mark: *manage products in my shopping bag* as a **Guest** and **Registered User**.
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

**General**  
- :white_check_mark: *view the site* from **any device** *(mobile, tablet, desktop)*.
- :white_check_mark: *I want to immediately understand the purpose of the site*
- :white_check_mark: *I want to be able to easily navigate through the site*
- :white_check_mark: *I want a site that is visually simplistic*
- :white_check_mark: *I want to know where I am on the site at any time*
- :white_check_mark: *I want to be informed of actions I make and whether they are successful or not*

**Products**   
- :white_check_mark: *I want to see a list of available products*
- :white_check_mark: *I want products to be sorted into relevant categories*
- :white_check_mark: *I want to be able to search the site for a specific product*
- :white_check_mark: *I want to be able to view the individual product details*
- :white_check_mark: *I want to be able to select the size of a product*
- :white_check_mark: *I want to be able to adjust the quantity of a product*

**Athletes**   
- :white_check_mark: *I want to see a list of sponsored athletes*
- :white_check_mark: *I want to be able to see what sport the athlete plays*
- :white_check_mark: *I want to be able to view the individual athlete details*
- :white_check_mark: *I want to be able to connect with an specific athlete via social media*

**Team** 
- :white_check_mark: *I want to be able to see who is behind the brand*
- :white_check_mark: *I want to be able to see which roles each team member has in relation to the brand*
- :white_check_mark: *I want to be able to connect with an specific team member via social media*

**Shopping Bag**  
- :white_check_mark: *I want to easily view my shopping bag*
- :white_check_mark: *I want to easily view my bag total*
- :white_check_mark: *I want to easily view my bag total from anywhere on the site*
- :white_check_mark: *I want to be able to remove items from my shopping bag*
- :white_check_mark: *I want to be able to adjust the quantity of items in my shopping bag*
- :white_check_mark: *I want to see any changes I make to my bag reflected in the bag totals*
- :white_check_mark: *I want to view the details of what is in my bag*

**Checkout**  
- :white_check_mark: *I want to be able to checkout securely*
- :white_check_mark: *I want to receive a confirmation of my order on site*
- :white_check_mark: *I want the confirmation of my order to include the details of my order*

**Account**   
- :white_check_mark: *I want to be able to create an account*

#### **As a Registered User:** 
- :white_check_mark: *I want to be able to log in and out easily*
- :white_check_mark: *I want to be able to reset my password*
- :white_check_mark: *I want to receive confirmation that I have registered for the site*
- :white_check_mark: *I want to have a personal profile*
- :white_check_mark: *I want to be able to view my order history*
- :white_check_mark: *I want to be able to save my default delivery details*
- :white_check_mark: *I want to be able to easily update my delivery information*

#### **As a Superuser or Store Owner:**
- :white_check_mark: *I want to be able to access the admin panel*
- :white_check_mark: *I want to be able to add/edit/delete categories*
- :white_check_mark: *I want to ba able to add/edit/delete subcategories*
- :white_check_mark: *I want to be able to add new products*
- :white_check_mark: *I want to be able to add new athletes*
- :white_check_mark: *I want to be able to edit/delete existing products*
- :white_check_mark: *I want to be able to edit/delete existing athletes*
- :white_check_mark: *I want to be able to view/manage users of the site*
- :white_check_mark: *I want to be able to view/manage orders*


### Design 

- The design of the Après Apparel website is a monochromatic Black/White/Grey color scheme to fit in line with a simple high contrast aesthetic, with various star/sunset background images used across the site to 
symbolize the outdoor lifestyle the brand wishes to promote.
- I personally prefer to create my websites with a light/dark theme and avoid brighter colours as I feel it can impede on readability for the user.
- I wanted the website to have a simplistic high contrast colour scheme
- I wanted the website to be intuitive and easy to navigate.
- I wanted to achieve a clean, uncluttered aesthetic.
- I wanted the website to be accessible on all devices (desktop, mobile, tablet).

#### Frameworks

- [Bootstrap 4.6.0](https://getbootstrap.com/)
    - My preferred CSS framework for this project because of the simple-to-understand documentation & simplicity of use.
- [jQuery 3.6.0](https://code.jquery.com/jquery/)
    - In an effort to keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.
- [Django 3.1.0](https://www.djangoproject.com/download/)
    - Django is a free and open-source web framework that I've used to render the back-end Python with the front-end Bootstrap4 CSS3 Framework and AnimateCSS Library. 

#### Color Scheme

- As I favour simplicity & high contrast over popping colours when designing website, the color scheme used for this website is a simple Black/White/Grey monochromatic theme.

- ![#fff](https://via.placeholder.com/15/fff/000000?text=+) `#fff`
- ![#696969](https://via.placeholder.com/15/696969/000000?text=+) `#696969`
- ![#000](https://via.placeholder.com/15/000/000000?text=+) `#000`

My main reason for a basic white/grey/black monochromatic color scheme is that it provides high contrast between text & background elements which makes readability easier for visitors who visit the site.
I've been inspired in the past by tech giant Apple's UX, where they favour simplicity & grayscale monochromatic color schemes.
This particular color scheme also fits in with the simple aesthetic the brand owner of Après Apparel is trying to achieve.

White is the predominant theme of the website with black being reserved for button outlines & texts for extra readability.
The white background also helps the product images pop out visually for the site visitors as they are mostly bright & colourful.

#### Icons

- [Font Awesome 5.15.3](https://fontawesome.com/)
    - Font Awesome was my preferred source for icon use across the site rather than Materialize Icons. Font Awesome Icons are simplistic & easily customizable and displayed through *classes* rather than *text*
    which fits the aesthetic Après Apparel is targetting.

#### Typography

- [Google Fonts](https://fonts.google.com/) were used across the site:
- [Montserrat](https://fonts.google.com/specimen/Montserrat#standard-styles) : default font.
- [AnimateCSS](https://animate.style/) : Animations used for landing, team & athlete page.
- [Bootstrap](https://getbootstrap.com/) : Typography / Colors Documentation from Bootstrap was used in various headings/texts/alerts around the site such as ".display-x" & ".text-success" classes.


#### Features
 
### Existing Features
- The site contains 7 separate custom apps. Each app has its own features & unique content.
    - Home
    - Products
    - Bag
    - Checkout
    - Athletes
    - Team
    - Profile 

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
- [CRUD] Store Owners / Superusers can add new products to the website or update/delete current products or athletes. Certain defensive programming measures have been implemented such as granting adding/editing/deleting permissions to registered superusers/store owners only.

**Admin**
- Django Admin application that allows superusers / store owners to manually create, update or delete any existing models or products from the store.

**About Us**
- Section designated to showcasing sponsored athletes & the team behind the Après Apparel brand and their respective social media links.

**Toast Messages**
- Site wide feature that gives users feedback on if the action they took was successful/unsuccessful with correlating colors.
- There are 4 types of toast messages:
        - Success (Green)
        - Info  (Blue)
        - Warning (Yellow)
        - Error (Red)

**Automated Emails**
    - Automated emails are sent to the user when certain actions are performed.
        - Account verification email when a user registers for an account.
        - Password reset email.
        - Order confirmation email when a user completes an order.

### Features Left To Implement

**Additional Products & Categories**
- Add more products & categories added to the website. 
- More products specific to surfing, hiking, mountain climbing, skiing.

#### Technologies Used

### Version Control & Project Management

- [Git](https://git-scm.com/) - Primary version control for pushing code to my online repository.

- [GitPod](https://www.gitpod.io/) - Used as my primary IDE for developing projects.

- [GitHub](https://github.com/) - Used as remote storage of my projects online.


### Front-End Technologies


- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.

- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.

- [jQuery 3.4.1](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.

- [Bootstrap 4.6.0](https://getbootstrap.com/) - Used as the front-end framework for layout and design.

- [Stripe API](https://stripe.com/docs/api?lang=python) - Used to make secured payments.

- [Amazon AWS S3](https://aws.amazon.com/) - Used to store *staticfiles* and *media* folders and files.

### Back-End Technologies


- [Python 3.6.7](https://www.python.org/) - Used as the back-end programming language.

- [Django 2.2.16](https://docs.djangoproject.com/en/2.2/) - Used as my Python web framework.

- [Heroku](https://www.heroku.com) - Used for *"Platform as a Service"* (PaaS) for app hosting.

- [PostgreSQL 9.6](https://www.postgresql.org/) - Used as relational SQL database plugin via Heroku.

### Tools 

- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Allowed me to use browser as an editor for experimental style changes.

- [Am I Responsive](http://ami.responsivedesign.is/) - Check responsiveness of website.

### Resources
- [Django Docs](https://docs.djangoproject.com/en/3.2/)
- [cdnjs](https://cdnjs.com/)
- [w3schools](https://www.w3schools.com/) 
- [Stack Overflow](https://stackoverflow.com/)
- Boutique Ado Project - [Code Institute](https://codeinstitute.net/) Full Stack Frameworks Module
    
The environment dependencies/ requirements for this project are shown below :

![responsive_screenshot](media/readme-imgs/requirementstxt-apresapparel.JPG)

#### Testing

A thorough mix of automated and manual testing have gone into building this project. 
In addition to tests, I have used online code validation sites for the code in this project. 
I have also checked compatibility of the site across various modern browsers and devices.

**HTML**
- [W3C HTML Validator](https://validator.w3.org)
    

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    - The W3C Jigsaw validator shows Bootstrap4 2 errors coming from URI: "https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" The errors are:
        - abbr[data-original-title], abbr[title] -> "Property text-decoration-skip-ink doesn't exist : none"
        - .accordion -> "Property overflow-anchor doesn't exist : none"
        
    - The W3C Jigsaw validator does not yet recognize elements imported in from the AnimateCSS library used in this project, and therefore passes 34 **Parse Errors**. The elements from AnimateCSS in my landing page headings are not recognized by the CSS Validator. The Parse Errors I've received are:
        -![css_validation](media/readme-imgs/css-validation-errors-AnimateCSS.JPG)

    - I also received these **Warnings** which are all coming from the validator not recognizing vendor extensions from Bootstrap4 and AnimateCSS:

        - Some of the warnings from AnimateCSS extensions
        - `--animate-duration` is an unknown vendor extension
        - `--animate-delay` is an unknown vendor extension.
        - `--animate-repeat` is an unknown  vendor extension.
        - `-webkit-animation-duration` is an unknown vendor extension.
        - `-webkit-animation-fill-mode` is an unknown vendor extension.

        - Some of the warnings from the Bootstrap4 extensions
        - `--blue` is an unknown vendor extension
        - `--indigo` is an unknown vendor extension
        - `--purple` is an unknown vendor extension
        - `--pink` is an unknown vendor extension
        - `--red` is an unknown vendor extension