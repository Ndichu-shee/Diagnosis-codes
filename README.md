# Backend-Assessment
mPharma Backend Assessment

RESTful API that can allow people to utilize an internationally recognized set of diagnosis codes


# Technologies Used
Python, Django, DRF, PostgreSQL.

# Running the app
 `git clone git@github.com:Ndichu-shee/Backend-Assessment.git`
 
 `cd Backend-Assessment`
 
 ## Run Server
 `docker-compose build`
 
 `docker-compose up`
 ### Run the migrations 
 `docker-compose exec web python manage.py makemigrations`
 
 `docker-compose exec web python manage.py migrate`
 ### Create a super user
`docker-compose exec web python manage.py createsuperuser`

 
 # Running the Tests

   `docker-compose exec web python manage.py test`
   
 ## Accessing different endpoints
 
 #### log in as an admin
 `http://0.0.0.0:8000/admin/`
 
 #### register a user
 `http://0.0.0.0:8000/create_user/` 
  
 #### upload a csv
  `http://0.0.0.0:8000/diagnosis-codes-upload/`
  
 #### View all the diagnosis codes
  `http://0.0.0.0:8000/diagnosis-codes/`
  
  #### view, edit and deleting by id 
  `http://0.0.0.0:8000/diagnosis-codes/{id}`
 


