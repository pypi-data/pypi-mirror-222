import pytest
from snowplow_tracker import SelfDescribingJson, Snowplow

from gitlab_sdk import Client
from gitlab_sdk.client import SCHEMAS

app_id = "app_id"
host = "host"
event_name = "event_name"
event_payload = {"pay": "load"}
user_id = "12"
user_attributes = {"user_name": "Matthew"}


@pytest.fixture(autouse=True)
def cleanup_after_test():
    yield
    Snowplow.reset()


def test_initializes_snowplow_tracker_correctly(mocker):
    mocked_tracker_creation = mocker.patch("snowplow_tracker.Snowplow.create_tracker")

    Client(app_id=app_id, host=host)

    creation_args = mocked_tracker_creation.call_args[1]
    assert creation_args["app_id"] == app_id
    assert creation_args["namespace"] == "gitlab"
    assert creation_args["endpoint"] == host
    assert creation_args["emitter_config"].batch_size == 1


def test_track(mocker):
    mocked_track = mocker.patch("snowplow_tracker.Tracker.track_self_describing_event")

    Client(app_id=app_id, host=host).track(event_name, event_payload)

    track_args = mocked_track.call_args[1]
    assert list(track_args.keys()) == ["event_json"]
    assert track_args["event_json"].schema == SCHEMAS["custom_event"]
    assert track_args["event_json"].data == {"name": event_name, "props": event_payload}


def test_identify_without_user_attributes(mocker):
    mocked_set_subject = mocker.patch("snowplow_tracker.Tracker.set_subject")

    client = Client(app_id=app_id, host=host)
    client.identify(user_id)
    client.track(event_name, event_payload)

    subject = mocked_set_subject.call_args[0][0]
    assert subject.standard_nv_pairs["uid"] == user_id


def test_identify_with_user_attributes(mocker):
    mocked_set_subject = mocker.patch("snowplow_tracker.Tracker.set_subject")
    mocked_track = mocker.patch("snowplow_tracker.Tracker.track_self_describing_event")

    client = Client(app_id=app_id, host=host)
    client.identify(user_id, user_attributes)
    client.track(event_name, event_payload)

    subject = mocked_set_subject.call_args[0][0]
    assert subject.standard_nv_pairs["uid"] == user_id

    track_args = mocked_track.call_args[1]
    assert list(track_args.keys()) == ["event_json", "context"]
    assert isinstance(track_args["event_json"], SelfDescribingJson)
    assert len(track_args["context"]) == 1
    assert track_args["context"][0].schema == SCHEMAS["user_context"]
    assert track_args["context"][0].data == user_attributes
