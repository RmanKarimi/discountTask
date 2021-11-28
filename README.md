# Discount generator

# Environment

1. Django
2. SQLite
3. DjangoRestFramework
4. swagger Api documentation


### Features

1. Generate a discount code
   - send the **storeID**, **end_date** and the **number of discount code**
    it will generate X number of discount code for the given store
    
2. Fetch a discount code
   - send the **storeID** and it will return back the first available discount code for the store


# Getting Started

Following are instructions on setting up your development environment.

simply run the application and migrate the changes using 

   ```sh
   $ pip install -r requirements.txt
   $ python manage.py runserver
   $ python manage.py makemigrations
   $ python manage.py migrate
   $ python manage.py createsuperuser # not necessary
   ```

# APIs :

1. Post request to Generate X number of discount code
   

    (http://127.0.0.1:8000/create_discount/)
   
    Body:
         {
          "storeID": 1,
          "number": 2,
          "end_date": "2021-11-28"
          }


2. Get request to Fetch a discount code

   

    (http://127.0.0.1:8000/get_discount/?StoreID=1)


3. swagger Api documentation endpoint


    (http://127.0.0.1:8000/swagger/)

# Author

- [Arman Karimi](https://github.com/RmanKarimi)
- rman.karimi.1991@gmail.com