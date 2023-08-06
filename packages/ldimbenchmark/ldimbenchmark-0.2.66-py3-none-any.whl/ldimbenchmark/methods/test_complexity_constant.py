from ldimbenchmark import LDIMMethodBase, BenchmarkData, BenchmarkLeakageResult
from ldimbenchmark.classes import MethodMetadata, MethodMetadataDataNeeded
from typing import List, Union


class TestConstantComplexityLeakageDetectionMethod(LDIMMethodBase):
    """
    Test Complexity: Constant
    """

    def __init__(self):
        super().__init__(
            name="Constant Complexity",
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
        return

    def detect_offline(
        self, evaluation_data: BenchmarkData
    ) -> List[BenchmarkLeakageResult]:
        return []

    def detect_online(self, evaluation_data) -> Union[BenchmarkLeakageResult, None]:
        return None
