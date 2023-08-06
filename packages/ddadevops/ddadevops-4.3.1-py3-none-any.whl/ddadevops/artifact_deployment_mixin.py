from pybuilder.core import Project
from .devops_build import DevopsBuild

# """
# Functional Req:

# General process for deploying prebuilt (meissa) binaries to our own repo server.

# [0]
# get artifact deployment url

# [1]
# build ubejarServer
# build ubejarDesktop
# build ubejarSyspec

# [2]
# get release token

# [3]
# get release tag

# [4]
# post a json message containting [3] to [0], watching stdout for answers
#     authorized by [2]
#     validate if [4] was successful by reading stdout
#         or create error message containing ID of release

# [5]
# get release-id
# print release-id

# [6]
# generate sha256 sums & generate sha512 sums of results of [1]

# [7]
# push results of [1] & [6] to [0]/[5]

# """


class ArtifactDeploymentMixin(DevopsBuild):
    def __init__(self, project: Project, inp: dict):
        super().__init__(project, inp)
