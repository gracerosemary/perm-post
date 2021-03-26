# Back End Deployment

PR Link: https://github.com/gracerosemary/perm-post/pull/3  
**Author**: G Choi   
**Version**: 3.0.0   

## Overview
Create a DRF powered API and adjust project's permissions for authenticated access only. Add custom permissions to update/delete and add ability for user's to switch from API. Add JWT Authentication. Make sure data persists. Modify application to store db information in .env file.   

## Architecture
Django, Docker, Postgres, Poetry, Whitenoise, djangorestframework-simplejwt, HTTPie, Gunicorn, Django-Cors-header     

## API
Project - Password Tracker: enter username, password, and website   

## Testing HTTPie
HTTPie - Is it working?

1. `http post localhost:8000/api/token/ username=admin password=admin`
2. copy access token
3. `http :8000/api/v1/tracker/ 'Authorization Bearer (paste token)’`
4. `http GET localhost:8000/api/v1/tracker/`

Good Endpoint example:
- HTTP status: 200 OK -> status is good
- Content-Length: 84 -> we know it has content
- Content-Type: application/json -> content is in JSON format
```
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Connection: close
Content-Length: 84
Content-T
Date: Fri, 26 Mar 2021 23:33:47 GMT
Referrer-Policy: same-origin
Server: gunicorn/20.0.4
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
[
    {
        "id": 1,
        "updated_at": "2021-03-25T02:13:38.957221Z",
        "user": 1,
        "website": "grace.com"
    }
]
```

Bad Endpoint example:
- HTTP status: 404 Not Found -> not found!
- “detail”: Not found.
```
HTTP/1.1 404 Not Found
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Connection: close
Content-Length: 23
Content-Type: application/json
Date: Fri, 26 Mar 2021 23:39:14 GMT
Referrer-Policy: same-origin
Server: gunicorn/20.0.4
Vary: Accept, Origin
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "detail": "Not found."
}
```

## Change Log
03-20-2021 3:53pm - Completed lab and testing  
03-24-2021 9:00pm - Completed second lab
03-26-2021 4:45pm - Completed third lab 