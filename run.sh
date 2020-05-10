#!/usr/local/bin/bash

# when running for reals strict validation is done with
# for performance probably don't want to validate
# app.add_api('my_apy.yaml', strict_validation=True)

connexion run swagger.yaml -v --debug --strict-validation
