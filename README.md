# Backend-Assessment
mPharma Backend Assessment

RESTful API that can allow people to utilize an internationally recognized set of diagnosis codes


# Technologies Used
Python, Django, DRF, PostgreSQL.

# Running the app
 `git clone git@github.com:Ndichu-shee/Backend-Assessment.git`
 
 ## Run Server
 `sudo docker-compose build`
 `sudo docker-compose up`
 ### Run the migrations 
 `sudo docker-compose exec web python manage.py makemigrations`
 
 `sudo docker-compose exec web python manage.py migrate`
 ### Create a super user
`sudo docker-compose exec web python manage.py createsuperuser`
 
 # Running the Tests

   `sudo docker-compose exec web python manage.py test`
   
 ## Accessing different endpoints
 
 #### register a user
 `http://0.0.0.0:8000/create_user/` 
 
 #### login user
  `http://0.0.0.0:8000/login_user/`
  
 #### upload a csv
  `http://0.0.0.0:8000/diagnosis-codes-upload/`
  
 #### View all the diagnosis codes
  `http://0.0.0.0:8000/diagnosis-codes/`
  
  #### view, edit and deleting by id 
  `http://0.0.0.0:8000/diagnosis-codes/{id}`
 


