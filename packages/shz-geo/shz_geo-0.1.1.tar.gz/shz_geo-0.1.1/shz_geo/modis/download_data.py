from typing import Iterator
from modis_tools.auth import ModisSession
from modis_tools.resources import CollectionApi, GranuleApi, Granule
from modis_tools.granule_handler import GranuleHandler
from typeguard import typechecked

@typechecked
def get_session(username: str, password: str):
    return ModisSession(username, password)

parana_bbox = [-55, -26.5, -48, -22]

@typechecked
def get_granules(session: ModisSession, start_date: str, end_date: str, bbox: list=parana_bbox, modis_name: str="MOD13Q1", modis_version: str="061"):
    collecation_client = CollectionApi(session=session)
    collections = collecation_client.query(short_name=modis_name, version=modis_version)
    granule_client = GranuleApi.from_collection(collections[0], session=session)
    parana_granules = granule_client.query(start_date=start_date, end_date=end_date, bounding_box=bbox)
    return parana_granules

@typechecked
def download_granules(session: ModisSession, granules: Iterator[Granule], target_path: str):
    GranuleHandler.download_from_granules(granules, session, path=target_path)