# **Flora & Fauna** <!-- omit in toc -->

![Flora & Fauna logo](media/docs/brand-logo.jpg)

## **Welcome to Flora & Fauna: Organic Skincare** <!-- omit in toc -->

Embued with the nourishment of nature, our mission at Flora & Fauna is to offer the finest organic ingredients across our entire range of products. Our collection of serums, creams, and elixirs transforms your skincare routine into a botanical sanctuary. Dive into our garden of products and discover the perfect blend of nature's best for your skin.

This project was created as part of the Code Institute Level 5 Diploma in Web Application Development course.

![Quest Board displayed on miltiple devices](media/docs/responsive-site.jpg)

[Click here to visit Flora & Fauna](https://flora-and-fauna-c279c1bad929.herokuapp.com/)

**By [Andrew Wright](https://github.com/AndyWright360)**

---

## **Contents** <!-- omit in toc --> 

- [**User Experience (UX)**](#user-experience-ux) 
  - [**Initial Concept**](#initial-concept) 
  - [**User Stories**](#user-stories) 
- [**Design**](#design) 
  - [**Colour Scheme**](#colour-scheme) 
    - [**Primary Palette**](#primary-palette) 
    - [**Additional Colours**](#additional-colours) 
  - [**Typography**](#typography) 
    - [**Dragon Hunter**](#dragon-hunter) 
    - [**Charm**](#charm) 
  - [**Imagery**](#imagery) 
  - [**Wireframes**](#wireframes) 
    - [**Home Page WF**](#home-page-wf) 
    - [**Products Page WF**](#products-page-wf) 
    - [**Product Detail Page WF**](#product-detail-page-wf) 
    - [**Add Product Page WF**](#add-product-page-wf) 
    - [**Edit Product Page WF**](#edit-product-page-wf) 
    - [**Bag Page WF**](#bag-page-wf) 
    - [**Checkout Page WF**](#checkout-page-wf) 
    - [**Checkout Success Page WF**](#checkout-success-page-wf)
    - [**Profile Page WF**](#profile-page-wf) 
    - [**Add Review Page WF**](#add-review-page-wf) 
    - [**Edit Review Page WF**](#edit-review-page-wf)
  - [**User Journey**](#user-journey) 
  - [**Database Schema**](#database-schema)
- [**Features**](#features) 
  - [**General Features**](#general-features)  
  - [**Future Implementations**](#future-implementations) 
- [**Technologies Used**](#technologies-used) 
  - [**Languages Used**](#languages-used) 
  - [**Frameworks, Libraries \& Programs Used**](#frameworks-libraries--programs-used) 
- [**Deployment \& Local Development**](#deployment--local-development) 
  - [**Deployment**](#deployment) 
  - [**Local Development**](#local-development) 
    - [**How to Fork**](#how-to-fork) 
    - [**How to Clone**](#how-to-clone) 
- [**Testing**](#testing) 
- [**Credits**](#credits) 
  - [**Code Used**](#code-used) 
  - [**Content**](#content) 
  - [**Media**](#media) 
  - [**Acknowledgments**](#acknowledgments)

---

## **User Experience (UX)**

### **Initial Concept**

From a visual perspective, the design of the website is intended to evoke the beauty of nature. A soft color palette of greens and blues was chosen to represent earthy and natural tones. The visual design is minimalist and clean, further emphasising the connection to nature. Each product range focuses on a key natural ingredient, prominently featured in the images. By incorporating nature-inspired visuals and a user-friendly interface, my intention is to make navigating the site feel like a walk through a botanical garden.

### **User Stories**

**As A Site User:**

1. I want to understand the purpose of the site immediately upon entering.
2. I want to be able to navigate the site easily and intuitively.
3. I want to use all features on the site on any device.
4. I want to receive feedback when interacting with the site to know if my actions have been successful.

**As A Shopper:**

1. I want to browse products easily, with options to filter and search to find what I need.
2. I want to find detailed information about products.
3. I want to see ratings and reviews of a product to know more about its quality and suitability for me.
4. I want to be able to add multiple products and quantities to my shopping bag.
5. I want to edit my shopping bag if I change my mind.
6. I want to know what I will be charged for delivery.
7. I want the option to purchase products without creating an account.

**As An Account Holder:**

1. I want my account to be secure and easy to set up.
2. I want to see my order history.
3. I want to update and save my personal information.
4. I want to leave reviews of products.
5. I want to edit and delete my reviews.
6. I want to add and remove products from my wishlist.

**As An Administrator:**

1. I want to add and edit products.
2. I want to remove products.
3. I want all admin controls to be simple to find and use.

---

## Deployment & Local Development

The application was deployed on [Heroku](https://www.heroku.com) using the steps below.

### PostgreSQL Database

This project uses a PostgreSQL Database hosted by Code Institute. As an alternative, you can create a free account on [ElephantSQL](https://www.elephantsql.com) using the following steps:

1. Sign up for ElephantSQL using your GitHub account.
2. Click **Create New Instance**.
3. Provide a name (usually the name of your project).
4. Select the **Tiny Turtle (Free)** plan.
5. Leave the **Tags** field blank.
6. Choose the **Region** and **Data Center** closest to you.
7. After creation, click on your new database name to view the database URL and Password.

### Amazon AWS

This project uses AWS for storing media and static files.

#### Create S3 Bucket:

1. **Log In:** Log into the AWS Management Console.
2. Search for **S3** and click to create a new bucket.
3. Name the bucket (preferably matching your Heroku app name) and select the closest region.
4. Uncheck **Block all public access** and acknowledge that the bucket will be public.
5. Enable **ACLs** from the **Object Ownership** section, and select **Bucket owner preferred**.
6. Go to the **Properties** tab, enable **Static website hosting**, enter `index.html` and `error.html` in their respective fields, and click **Save**.
7. Navigate to the **Permissions** tab and paste the following CORS configuration:

    ```json
    [
      {
        "AllowedHeaders": ["Authorization"],
        "AllowedMethods": ["GET"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
      }
    ]
    ```

8. Copy your ARN string from the **Bucket Policy** tab.
9. Click on **Policy Generator** and set:

    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": "s3:*",
          "Resource": [
            "arn:aws:s3:::your-bucket-name",
            "arn:aws:s3:::your-bucket-name/*"
          ]
        }
      ]
    }
    ```

10. Click **Add Statement** and **Generate Policy**.
11. Copy the entire policy, and paste it into the Bucket Policy Editor. Add `/*` to the end of the Resource key, and click **Save**.
12. In the **Access Control List (ACL)** section, click **Edit**, enable **List** for **Everyone (public access)**, and accept the warning box. If the **Edit** button is disabled, ensure ACLs are enabled in the **Object Ownership** section.

#### Set Up IAM:

1. Go to IAM (Identity and Access Management).
2. Click **Create New Group**, name it (e.g., `flora-and-fauna-group`), and proceed to the review policy page.
3. Select the group, go to the **Permissions** tab, and click **Add Permissions**.
4. Choose **Attach Policies**, find and select **AmazonS3FullAccess**, and click **Add Permissions**.
5. In the **JSON** tab, click **Import Managed Policy**, search for S3, select **AmazonS3FullAccess**, and **Import**.
6. Click **Review Policy**, name it (e.g., `flora-and-fauna-policy`), and provide a description:

    ```plaintext
    "Access to S3 Bucket for Flora & Fauna static files."
    ```

7. Click **Create Policy**.
8. Go to the **User Groups** section, select `flora-and-fauna-group`, click **Attach Policy**, search for your newly created policy, and attach it.
9. Click **Add User**, name it (e.g., `flora-and-fauna-user`), select **Programmatic Access**, add it to the `flora-and-fauna-group`, and click **Create User**.
10. Download the `.csv` file containing the Access key ID and Secret access key immediately.
  - **Note:** The `.csv` file contains:
    - `AWS_ACCESS_KEY_ID` = Access key ID
    - `AWS_SECRET_ACCESS_KEY` = Secret access key

### Final AWS Setup

1. Remove `DISABLE_COLLECTSTATIC` from Heroku Config Vars so that AWS handles static files.
2. Create a folder named `media` in S3.
3. Upload any existing media images, ensuring they are publicly readable.

### Stripe API

Stripe handles ecommerce payments.

1. From the Stripe dashboard, access **API Keys** from the **Developers** tab.
  - **Note:** The page contains:
    - `STRIPE_PUBLIC_KEY` = Publishable Key
    - `STRIPE_SECRET_KEY` = Secret Key
2. Select the **Webhooks** tab.
3. Click **Add Endpoint**, enter `https://your-heroku-domain/checkout/wh/`, and select **Receive all events**.
4. Click **Add Endpoint** to complete.
**Note:** The page contains:
  - `STRIPE_WH_SECRET` = Signing Secret Key

### Heroku Deployment

This web application is deployed using Heroku. Follow these steps to recreate the deployment process:

1. Create a requirements.txt file in the root directory, containing all necessary applications and dependencies.
2. Create a Procfile in the root directory, which informs Heroku about the files that run the app and how to run it.
**NB: Ensure the Procfile has a capital "P" and no file extension.**
3. Check for any blank lines at the end of the file and remove them if present.
4. Save both files, add, commit, and push them to your GitHub repository.
5. Log in to Heroku.
6. Click on the '**New**' button and select '**Create new app**'.
7. Enter a unique name for your app and select a region. Click '**Create app**'.
8. In the deployment section, select GitHub.
9. Connect the correct repository for the project.
10. Go to the '**Settings**' tab, click '**Reveal Config Vars**', and set the following variables:

    | KEY | VALUE |
    | :-- | :-- |
    | AWS_ACCESS_KEY_ID | Your Value |
    | AWS_SECRET_ACCESS_KEY | Your Value |
    | DATABASE_URL | Your Value |
    | DISABLE_COLLECTSTATIC | 1 (To be removed for final deployment) |
    | EMAIL_HOST_PASS | Your Value |
    | EMAIL_HOST_USER | Your Value |
    | SECRET_KEY  | Your Value |
    | STRIPE_PUBLIC_KEY | Your Value |
    | STRIPE_SECRET_KEY | Your Value |
    | STRIPE_WH_SECRET | Your Value |
    | USE_AWS | True |

11. Enable automatic deploys (this step is optional).
12. Within the Manual deploy section. Select the "main" branch from the list of branch options.
13. Click the "Manual Deploy" button.
14. Click "Open app" and the application should open in a new tab.

### **Local Development**

#### **How to Fork**

Forking the GitHub Repository allows for changes to be made without altering the original repository. To do this please follow the following steps:

1. Log in to GitHub.
2. Locate the relevant repository for this project [Flora & Fauna](https://github.com/AndyWright360/Flora-and-Fauna).
3. Select the '**Fork**' button located towards the top right of the repository.
4. You should now have a copy of the original repository in your GitHub account.

#### **How to Clone**

To clone this project, please follow the steps below:

1. Log in to GitHub.
2. Locate the relevant repository for this project [Flora & Fauna](https://github.com/AndyWright360/Flora-and-Fauna).
3. Click on the green '**Code**' drop-down button.
4. Select the '**Local**' tab in the window that appears.
5. Select the option '**HTTPS**' and copy the link shown.
6. Open the terminal in your IDE of choice.
7. Change the current working directory to the location you want to use for the cloned directory.
8. Type '**git clone**' into the terminal and then paste the link you copied in Step 5.

    ```bash
    git clone (relevant link)
    ```

9. Press enter.
10. Set up a virtual environment.
**NB: If you're using the Code Institute Template in GitPod, you can proceed directly to the next step as the virtual environment is pre-configured for you.**
11. Install the required packages listed in the requirements.txt file by executing the following command in the Terminal.

    ```bash
    pip3 install -r requirements.txt
    ```

12. Create an `env.py` file in the root directory.

    ```python
    import os

    os.environ.setdefault("AWS_ACCESS_KEY_ID", "your_value")
    os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "your_value")
    os.environ.setdefault("DATABASE_URL", "your_value")
    os.environ.setdefault("EMAIL_HOST_PASS", "your_value")
    os.environ.setdefault("EMAIL_HOST_USER", "your_value")
    os.environ.setdefault("SECRET_KEY", "your_value")
    os.environ.setdefault("STRIPE_PUBLIC_KEY", "your_value")
    os.environ.setdefault("STRIPE_SECRET_KEY", "your_value")
    os.environ.setdefault("STRIPE_WH_SECRET", "your_value")

    # Local environment only
    os.environ.setdefault("DEBUG", "True")
    ```

13. Make and apply migrations.

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

14. Create a superuser.

    ```bash
    python3 manage.py createsuperuser
    ```

15. Load fixtures (if needed).

    ```bash
    python3 manage.py loaddata file-name.json
    ```

16. Run the server.

    ```bash
    python3 manage.py runserver
    ```

---