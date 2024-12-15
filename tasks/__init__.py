from invoke import Collection

import packages
import infra


namespace = Collection(packages, infra)
