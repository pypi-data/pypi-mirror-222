import os

from pyspark.ml.feature import VectorAssembler
from pyspark.sql import DataFrame
from pyspark.ml.tuning import CrossValidator
from pyspark.ml.tuning import ParamGridBuilder
import numpy as np
import random


class DemoUtil:
    """
        pyspark作业工具类
    """

    def __init__(self):
        pass

    @staticmethod
    def test(a, b):
        return a + b
