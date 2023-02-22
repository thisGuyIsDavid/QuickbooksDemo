**A fatally insecure proof of concept of the Quickbooks Authentication process and some basic queries.**

This is so very insecure, and should never ever be used in any kind of production environment.
Written only to access the QB Sandbox API.

**Setup**

The easiest way to run this is within an IDE, such as PyCharm.
Install all pip packages.

Run the script in 'server.py'. This will start a Flask server that is needed for response handling during the auth process.

In the root directory, create a JSON file called `auth.json` with the following information from the QB developer dashboard:

`{
    "CLIENT_ID": <CLIENT ID>,
    "CLIENT_SECRET": <CLIENT SECRET>
}`

Make sure to add http://localhost:5001 to allowed URLs in the Quickbooks Dashboard (sandbox).

In a separate console, run the method `generate_url` to get an auth URL. Follow this to complete authentication. This will create a file called`intuit_auth.json' in your root directory with plain text credentials. **Once again, I must stress that this is dangerously insecure.**

With this done, you should be able to run the `demo.py` script successfully. This script demonstrates a few GET and POST requests.