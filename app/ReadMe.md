# API development

## Using FastAPI
- start from same directory app: `uvicorn main:app --reload`
- start app which is in directory named app: `uvicorn app.main:app --reload`
- Dokumentacija na [FastAPI](https://fastapi.tiangolo.com/)

## Schemas.py
- We can data types which get sent or returned from database, so we can compile useful data and check if data is in correct shape

## Models.py
- Defines the SQL ORM, (object relational mapping)
- It uses [sqlalchemy](https://www.sqlalchemy.org/)

## Database.py
- Opens database session

## Routers
- Define the API function which manages communication with database, get, post, update, delete


## MORE:
- More complex types with annotated
q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):

[Full stack app example](https://github.com/tiangolo/full-stack-fastapi-template)


# PRODUCTION:
- Set environment variables on a machine not just in .env file
- `uvicorn --host 0.0.0.0 app.main:app` (so you can access from anywhere)
- gunicorn for production, so you can run multiple instances of the app: `gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000`
- sudo systemctl enable `[name-of-service-api]` - so it reloads on boot

### Server setup:
```bash
    1  exit
    2  logout
    3  exit
    4  logout
    5  vim ~/.ssh/authorized_keys 
    6  ll ~/.ssh
    7  ll ~/
    8  exit
    9  cd ..
   10  ls
   11  cd home/
   12  ls
   13  cd ..
   14  cd root/
   15  sudo root/
   16  cat /etc/passwd
   17  cat /etc/group
   18  exit
   19  sudo apt upgrade
   20  exit
   21  sudo ls -la /root
   22  ll
   23  sudo ll
   24  ls -la
   25  sudo ls -la
   26  cd .ssh
   27  sudo cd .ssh
   28  sudo cat .ssh/authorized_keys
   29  sudo cd .ssh
   30  cd .ssh
   31  sudo "cd .sh"
   32  sudo "cd .ssh"
   33  cd rok
   34  cd ~
   35  sudo ls -la /root
   36  cd /root
   37  sudo cd /root
   38  sudo -i
   39  sudo -s
   40  type cd
   41  cd rok
   42  cd ~
   43  cd /bin
   44  ls
   45  ls | grep "cd"
   46  ls | grep "c"
   47  ls | grep "echo"
   48  cd ~
   49  sudo apt upgrade
   50  pwd
   51  mkdir app
   52  cd app/
   53  virtualenv venv
   54  ls -la
   55  ll
   56  source venv/bin/activate
   57  deactivate 
   58  mkdir src
   59  cd src/
   60  git clone https://github.com/rokHladin/example-fastapi.git .
   61  ll
   62  cd ..
   63  source venv/bin/activate
   64  cd src/
   65  cat requirements.txt 
   66  pip install -r requirements.txt 
   67  uvicorn app.main:app
   68  export MY_NAME=rok
   69  printenv
   70  unset MY_NAME
   71  printenv
   72  cd ~
   73  ls
   74  touch .env
   75  ll
   76  vim .env
   77  cat .env
   78  source .env
   79  printenv
   80  unset MY_NAME 
   81  unset MY_PASSWORD 
   82  printenv
   83  vim env
   84  ll
   85  vim .env
   86  cat .env
   87  set -o allexport; source /home/rok/.env; set +o allexport
   88  printenv
   89  sudo reboot
   90  ll
   91  vim profile
   92  vim .profile 
   93  cat .profile
   94  printenv
   95  exit
   96  cd app/src/
   97  ps -aef | grep -i gunicorn
   98  vim .env 
   99  cd app/
  100  source venv/bin/activate
  101  cd src/
  102  cd ..
  103  ls
  104  cd src/
  105  ls
  106  cd alembic/
  107  ls
  108  cd versions/
  109  ls
  110  cd ..
  111  alembic upgrade head
  112  cd ..
  113  cd src/
  114  uvicorn app.main:app
  115  uvicorn --host 0.0.0.0 app.main:app --help
  116  uvicorn --host 0.0.0.0 app.main:app
  117  gunicorn --version
  118  pip install gunicorn
  119  pip install httptools
  120  pip install uvtools
  121  gunicorn --help
  122  iscpu
  123  cat /proc/cpuinfo 
  124  gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
  125  pip freeze
  126  uvloop --version
  127  gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
  128  uvicorn --host 0.0.0.0 app.main:app
  129  cd /etc/systemd/system
  130  ls
  131  cd ~
  132  pwd
  133  cd apo
  134  cd app
  135  cd src/
  136  pwd
  137  cd ..
  138  cd venv/
  139  pwd
  140  ls
  141  cd bin/
  142  ls
  143  cd /etc/systemd/system/
  144  ls
  145  sudo vim api.service
  146  systemctl start api
  147  systemctl status api
  148  cd ~
  149  ls
  150  ls -l
  151  ll
  152  systemctl status api
  153  sudo systemctl enable api
  154  systemctl status api
  155  sudo reboot
  156  systemctl status api
  157  systemctl start apu
  158  systemctl start api
  159  systemctl status api
  160  sudo apt install nginx -y
  161  nginx
  162  systemctl start nginx
  163  sudo apt install nginx -y
  164  systemctl start nginx
  165  cd /etc/nginx/
  166  cd sites-available/
  167  ls
  168  cat default 
  169  vim default 
  170  sudo vim default 
  171  systemctl restart nginx
  172  systemctl status nginx
  173  systemct status api
  174  systemctl status api
  175  systemctl restart api
  176  systemctl status api
  177  systemctl status nginx
  178  systemctl status api
  179  systemctl status nginx
  180  snap --version
  181  sudo snap install --classic certbot
  182  sudo
  183  sudo snap install --classic certbot
  184  ls
  185  ll
  186  systemct status ai
  187  systemctl status api
  188  systemctl --help
  189  systemctl stop api
  190  systemctl status api
  191  systemctl start api
  192  systemctl status api
  193  sudo ln -s /snap/bin/certbot /usr/bin/certbot
  194  sudo certbot --nginx
  195  ls
  196  cd app/
  197  cd /etc/nginx/
  198  cd sites-available/
  199  ls
  200  cat default 
  201  systemctl status api
  202  systemctl status nginx
  203  systemctl start api
  204  systemctl status api
  205  systemctl status nginx
  206  sudo ufw status
  207  sudo ufw allow http
  208  sudo ufw allow https
  209  sudo ufw allow ssh
  210  sudo ufw enable
  211  sudo ufw status
  212  sudo ufw enable
  213  sudo ufw status
  214  cd ~
  215  cd app
  216  cd src/
  217  git pull
  218  sudo systemctl restart api
```


## Secure Authentication
1. **Use HTTPS**: Always use HTTPS for secure communication. This ensures that the data, including your sensitive authentication tokens, is encrypted during transit.

2. **Store Passwords Securely**: Never store passwords in plain text. Use hashing algorithms to store passwords. FastAPI's security utilities support "password hashing" out of the box.

3. **Use OAuth2 or JWT for Token-Based Authentication**: These are standard protocols for handling authentication and authorization in APIs and are supported by FastAPI.

4. **Handle Authentication in Middleware**: This allows you to check for valid authentication credentials on every request before it reaches your route functions.

5. **Use Role-Based Access Control (RBAC)**: This allows you to restrict access to certain parts of your API based on the role of the user.

6. **Use Secure Cookies for Storing Tokens**: If you need to store tokens on the client side, secure HTTP-only cookies can be a good option. This can help protect against cross-site scripting (XSS) attacks.

7. **Validate User Input**: Always validate user input to protect against attacks such as SQL injection, cross-site scripting (XSS), and remote code execution.

8. **Use Environment Variables for Sensitive Data**: Never hard-code sensitive data like database URIs, secret keys, etc. Instead, use environment variables.

9. **Keep Third-Party Packages Updated**: Always keep your third-party packages updated, especially those related to security and authentication. This ensures that you get the latest security patches.

10. **Error Handling**: Don't reveal too much information in your error messages. This can expose details about your application's inner workings that could be useful to attackers.