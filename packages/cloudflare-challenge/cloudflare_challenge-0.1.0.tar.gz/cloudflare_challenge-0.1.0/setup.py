# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cloudflare_challenge']

package_data = \
{'': ['*'], 'cloudflare_challenge': ['templates/*']}

install_requires = \
['flask>=2.0,<3.0']

setup_kwargs = {
    'name': 'cloudflare-challenge',
    'version': '0.1.0',
    'description': 'CloudFlare Challenge pages',
    'long_description': '# CloudFlare-Challenge\n\nEnsure that we can do a cloudflare challenge in flask\n\n## Rationale\n\nIf you Flask server is behind a CloudFlare wall then any upload of data may provoke\na "challenge" of the "I\'m not a robot" kind.\n\nInstead of returning the response to your browser query, CloudFlare sends\nback an html page with a 403 HTTP status which will interogate your browser internals and leave a cookie `cf_clearance`\n-- _if_ you "pass" the challenge!.\n\nThis is of course a _disaster_ if you have used Ajax to send the request.\n\nThe idea here is to get that sweet, sweet CloudFlare cookie `cf_clearance` as soon as possible or at least before\nyou do any ajax requests.\n\nBasically if there is no `cf_clearance` cookie for a request this Blueprint will redirect to\na "managed" page where it will automatically upload an image to provoke the CloudFlare challenge --\nthen check for success.\n\nOnce your browser has the `cf_clearance` cookie then `CloudFlare-Challenge`\nwill leave your app alone.\n\nThis "solution" is not ideal but it maybe better than weird failures of your ajax requests that will\nultimately confuse/anger your users.\n\n**The big assumption here is that an upload of an image will provoke the CloudFlare challenge. If\nit doesn\'t then don\'t use this package!**\n\n## Configuration\n\nYou will need to set 1-5 configuration variables\n\n```python\n# path to a static image (required) e.g:\nCF_IMAGE_FILENAME = "img/Three-pink-daisies.jpeg"\n# endpoint to redirect to after challenge\nCF_REDIRECT_TO = None\n# template to inherit from. Defaults to one provided by cloudflare_challenge.\nCF_MAIN_TEMPLATE = None\n# list of endpoint prefixes that will be white/black listed\n# can be just a string\nCF_WHITE_LIST = ()\nCF_BLACK_LIST = ()\n```\n\nIf `CF_IMAGE_FILENAME` is missing or None then the blueprint will _silently_ not be registered even\nif `init_app` is called. `init_app` is indempotent.\n\nThe image filename will be used by `url_for(\'static\', filename=CF_IMAGE_FILENAME)` to\ngenerate a url. The image should be large enough to provoke a challenge. Choose an image\nthat will already be cached in your brower such as a banner image in your flask landing page.\n\nIf you specify a template (`CF_MAIN_TEMPLATE`) it should have a `content` block\n(for html, this is where the iframe is blatted) and a `js` block (for javascript).\n\nIf `CF_REDIRECT_TO` is missing or None then steps will be taken to redirect back to\nthe original page that prompted the redirection to the challenge page otherwise it will\nredirect back to `/`. **Remember:** `CF_REDIRECT_TO` expects a flask _endpoint_ not a URL.\n\nWhite listed endpoints won\'t trigger a check for CloudFlare cookies, headers etc.\nUse this for "static" images, css etc (the `static` endpoint is already white listed).\n\nYou can blacklist flask endpoints -- possibly endpoints that generate html with forms in them\nand thus might trigger the challenge.\n\nThe black list is checked first then the white list.\n\nEither way, Ajax requests (with a `X-Requested-With` header) will not trigger the challenge page (no point really since\nthis doesn\'t help -- too late!).\n\nIt is maybe the best to black list endpoints that generate html forms for the user to fill out, or\nany page that might send an ajax request due to user interaction. You will want to trigger the\nchallenge **before** any Ajax/form upload is undertaken.\n\n## Usage\n\nBasic usage\n\n```python\nfrom flask import Flask\nfrom cloudflare_challenge import init_app\n\napp = Flask(__name__)\napp.config.from_pyfile("config.py") # say\ninit_app(app, url_prefix=\'/someprefix\')\n```\n\n## Client Side\n\nIf you are using jQuery on a page to enable Ajax then you can ensure Challenges\nare detected by adding to your page:\n\n```jinja\n    {% from "cloudflare-macros.html" import cf_challenge %}\n    {{ cf_challenge() }}\n```\n\nThen Ajax challenges will be detected and logged.\n\nIf, in addition you set `MAIL_SERVER` _and_ `CF_MAIL_RECIPIENT`, then cloudflare-challenge will attempt to\nsend an email too.\n\nIf you only want this part then set `CF_WHITE_LIST = \'*\'`\n',
    'author': 'arabidopsis',
    'author_email': 'ian.castleden@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
