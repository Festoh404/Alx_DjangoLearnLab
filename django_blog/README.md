## User Authentication System

This project includes a complete user authentication system with the following features:

### Features

- **User Registration**: New users can create an account via the `/register/` endpoint.
- **User Login**: Existing users can log in using their credentials at `/login/`.
- **User Logout**: Authenticated users can log out via the `/logout/` endpoint.
- **User Profile**: A personalized profile page is available to authenticated users at `/profile/`.

### How to Use

1. **Register**: Navigate to `http://127.0.0.1:8000/register/` and fill out the form to create a new account.
2. **Log In**: Go to `http://127.0.0.1:8000/login/` and use your new credentials to log in.
3. **Access Profile**: After logging in, you will be redirected to your profile page at `http://127.0.0.1:8000/profile/`.
4. **Log Out**: Log out by clicking the "Logout" link in the header.

### Security

- All forms are protected with Django's **CSRF tokens** to prevent cross-site request forgery attacks.
- User passwords are automatically **hashed** by Django's built-in authentication system, ensuring they are stored securely.
