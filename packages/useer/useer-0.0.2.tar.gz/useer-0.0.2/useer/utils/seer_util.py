import os

from pyspark.ml.feature import VectorAssembler
from pyspark.sql import DataFrame
from pyspark.ml.tuning import CrossValidator
from pyspark.ml.tuning import ParamGridBuilder
import numpy as np
import random

class SEERUtil:
    """
        pyspark作业工具类
    """

    def __init__(self):
        pass

    @staticmethod
    def add_vector_assembler_stage(pu, parent_df, feature_list, input_col, stage_order: int):
        """
            pipeline增加向量化过程
        """

        vector_assembler_col = 'vector_assembler'
        if not input_col:
            vectored = VectorAssembler(inputCols=feature_list, outputCol=vector_assembler_col, handleInvalid='skip')

            pu.save_stage(vectored, stage_order)

            stage_order += 1

            parent_df: DataFrame = vectored.transform(parent_df)

            input_col = vector_assembler_col

        return pu, input_col, parent_df, stage_order

    @staticmethod
    def delete_old_stage(pu, stage_order: int):
        """
            清理pipeline中旧的stage数据
        :param processor:
        :param stage_order:
        """

        if pu.fs.exists(pu.path(pu.stage_dir)) and len(pu.stage_uids) - 1 >= stage_order:
            old_stage_file = os.path.join(pu.stage_dir, '{}_{}'.format(stage_order, pu.stage_uids[stage_order]))

            print('old_stage_file: ' + old_stage_file)
            print('\r\n')

            pu.fs.delete(pu.path(old_stage_file))

    @staticmethod
    def save_feature_importances(spark, extra_args, model, feature_list):
        """
            保存模型特征重要性(model.featureImportances)
        :param spark:
        :param extra_args:
        :param model:
        :param feature_list:
        """
        feature_importances_path = extra_args.get('feature_importances_path', '')
        if feature_importances_path and hasattr(model, 'featureImportances'):
            print(f'has_featureImportances: {feature_importances_path}')
            print('\r\n')

            print('featureImportances: ' + str(model.featureImportances))
            print('\r\n')

            importances_df: DataFrame = spark.createDataFrame(
                list(zip(feature_list, [float(i) for i in model.featureImportances])),
                schema=['feature_name', 'feature_importance'])

            importances_df.write.saveAsTable(feature_importances_path, mode="overwrite")

    @staticmethod
    def save_feature_importances_v2(spark, extra_args, model, feature_list):
        """
            保存模型特征重要性(model.getFeatureImportances)
        :param spark:
        :param extra_args:
        :param model:
        :param feature_list:
        """
        feature_importances_path = extra_args.get('feature_importances_path', '')
        if feature_importances_path:
            print(f'has_featureImportances: {feature_importances_path}')
            print('\r\n')

            print('featureImportances: ' + str(model.getFeatureImportances()))
            print('\r\n')

            importances_df: DataFrame = spark.createDataFrame(
                list(zip(feature_list, [float(i) for i in model.getFeatureImportances()])),
                schema=['feature_name', 'feature_importance'])

            importances_df.write.saveAsTable(feature_importances_path, mode="overwrite")

    @staticmethod
    def automl_ex(model, evaluator, grid, df):
        cv = CrossValidator(estimator=model,
                            estimatorParamMaps=grid,
                            evaluator=evaluator,
                            numFolds=3)
        cvModel = cv.fit(df)
        return cvModel.bestModel

    @staticmethod
    def get_automl_params(model, automl_config, field_map={}):
        parameter_type = automl_config.get('parameter_type', '')
        parameter_nums = automl_config.get('parameter_nums', 2)
        parameter_range = automl_config.get('parameter_range', [])
        if parameter_type == 'GridSearch':
            # 网格拆分
            grid_obj = ParamGridBuilder()
            for parame in parameter_range:
                field = field_map.get(parame['field'], parame['field'])
                scope_value = parame.get('scope_value', [])
                if not all(isinstance(x, (int, float)) for x in scope_value) or len(scope_value) != 2:
                    continue
                min, max = scope_value
                values = np.linspace(min, max, parameter_nums).tolist()
                field_type = parame.get('data_type')
                if not field_type:
                    field_type = parame.get('dataType')

                if field_type == "int":
                    values = [int(i) for i in values]
                grid_obj.addGrid(eval(f'model.{field}'), values)
            return grid_obj.build()

        else:
            # 随机拆分
            field_value_map: dict = {}
            grid_list: list = []
            for i in range(parameter_nums):
                if not grid_list:
                    grid_obj = ParamGridBuilder()
                    for parame in parameter_range:
                        field_type = parame.get('data_type')
                        if not field_type:
                            field_type = parame.get('dataType')
                        field = field_map.get(parame['field'], parame['field'])
                        scope_value = parame.get('scope_value', [])
                        if not all(isinstance(x, (int, float)) for x in scope_value) or len(scope_value) != 2:
                            continue
                        min, max = scope_value
                        if not field_type == "float":
                            random_func = random.randint
                        else:
                            random_func = random.uniform
                        value = random_func(min, max)
                        field_value_map[field] = [min, max, random_func]
                        if not grid_list:
                            grid_obj.addGrid(eval(f'model.{field}'), [value])
                    grids = grid_obj.build()
                    grid_list.append(grids[0])
                else:
                    dic = {}
                    for k, v in grid_list[0].items():
                        min, max, random_func = field_value_map[k.name]
                        dic[k] = random_func(min, max)
                    grid_list.append(dic)
            return grid_list
