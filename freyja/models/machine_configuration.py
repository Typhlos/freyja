from pathlib import Path
from typing import List, Optional

from pydantic import BaseModel, Field

from freyja.models.network_configuration import NetworkConfiguration


class User(BaseModel):
    username: Optional[str] = "freyja"
    password: Optional[str] = "$6$GM./aNJikL/g$AR2c35i1QIaimKo/zOC/1Qg2JO65ysPPjv/leWBcgBXaxNV3V8IcgJVeTzt4VHWzcja66zsBnR1iyYtO2DPme/"
    keys: Optional[List[str]] = None
    groups: Optional[List[str]]


class Ignition(BaseModel):
    version: str
    file: Optional[Path]


class WriteFile(BaseModel):
    source: Path
    destination: Path
    permissions: Optional[str] = "0600"
    owner: Optional[str] = "root:root"


class MachineConfiguration(BaseModel):
    image: str
    os: str
    hostname: str
    networks: Optional[List[NetworkConfiguration]]
    users: List[User] = [User()]
    disk: Optional[int] = 30
    memory: Optional[int] = 4096
    vcpus: Optional[int] = 2
    packages: Optional[List[str]]
    ignition: Optional[Ignition]
    runcmd: Optional[List[str]]
    write_files: Optional[List[WriteFile]] = Field(None, alias="write-files")
    update: Optional[bool] = False
    reboot: Optional[bool] = False
    arch: Optional[str]
    machine: Optional[str]
    cpu: Optional[str]
