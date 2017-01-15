# UCSD Degree Audit 2.0

Scraps UCSD's Degree Audit and parses information to JSON using Selenium, PhantomJS, BeautifulSoup, and Python. Plans to incorporate CAPE data.

## TODO
1. Integrate API with Frontend
    - ~~Decouple Auth complements into Main, Auth, Fetch, etc and have a router~~
    - Card View to show all of the courses
    - More intuitive menu
    - Handle tokens better
2. Implement OAuth2 authentication for API
3. Write wrapper module for API and add to NPM
3. Integrate CAPE data to front end, so users can see how well they do on average compared to class average

## Running Application
### API
1. gunicorn app 

### Web
1. cd web
2. npm start

## API Usage
1. Obtain API Token through GET request at /auth/**{PID}**/**{PASSWORD}**
2. Obtain courses through GET /courses/**{TOKEN}**// or GET /courses/**{TOKEN}**/quarter/

**{PID}** = *UCSD PID i.e. A12345678* 

**{PASSWORD}** = *UCSD Password for TritonLink etc.* 

**{TOKEN}** = *Token received from Step 1* 


*For example*: 

curl http://localhost:8000/auth/A123456789/hunter2

```
HTTP/1.1 200 OK
Connection: close
Date: Fri, 13 Jan 2017 19:04:44 GMT
Server: gunicorn/19.6.0
content-length: 48
content-type: application/json; charset=UTF-8

{"Auth Token": 12345678912345678912345678912345}
```

curl http://localhost:8000/courses/12345678912345678912345678912345//

```
HTTP/1.1 200 OK
Connection: close
Date: Fri, 13 Jan 2017 19:06:59 GMT
Server: gunicorn/19.6.0
content-length: 3268
content-type: application/json; charset=UTF-8

{
    "GPA": "4.000", 
    "courses": [
        {
            "course": "CSE 100", 
            "grade": "A+", 
            "quarter": "WI17", 
            "units": "4.0"
        }, 
        ....
}
```

