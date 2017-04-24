# Gomatic Kickstarter

A repository which lets you get started with Gomatic with a few examples.

# Setup

Prerequisites:

- Python (tested on 2.7.x, will _not_ work with 3.x)
- pip (tested on 8.1.2)
- virtualenv (tested on 13.1.2)
- docker-compose (tested on 1.11.2)

_Note: If you don't have `virtualenv` installed you can use `pip` to install it._

# Deploy your pipelines

Run the `docker-compose` environment:

```sh
$ docker-compose up
```

And now you can deploy the already existing code with

```sh
$ ./deploy
```

This will create the Virtualenv if it hasn't been created already and then try to run your the Gomatic code against the virtual GoCD instance.

_Note: The GoCD server takes a lot of time to get started, sometimes up to 60 seconds. Keep that in mind when provisioning your instance._
