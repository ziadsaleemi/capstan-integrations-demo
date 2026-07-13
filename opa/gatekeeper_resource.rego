package awx.gatekeeper_resource

import rego.v1

default allow := false

# Permit an explicitly approved project sync by a Capstan system administrator.
allow if {
    input.source == "gatekeeper_project_sync"
    input.mode == "apply"
    input.human_approved == true
    input.user.is_superuser == true
}
