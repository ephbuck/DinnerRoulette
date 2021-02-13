




### Security
##Signiture verification
This Application utilizes signiture verification. The attachted timestamp, the body of the request as well the the secret are hashed and comparied against the attatched signiture. there is also an time of request limitation preventing replay attacks.



# Build your image

Build your image by running `docker build -t python_flask_app dinner_roulette_app`.

# Run

You can run your docker image directly with `docker run -it -p 5000:5000 python_flask_app` 