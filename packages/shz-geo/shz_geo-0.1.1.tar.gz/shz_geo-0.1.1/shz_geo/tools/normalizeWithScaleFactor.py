from shz_types.datasets import anyDataset
from typeguard import typechecked 
import numpy as np
from typing import Union


@typechecked
def normalizeWithScaleFactor(dataset: anyDataset, scaleFactor: Union[int, float]):    
    if isinstance(dataset, list):
        dataset = np.array(dataset)

    normalized = dataset / scaleFactor 
    return normalized
