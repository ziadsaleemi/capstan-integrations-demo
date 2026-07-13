# Capstan Integrations Demo

One source-controlled demo used to prove four Capstan integration paths:

| Integration | Repository content | Expected proof |
| --- | --- | --- |
| Event-Driven Ansible | `extensions/eda/rulebooks/capstan_demo.yml` | EDA project sync discovers the rulebook and an activation emits demo events. |
| Galaxy NG | Collection metadata, role, module, and playbook | `ansible-galaxy collection build` publishes `r92.capstan_demo` and Galaxy exposes its real contents. |
| Gatekeeper | `gatekeeper/policies/` | Capstan previews, dry-runs, and applies the template and constraint through its governed project-sync API. |
| Project Quay | `ee/execution-environment.yml` | A saved EE build template builds this project and pushes `admin/capstan-integrations-demo:latest`. |

## Local validation

```bash
./scripts/validate.sh
```

The script always validates YAML and builds the collection. When the Gatekeeper `gator` CLI is installed, it also proves that the allowed fixture passes and the missing-label fixture is rejected.

## Galaxy NG

Build the artifact:

```bash
ansible-galaxy collection build --output-path dist
```

Publish it with a token supplied at runtime:

```bash
ansible-galaxy collection publish \
  dist/r92-capstan_demo-1.0.0.tar.gz \
  --server "$GALAXY_SERVER" \
  --api-key "$GALAXY_TOKEN"
```

## Event-Driven Ansible

Create an EDA project from this Git URL and synchronize it. EDA discovers rulebooks under `extensions/eda/rulebooks`. The included rulebook uses a finite range source, writes two debug events, and then shuts itself down, making repeated smoke tests deterministic.

## Gatekeeper

Sync `gatekeeper/policies` from the Capstan Project. The constraint is deliberately non-blocking (`enforcementAction: dryrun`) and only selects Kubernetes objects carrying:

```yaml
capstan.r92.io/demo: "true"
```

No production object is affected unless it is explicitly opted into the demo label.

## Project Quay

Create an EE build template with:

- Project: `Capstan Integrations Demo`
- Namespace: `admin`
- Repository: `capstan-integrations-demo`
- Definition: `ee/execution-environment.yml`
- Context: `ee`
- Tag: `latest`

The resulting image includes `r92.capstan_demo` from this Git repository and validates the collection during the image build.
