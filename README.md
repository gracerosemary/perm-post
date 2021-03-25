# Permissions and Postgrestql

PR Link: https://github.com/gracerosemary/perm-post/compare/perm?expand=1  
**Author**: G Choi   
**Version**: 2.0.0   

## Overview
Create a DRF powered API and adjust project's permissions for authenticated access only. Add custom permissions to update/delete and add ability for user's to switch from API.  

## Getting Started
Create dockerfiles and update permissions. Add JWT Authentication. Make sure data persists.  

## Architecture
Django, Docker, Postgres, Poetry, Whitenoise, djangorestframework-simplejwt, HTTPie, Gunicorn   

## API
Project - Password Tracker: enter username, password, and website   

## Testing HTTPie
HTTPie - Is it working?

Command:  
`http post localhost:8000/api/token/ username=admin password=admin`

If there is a connection error, this will display:  
"http: error: ConnectionError: HTTPConnectionPool(host='localhost', port=8000): Max retries exceeded with url: /api/token/ (Caused by NewConnectionError(': Failed to establish a new connection: [Errno 61] Connection refused')) while doing a POST request to URL: http://localhost:8000/api/token/“  

If your token has expired, this will display:  
```
HTTP/1.1 401 Unauthorized  
Allow: GET, POST, HEAD, OPTIONS  
Connection: close  
Content-Length: 176 
Content-Type: application/json  
Date: Thu, 25 Mar 2021 03:10:19 GMT  
Referrer-Policy: same-origin  
Server: gunicorn/20.0.4  
Vary: Accept  
WWW-Authenticate: Bearer realm="api"  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY  
```
```
{
    "code": "token_not_valid",
    "detail": "Given token not valid for any token type",
    "messages": [
        {
            "message": "Token has wrong type",
            "token_class": "AccessToken",
            "token_type": "access"
        }
    ]
}
```

If it is working as expected, this will display:
```
HTTP/1.1 200 OK  
Allow: POST, OPTIONS  
Connection: close  
Content-Length: 438  
Content-Type: application/json  
Date: Thu, 25 Mar 2021 03:58:07 GMT  
Referrer-Policy: same-origin  
Server: gunicorn/20.0.4  
Vary: Accept  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY  
```

## Change Log
03-20-2021 3:53pm - Completed lab and testing  
03-24-2021 9:00pm - Completed second lab