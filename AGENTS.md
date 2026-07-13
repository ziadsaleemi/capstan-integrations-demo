# Capstan Integrations Demo

This repository is the reusable end-to-end fixture for Capstan integrations with Event-Driven Ansible, Galaxy NG, Kubernetes Gatekeeper, and Project Quay.

## Validation

Run `./scripts/validate.sh` before committing. The script builds the Ansible collection and validates every YAML document. If `gator` is installed, it also runs the Gatekeeper policy suite.

## Safety

- Keep the Gatekeeper demo constraint in `dryrun` mode.
- Scope the constraint with the `capstan.r92.io/demo=true` label selector.
- Never commit Galaxy, Quay, Kubernetes, or source-control credentials.
- Keep deployment-specific URLs in Capstan settings, not in this repository.

## Release

The collection version is defined in `galaxy.yml`. Build artifacts belong in `dist/` and are ignored by Git.
