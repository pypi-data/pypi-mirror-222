===============
pop-create-idem
===============

Project description
+++++++++++++++++++

`pop-create-idem` is an extension of `pop-create` that creates boilerplate code for new `idem-cloud` projects. `pop-create-idem` includes code that transforms a CloudSpec dictionary into idem states, tools, and exec modules. Your unique `pop_create` plugin's purpose is to convert API documentation into the CloudSpec format.

**Note**: It is recommended that you use a Python virtual environment when creating a new Idem provider plugin.

Create a virtual environment
++++++++++++++++++++++++++++

Before you start, ensure that you installed Python 3.8 or later. If you are running 3.7 or earlier, you might need to use `python3` instead of `python` in the commands in the rest of this tutorial.

To verify your Python version, run the following command:

.. code-block:: bash

    python -V

Next, create your virtual environment:

.. code-block:: bash

    python -m venv env
    source env/bin/activate

Now you should be in your new Python virtual environment.

Update pip
++++++++++

Next, update to the latest version of `pip` inside your virtual environment:

.. code-block:: bash

    pip install -U pip


Install dependencies
++++++++++++++++++++

Next, you need to install `pop-create`:

.. code-block:: bash

    pip install pop-create


You now have access to the `pop-create` command for creating Idem plugins.

Install `pop-create-idem`
+++++++++++++++++++++++++

Install `pop-create-idem` with `pip` from the project root:

.. code-block:: bash

    pip install -e {project_root}

Next, install `pop-create-idem` with `pip` from PyPi:

.. code-block:: bash

    pip install pop-create-idem


Generate an Idem Cloud plugin
+++++++++++++++++++++++++++++

To generate a new skeleton Idem Cloud plugin, run the following command:

.. code-block:: bash

    pop-create idem-cloud --directory /path/to/new/project --project-name=idem-{my_cloud} --simple_cloud_name={my_cloud}

This command creates a new project with the directory structure needed to get started with your plugin.

Generate an Idem plugin with a Swagger specification
====================================================

To generate a new Idem plugin with a Swagger specification, run the following command:

.. code-block:: bash

    pop-create swagger --directory /path/to/new/project --specification={swagger-spec-yaml-or-accessible-swagger-spec-json-url} --project-name=idem-{my_cloud} --simple_cloud_name={my_cloud}

Generate an Idem plugin with an OpenAPI3 specification
======================================================

To generate a new Idem plugin project with an OpenAPI3 specification, run the following command:

.. code-block:: bash

    pop-create openapi3 --directory /path/to/new/project --specification={openapi3-spec-yaml-or-accessible-openapi3-spec-json-url} --project-name=idem-{my_cloud} --simple_cloud_name={my_cloud}


This command creates a new project with the boilerplate code needed to get started with each respective cloud provider.

Next steps
++++++++++

After you generate your Idem plugin:

* Try the example Swagger petstore tutorial in the `tutorial` directory, which walks you through generating an Idem plugin with a Swagger specification.
* Configure the plugin for your provider. See the `pop-create-idem` quickstart for instructions.
