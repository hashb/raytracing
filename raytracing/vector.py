
import jax.numpy as jnp

class Vector3D:
    """
    """

    def __init__(self, vec=None) -> None:
        if vec is None:
            self.data = jnp.zeros(shape=(3,))
        else:
            self.data = vec

