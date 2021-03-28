'''
Author: Ken
git : https://github.com/PlayingNumbers/ds_salary_proj
Tutorial(youtube) : https://www.youtube.com/watch?v=QWgg4w1SpJ8&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t&index=6

Inspired by (Tutorial) : https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

Disclaimer: I don't own the copyrights of the code , It was written and coded as
            followed on the youtube channel as mentioned above, I have add extra comments for 
            my reference to make code understandable.please take a note that I have changed the names of the column and files according to my need
                   , if you are copy pasting this code you have to look for syntax errors in names of files and
                   data-columns that are used in tutorial.
                   
            P.S: I have used following tools to run the server/client request
            
             # following command to install "gunicorn" from command-line
             pip install flask gunicorn sklearn
            
             ## following command to run/link (i am not sure:just follow the tutorial) for working request
                type into command-line and press enter
             touch app.py
             touch Procfile
             touch wsgi.py
             
             ### following command to run the wsgi file from (this file) from command-line
             gunicorn --bind 0.0.0.0:8080 wsgi:application -w 1
             
             #### following command to run from command line in order to get the response from request
                  note the i.p. address are same for 'curl' and 'gunicorn' commands
             curl -X GET http://0.0.0.0:8080/predict

'''
from app import app as application
if __name__ == "__main__":
    application.run()