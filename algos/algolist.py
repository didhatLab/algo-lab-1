import enum
from typing import Dict, Callable, List, Any

from algos.linear import linear_search
from algos.binsearch import bin_search
from algos.exp import exp_search


class AlgoTypes(enum.Enum):
    linear = "linear"
    binary = "binary"
    exp = "exp"


ALL_ALGOS: Dict[AlgoTypes, Any] = {
    AlgoTypes.linear: linear_search,
    AlgoTypes.binary: bin_search,
    AlgoTypes.exp: exp_search
}
