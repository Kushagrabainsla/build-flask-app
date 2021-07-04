#!/bin/bash

echo "Name you app."

read appName
echo "Building Structure for ${appName}"

mkdir "${appName}" && cd "${appName}"

mkdir "flaskr" && mkdir "tests"

touch setup.py && touch requirements.txt



# Views part
echo "Creating VIEWS for ${appName}"


cd "flaskr"

touch "__init__.py" && mkdir "views" && mkdir "templates" && mkdir "static"


cd "views"

touch "db.py" && touch "auth.py" && touch "blog.py"

cd "../"


cd "templates"

touch "base.html" && mkdir "auth" && mkdir "blog"

cd "auth" && touch "login.html" && touch "register.html" && cd "../"
cd "blog" && touch "create.html.html" && touch "index.html" && touch "update.html" && cd "../"

cd "../"


cd "static"

touch "style.css" && cd "../"

cd "../"




# Tests part
echo "Creating TESTS for ${appName}"


cd "tests"

touch "test_db.py" && touch "test_auth.py" && touch "test_blog.py"

cd "../"




echo "${appName} build completed"
