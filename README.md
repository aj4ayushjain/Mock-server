# Mock-server
A Json Editor for all sort of operations on json

Build a REST based JSON mock server to easily add, update, delete and access data from a JSON file.
    
    -Every data set should have a parent identifier (entity type), which will be used in the GET APIs.

    -Every data set should have an ID (Primary key)

    -ID should be immutable, error needs to be thrown if ID is tried to be mutated.

    -If you make POST, PUT, PATCH or DELETE requests, changes have to be automatically saved to store.json.

    -The store.json file should support multiple entity types.
    


Enable filtering at entity level :

    GET /posts?title=title1&author=CIQ

Enable sorting at entity level :

    GET /posts?_sort=views&_order=asc

Enable basic search at entity level:

    GET /posts?q=IQ


## Packages/Frameworks
1. Json - Python inbuilt package to deal with json
2. Flask - Microwebframework

## Overview 

The main code is present at ```mockserver.py```. The ```utils.py``` file contains major function to handle json related utilities.

## Build the app 
```
$ cd Mock-server
$ flask run
```
And then access the app at ```http://localhost:5000/```

## REST DEV/TEST CURL

1. GET (General parent identifier(entity ))

```curl -X GET -i 'http://ayushj.pythonanywhere.com/posts'```

2.  GET (General parent identifier with id)

```curl -X GET -i 'http://ayushj.pythonanywhere.com/posts/0'```

3. GET(filtering at entity level)

```curl -X GET -i 'http://ayushj.pythonanywhere.com/posts?title=title3&author=CommerceIQ'```

4. GET(sorting at entity level)

```curl -X GET -i 'http://ayushj.pythonanywhere.com/posts?_sort=id&_order=asc'```

5.  POST

```curl -X POST -H 'Content-Type: application/json' -i 'http://ayushj.pythonanywhere.com/posts' --data '{"id": 3, "title": "title6", "author": "CommerceI", "views": 132, "reviews": 9}'```

6.  PUT OR PATCH

```curl -X PUT -H 'Content-Type: application/json' -i 'http://ayushj.pythonanywhere.com/posts/3' --data '{"author": "Commerce"}'```

7.  DELETE

```curl -X DELETE -i 'http://ayushj.pythonanywhere.com/posts/3'```

## Current Implementation Approach and other strategies

1. In the current implementation the json is loaded in-memory and operations are performed which allows a lot of dynamism in entity types/over the json.
Assuming not fixed entity types this approach seems suitable
2. Otherwise if the json file being loaded is pretty large than memory then we need to have class representing json entity and then we could play around, or do different techniques(ljson, database techniques) to work our way out. 

