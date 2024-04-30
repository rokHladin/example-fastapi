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