import scipy
import os
import yaml
from dataclasses import dataclass


@dataclass
class Config:
    # Gravity
    g: float = scipy.constants.g

    # Lengths of rods
    l_1: float = 1.0
    l_2: float = 1.0
    l_b: float = 0.2

    # Initial angle of rod 2 relative to rod 1
    theta_2_init_offset: float = 0.0

    # Point masses
    m_j: float = 1.0
    m_p: float = 1.0
    m_b: float = 0.5

    # Density of rods
    rho_1: float = 1.0 / l_1
    rho_2: float = 1.0 / l_2

    # Rod 1 extra rotational inertia
    I_extra: float = 0.0

    # Mass of driving weight and axle radius
    m_d: float = 10.0
    r_a: float = 0.1

    # Radius of rods and masses
    r_1: float = 0.0
    r_2: float = 0.0
    r_j: float = 0.0
    r_p: float = 0.0
    r_b: float = 0.0
    r_d: float = 0.0

    # Drag coefficients
    rho_air: float = 1.225
    Cd_cyl: float = 1.1
    Cd_sph: float = 0.47
    Cd_disk: float = 1.17


def load_config(config_path: str) -> Config:
    """
    Load the configuration from a YAML file.
    """
    assert os.path.isfile(config_path), f"Config file {config_path} does not exist."

    with open(config_path, "r") as f:
        file = yaml.safe_load(f)

    # Create a config object and populate it with values from file
    config = Config()
    for key, value in file.items():
        if hasattr(config, key):
            setattr(config, key, value)
        else:
            raise KeyError(f"Key {key} not found in config dataclass.")

    return config


def save_config(config: Config, config_path: str, overwrite: bool = False):
    """
    Save the configuration to a YAML file.
    """
    assert (
        not os.path.isfile(config_path) or overwrite
    ), f"Config file {config_path} already exists."

    with open(config_path, "w") as f:
        yaml.dump(config.__dict__, f)
