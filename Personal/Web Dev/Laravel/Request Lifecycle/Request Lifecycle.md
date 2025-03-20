The entry point for all requests to a Laravel application is the `public/index.php` file

The `index.php` file loads the Composer generated autoloader definition, and then retrieves an instance of the Laravel application from `bootstrap/app.php`

# HTTP/ Console Kernels

These two kernels serve as the central location that all requests flow  
through. For now, let's just focus on the HTTP kernel, which is located  
in  
`app/Http/Kernel.php`

In this kernel, the app runs logging, error handling, read .env files and after, handles the request itself.

The HTTP kernel set and handles all HTTP middleware that must run before the app handles the request.

## Middleware

Automates some routing and verification, for example, the user auth. It allows an easy abstraction for, like the name says, between event handling.

They can handle HTTP sessions, CSRF token and more.

## HTTP Kernel Methods

- Request
- Response

## Service Providers

This layer works on registering service container bindings, event listeners, middleware, and even routes. Basically, where you will config the application.

### List of providers set on config/app.php

Firstly, the function `register` registers 👍 all providers set on the array of config/app.php

Then, `boot` function is called upon each provider set on the list

# Routing

Just enter there, future me, don't be that lazy

[[Routing]]