import math
from time import sleep
from ldimbenchmark import LDIMMethodBase, BenchmarkData, BenchmarkLeakageResult
from ldimbenchmark.classes import MethodMetadata, MethodMetadataDataNeeded
from typing import List, Union


class TestPolynomialComplexityLeakageDetectionMethod(LDIMMethodBase):
    """
    Test Complexity: Polynomial
    """

    def __init__(self):
        super().__init__(
            name="Polynomial Complexity",
            version="1.0",
            metadata=MethodMetadata(
                data_needed=MethodMetadataDataNeeded(
                    pressures="ignored",
                    flows="ignored",
                    levels="ignored",
                    model="ignored",
                    demands="ignored",
                    structure="ignored",
                ),
                hyperparameters=[],
            )
            # hyperparameters={"est_length": "3 days", "C_threshold": 3, "delta": 4},
        )

    def prepare(self, train_data: BenchmarkData) -> None:
        number = (
            int(len(train_data.demands[list(train_data.demands.keys())[0]]) / 280) ** 2
        )
        # 16 Byte * 65536 = 1 MB
        memory = [None] * number * 65536 * 2
        sleep(number / 100)
        return

    def detect_offline(
        self, evaluation_data: BenchmarkData
    ) -> List[BenchmarkLeakageResult]:
        number = (
            int(
                len(evaluation_data.demands[list(evaluation_data.demands.keys())[0]])
                / 280
            )
            ** 2
        )
        # 16 Byte * 65536 = 1 MB
        memory = [None] * number * 65536 * 2
        sleep(number / 100)
        return []

    def detect_online(self, evaluation_data) -> Union[BenchmarkLeakageResult, None]:
        return None
