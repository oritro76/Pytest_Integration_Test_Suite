## BUG: GET request for all the APIs with json body returns Internal Server error


### Effected API Paths: 
    - /state
    - /devices

### Headers
```
{"Content-Type": "application/json"}
```
### json request
```
{"ip":  "192.168.100.10"}
```
### response:
```
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>

<head>
    <title>Error: 500 Internal Server Error</title>
    <style type="text/css">
        html {
            background-color: #eee;
            font-family: sans;
        }

        body {
            background-color: #fff;
            border: 1px solid #ddd;
            padding: 15px;
            margin: 15px;
        }

        pre {
            background-color: #eee;
            border: 1px solid #ddd;
            padding: 5px;
        }
    </style>
</head>

<body>
    <h1>Error: 500 Internal Server Error</h1>
    <p>Sorry, the requested URL <tt>&#039;http://localhost:8081/state?hola=1212&#039;</tt>
        caused an error:</p>
    <pre>Internal Server Error</pre>
    <h2>Exception:</h2>
    <pre>TypeError(&quot;get_device_state() got an unexpected keyword argument &#039;ip&#039;&quot;)</pre>
    <h2>Traceback:</h2>
    <pre>Traceback (most recent call last):
  File &quot;./app/app.py&quot;, line 868, in _handle
    return route.call(**args)
  File &quot;./app/app.py&quot;, line 1748, in wrapper
    rv = callback(*a, **ka)
  File &quot;./app/app.py&quot;, line 3790, in wrapper
    result = func(**params)
TypeError: get_device_state() got an unexpected keyword argument &#039;ip&#039;
</pre>
</body>
```

## BUG: Set Brightness API returns Internal Server error for certain inputs for both content-type

### Values: 
    - Empty string "",
    - Random string,
    - null

### response:
```
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>

<head>
    <title>Error: 500 Internal Server Error</title>
    <style type="text/css">
        html {
            background-color: #eee;
            font-family: sans;
        }

        body {
            background-color: #fff;
            border: 1px solid #ddd;
            padding: 15px;
            margin: 15px;
        }

        pre {
            background-color: #eee;
            border: 1px solid #ddd;
            padding: 5px;
        }
    </style>
</head>

<body>
    <h1>Error: 500 Internal Server Error</h1>
    <p>Sorry, the requested URL <tt>&#039;http://localhost:8081/brightness&#039;</tt>
        caused an error:</p>
    <pre>Internal Server Error</pre>
    <h2>Exception:</h2>
    <pre>TypeError(&quot;float() argument must be a string or a number, not &#039;NoneType&#039;&quot;)</pre>
    <h2>Traceback:</h2>
    <pre>Traceback (most recent call last):
  File &quot;./app/app.py&quot;, line 868, in _handle
    return route.call(**args)
  File &quot;./app/app.py&quot;, line 1748, in wrapper
    rv = callback(*a, **ka)
  File &quot;./app/app.py&quot;, line 3790, in wrapper
    result = func(**params)
  File &quot;./app/app.py&quot;, line 3849, in set_device_brightness
    brightness = float(brightness)
TypeError: float() argument must be a string or a number, not &#039;NoneType&#039;
</pre>
</body>

</html>
```


## BUG: Set Color API returns Internal Server error for certain inputs


### Values: 
    - Random number/json and form
    - null/json

### response:
```
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
    <html>
        <head>
            <title>Error: 500 Internal Server Error</title>
            <style type="text/css">
              html {background-color: #eee; font-family: sans;}
              body {background-color: #fff; border: 1px solid #ddd;
                    padding: 15px; margin: 15px;}
              pre {background-color: #eee; border: 1px solid #ddd; padding: 5px;}
            </style>
        </head>
        <body>
            <h1>Error: 500 Internal Server Error</h1>
            <p>Sorry, the requested URL <tt>&#039;http://localhost:8081/color&#039;</tt>
               caused an error:</p>
            <pre>Internal Server Error</pre>
              <h2>Exception:</h2>
              <pre>AttributeError(&quot;&#039;NoneType&#039; object has no attribute &#039;lstrip&#039;&quot;)</pre>
              <h2>Traceback:</h2>
              <pre>Traceback (most recent call last):
  File &quot;./app/app.py&quot;, line 868, in _handle
    return route.call(**args)
  File &quot;./app/app.py&quot;, line 1748, in wrapper
    rv = callback(*a, **ka)
  File &quot;./app/app.py&quot;, line 3790, in wrapper
    result = func(**params)
  File &quot;./app/app.py&quot;, line 3861, in set_device_color
    hex_to_rgb(color)
  File &quot;./app/app.py&quot;, line 3799, in hex_to_rgb
    hex = hex.lstrip(&#039;#&#039;)
AttributeError: &#039;NoneType&#039; object has no attribute &#039;lstrip&#039;
</pre>
        </body>
    </html>
```

## BUG: Chilltime automation is not working properly when brightness level is more or less than 30%

### Steps when brightness level is above 30%:
- Connect to a light
- Set brightness to any value more than 30%
- Execute chilltime until the brightness reaches 30%
- Check brightness level

### Observation:
    Brightness is always more then 30% but less than 40%
### Expected:
    Brightness should be 3.0

### Steps when brightness level is below 30%:
- Connect to a light
- Set brightness to any value below 30%
- Execute chilltime
- Check brightness level

### Observation:
    Brightness has been increased.
### Expected:
    Brightness should not change