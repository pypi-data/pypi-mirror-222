=========
idem-helm
=========

The Idem Helm provider

About
=====

An Idem plug-in to manage Helm resources. Helm is a package manager for Kubernetes.

What is POP?
------------

This project is built with `pop <https://pop.readthedocs.io/>`__, a Python-based implementation of *Plugin Oriented Programming (POP)*. POP seeks to bring together concepts and wisdom from the history of computing in new ways to solve modern computing problems.

For more information:

* `Intro to Plugin Oriented Programming (POP) <https://pop-book.readthedocs.io/en/latest/>`__
* `pop-awesome <https://gitlab.com/saltstack/pop/pop-awesome>`__
* `pop-create <https://gitlab.com/saltstack/pop/pop-create/>`__

Getting Started
===============

Prerequisites
-------------

* Python 3.7+
* git *(if installing from source or contributing to the project)*

  To contribute to the project and set up your local development environment, see ``CONTRIBUTING.rst`` in the source repository for this project.

Installation
------------

You can install ``idem-helm`` with the Python package installer (PyPI) or from source.

Install from PyPI
+++++++++++++++++

.. code-block:: bash

      pip install idem-helm

Install from Source
+++++++++++++++++++

.. code-block:: bash

   # Clone repo
   git clone git@<your-project-path>/idem-helm.git
   cd idem-helm

   # Set up venv
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e .

Usage
=====

Setup
-----

After installation, ``idem-helm`` execution and state modules are accessible to the pop *hub*.

For more information:

* `Intro to Plugin Oriented Programming (POP) <https://pop-book.readthedocs.io/en/latest/>`__
* `pop hub <https://pop-book.readthedocs.io/en/latest/main/hub.html#>`__

To use ``idem-helm`` execution and state modules to manage cluster resources, you need to set up authentication in one of the following ways.

**With environment variables**

Set KUBE_CONFIG_PATH and KUBE_CTX environment variables to the Kubernetes configuration file and context found in your ``kube_config`` file.

**In the Idem config file**

Edit the Idem config file to include the ``kube_config_path`` and ``context`` under account extras. Use the following example as a guideline.

.. code:: sls

    acct:
      extras:
        helm:
          default:
            kube_config_path: ~/.kube/config
            context: default

**In a credentials.yaml file**

Create or edit an Idem credentials.yaml file to add the ``kube_config_path`` and ``context`` to a Helm profile. Use the following example as a guideline.

..  code:: sls

    helm:
      default:
        kube_config_path: ~/.kube/config
        context: kubernetes-admin@kubernetes

For more about Idem credentials files, including recommended steps for encryption and environment variables, see `Authenticating with Idem <https://docs.idemproject.io/getting-started/en/latest/topics/gettingstarted/authenticating.html>`__

You are now ready to use idem-helm.

States
------

Idem SLS files use states to ensure that resources are in a desired configuration. An idem-helm SLS file supports three state functions: *present*, *absent*, and *describe*.

present
+++++++

The *present* function ensures that a resource exists. If a resource doesn't exist, running *present* creates it. If the resource already exists, running *present* might leave it unchanged, or update it if there are any configuration changes.

absent
++++++

The *absent* function ensures that a resource does not exist. If the resource exists, running *absent* deletes it. If the resource doesn't exist, running *absent* has no effect.

describe
++++++++

The *describe* function returns a list of all resources in the Kubernetes cluster of the same type as specified in the credential profile.

Accessing States
----------------

States can be accessed by their relative location in ``idem-helm/idem_helm/states``.

For example, a Helm release state can be created with the *present* function as shown in the following SLS file.

helm_release.sls:

.. code:: sls

    idem-helm-release-test:
      helm.release.present:
      - name: idem-redis
      - repository: https://charts.bitnami.com/bitnami
      - chart: redis
      - namespace: kube-system
      - resource_id: idem-redis
      - values:
            image:
                pullPolicy: IfNotPresent


The Idem command to create the preceding release state is:

.. code:: bash

    idem state $PWD/helm_release.sls

Current Supported Resources
---------------------------

helm
----

release
