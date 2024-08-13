All config is set on `config` dir. Every option is documented.

> [!important]  
> These configuration files allow you to configure things like your database connection information, your mail server information, as well as various other core configuration values such as your application timezone and encryption key.  

You can get a quick overview of your application's configuration, drivers, and environment via the `about` Artisan command:

  

```Shell
php artisan about
```

## Env config

The environment (.env) uses DotEnv lib.

The `.env` file is read in `env` function, so you might, as well, set an `.env.example` file for your team to locate differences and what to change.

### More env files

`.env` is the default file to the app, but you can specify APP_ENV variable provided on `--env` CLI arg.

# Environment Var Types

|   |   |
|---|---|
|`.env` Value|`env()` Value|
|true|(bool) true|
|(true)|(bool) true|
|false|(bool) false|
|(false)|(bool) false|
|empty|(string) ''|
|(empty)|(string) ''|
|null|(null) null|
|(null)|(null) null|

If you need to define an environment variable with a value that  
contains spaces, you may do so by enclosing the value in double quotes:  

> [!important]  
> APP_NAME="My Application"  

  

# Retrieving Env Config

All of the variables listed in the `.env` file will be loaded into the `$_ENV` PHP super-global.

`env` function args (’arg1’, false).

  

## Curr Env

You can code to a specific `env` by checking `App::environment` value:

```PHP
if (App::environment('local')) {
    // The environment is local
}
```

## ENCRYPT ENVIRONMENT

# **// TODO**

  

# Acessing config values

The `config` will return a specific value from the config or you even can set at runtime a change for the config files by sending an array on this syntax:

```PHP
config(['app.timezone' => 'America/Chicago']);
```

  

## Caching

Caching is simplified by just running the command `php artisan config:cache` , so, you don’t need to run it on local development.

> Once the configuration has been cached, your application's .env file will not be loaded by the framework during requests or Artisan commands

You can clear the cache by running `php artisan config:clear`

  

# Env Modes

### DEBUG

can be set on `.env` file by changing APP_DEBUG value

### MAINTENANCE

an exception will be thrown for the user when trying to request anything in the application (error code 503)

it can be activated by running `php artisan down`

You can make the browser refresh the page automatically for the user by sending `--refreseh=$_value_in_sencods_$`

  

> you can bypass with a code running `php artisan down --secret="1630542a-246b-4b66-afa1-dd72a4c43515"`

you can also `--redirect` or pre `--render` the error for the user.

  

`php artisan up` will disable maintenance