from pathlib import Path

import pandas as pd
import pytest
from shapely import Point

from imxInsights import AreaStatusEnum, GeoJsonFeatureCollection, ImxSituationsEnum
from imxInsights.diff.imxDiff import ImxDiff
from imxInsights.domain.imx import Imx


def test_diff_area_status_enums():
    for item in [AreaStatusEnum[item] for item in ["DELETED", "CREATED"]]:
        assert item.is_created_or_deleted() is True

    for item in [AreaStatusEnum[item] for item in ["NO_CHANGE", "MOVED", "INDETERMINATE"]]:
        assert item.is_created_or_deleted() is not True


def shapely_point_to_gml(shapely_point: Point):
    if shapely_point.has_z:
        return f"{round(shapely_point.x, 3)},{round(shapely_point.y, 3)},{round(shapely_point.z, 3)}"
    else:
        return f"{round(shapely_point.x, 3)},{round(shapely_point.y, 3)}"


@pytest.mark.slow
def test_imx_parse_project_v500(get_imx_project_test_file_path, tmp_path: str):
    imx = Imx(get_imx_project_test_file_path)
    assert imx.imx_version == "5.0.0", "imx version should be 5.0.0"

    imx.generate_population_excel("tester.xlsx", ImxSituationsEnum.InitialSituation)
    file_path = Path("tester.xlsx")
    assert file_path.exists(), "file should exist"
    file_path.unlink()

    signals_geojson = imx.project.initial_situation.get_geojson(object_type_or_path="Signal")
    assert isinstance(signals_geojson, GeoJsonFeatureCollection), "should return feature collection"

    geojson_dict = imx.project.initial_situation.get_geojson_dict()
    assert isinstance(geojson_dict, dict), "should return dict"  # todo: test if content is FeatureCollection

    diff = ImxDiff(imx.project.initial_situation, imx.project.new_situation)
    signals_geojson_diff = diff.as_geojson(object_type_or_path="Signal")
    assert isinstance(signals_geojson_diff, GeoJsonFeatureCollection), "should return feature collection"

    geojson_dict_diff = diff.generate_geojson_dict()
    assert isinstance(geojson_dict_diff, dict), "should return dict"

    dict_of_df_of_all_types = diff.pandas_dataframe_dict()
    assert isinstance(dict_of_df_of_all_types, dict), "should return dict"

    df_micro_nodes = diff.pandas_dataframe("MicroNode", geometry=False)
    assert isinstance(df_micro_nodes, pd.DataFrame), "should pd.DataFrame"

    df_signals = diff.pandas_dataframe("Signal", geometry=True)
    assert isinstance(df_signals, pd.DataFrame), "should pd.DataFrame"

    df_rail_con = diff.pandas_dataframe("RailConnection", geometry=True)
    assert isinstance(df_rail_con, pd.DataFrame), "should pd.DataFrame"


# def test_imx_parse_situation_v500(get_imx_project_test_file_path, tmp_path: str):
#     imx = Imx(get_imx_project_test_file_path)
#     assert imx.imx_version == "5.0.0", "imx version should be 5.0.0"
