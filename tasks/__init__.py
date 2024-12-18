from invoke import Collection

import packages
import infra
import migration


namespace = Collection(packages, infra, migration)
