The main route is set the on `App/Providers/RouteServiceProvider.php` .

This loads up all routes set on `routes` dir. This file will manage where to send the user whenever he is authenticated ou not.

Once the application has been bootstrapped and all service providers have been registered, the `Request` will be handed off to the router for dispatching. The router will dispatch the request for another route or a controller or run a middleware (which was registered before)

Once the application has been bootstrapped and all service providers have been registered, the `Request` will be handed off to the router for dispatching. The router will dispatch the request for another route or a controller or run a middleware (which was registered before)

If the request passes through all of the matched route's assigned middleware, the route or controller method will be executed and the response returned by the route or controller method will be sent back through the route's chain of middleware.

Finally, once the response travels back through the middleware, the HTTP kernel's `handle` method returns the response object and the `index.php` file calls the `send` method on the returned response. The `send` method sends the response content to the user's web browser.

## Coding it