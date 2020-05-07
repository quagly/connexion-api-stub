#!/usr/local/bin/bash

# when running for reals strict validation is done with
# app.add_api('my_apy.yaml', strict_validation=True)

connexion run swagger.yaml -v --debug --strict-validation
