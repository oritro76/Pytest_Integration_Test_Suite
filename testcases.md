1. List All Available Devices: GET /devices
Positive Scenarios:

Verify the endpoint returns a list of devices with their names and IP addresses.
Verify the response status code is 200.

2. Connect to a Device: POST /connect
Positive Scenarios:

Connect to a valid device using a correct IP address with application/json.
Connect to a valid device using a correct IP address with application/x-www-form-urlencoded.
Verify the response status code is 200.
Verify the response contains "success": true.
Negative Scenarios:

Attempt to connect using an invalid IP address with application/json.
Attempt to connect using an invalid IP address with application/x-www-form-urlencoded.
Attempt to connect to a device that is already connected.
Verify the response status code is 200 but the response contains "success": false.
3. Get the State of a Device: GET /state
Positive Scenarios:

Retrieve the state of a connected device.
Verify the response status code is 200.
Verify the response contains the device's name, IP, color, and brightness.
Negative Scenarios:

Attempt to retrieve the state without connecting to any device.
Verify the response status code is 200 but the response contains "success": false.
4. Set the Brightness of a Device: POST /brightness
Positive Scenarios:

Set the brightness of a connected device to a valid value (e.g., 5) with application/json.
Set the brightness of a connected device to a valid value (e.g., 5) with application/x-www-form-urlencoded.
Verify the response status code is 200.
Verify the response contains "success": true.
Negative Scenarios:

Attempt to set brightness without connecting to any device.
Attempt to set brightness to an invalid value (e.g., -1, 15) with application/json.
Attempt to set brightness to an invalid value (e.g., -1, 15) with application/x-www-form-urlencoded.
Verify the response status code is 200 but the response contains "success": false.
5. Set the Color of a Device: POST /color
Positive Scenarios:

Set the color of a connected device to a valid hex code (e.g., #00ff00) with application/json.
Set the color of a connected device to a valid hex code (e.g., #00ff00) with application/x-www-form-urlencoded.
Verify the response status code is 200.
Verify the response contains "success": true.
Negative Scenarios:

Attempt to set color without connecting to any device.
Attempt to set color to an invalid hex code (e.g., #gggggg) with application/json.
Attempt to set color to an invalid hex code (e.g., #gggggg) with application/x-www-form-urlencoded.
Verify the response status code is 200 but the response contains "success": false.
6. Set the Name of a Device: POST /name
Positive Scenarios:

Set the name of a connected device to a valid name (e.g., "New Bulb Name") with application/json.
Set the name of a connected device to a valid name (e.g., "New Bulb Name") with application/x-www-form-urlencoded.
Verify the response status code is 200.
Verify the response contains "success": true.
Negative Scenarios:

Attempt to set name without connecting to any device.
Attempt to set name to an empty string or None with application/json.
Attempt to set name to an empty string or None with application/x-www-form-urlencoded.
Verify the response status code is 200 but the response contains "success": false.

7. Drop the Brightness Automatically (Automation Task): POST /chilltime
Positive Scenarios:

Execute the automation task on a connected device.
Verify the response status code is 200.
Verify the response contains "success": true.
Ensure brightness drops to 30% or stops if already at 30%.
Negative Scenarios:

Attempt to execute the automation task without connecting to any device.
Verify the response status code is 200 but the response contains "success": false.
8. Disconnect from Any Device: POST /disconnect
Positive Scenarios:

Disconnect from a connected device.
Verify the response status code is 200.
Verify the response contains "success": true.
Negative Scenarios:

(Not applicable as disconnecting is typically a straightforward operation unless related to server issues.)