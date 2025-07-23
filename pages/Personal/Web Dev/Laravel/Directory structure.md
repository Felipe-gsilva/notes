- bootstrap → contains `app.php` and also `cached` info.
- config → all configuration files
- database → contains your database migrations, model factories and seeds.
- public → contains the entry point for all requests, on `index.php` file.
- resources → CSS and JS uncompiled assets.
- routes → Several route files are included with Laravel: `web.php`, `api.php`, `console.php`, and `channels.php`.
    - The `web.php` file contains routes that the `RouteServiceProvider` places in the `web` middleware group.
    - The `api.php` file contains routes that the `RouteServiceProvider` places in the `api`  
        middleware group. These routes are intended to be stateless, so  
        requests entering the application through these routes are intended to  
        be authenticated via tokens.  
        
    - The `console.php` file is where you may define all of your closure based console commands.
    - The `channels.php` file is where you may register all of the event broadcasting channels that your application supports.
- storage → The `storage` directory contains your logs, compiled Blade  
    templates, file based sessions, file caches, and other files generated  
    by the framework.  
    
- tests → contain all automated tests, which can be run using the command `phpunit`
- vendor → composer, basically

## THE `APP` DIR

- // TODO