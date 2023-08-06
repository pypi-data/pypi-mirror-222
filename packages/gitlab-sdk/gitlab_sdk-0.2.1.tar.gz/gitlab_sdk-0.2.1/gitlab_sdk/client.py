"""
This module provides a client interface for tracking events using Snowplow.
"""
from snowplow_tracker import EmitterConfiguration, SelfDescribingJson, Snowplow, Subject

SCHEMAS = {
    "custom_event": "iglu:com.gitlab/custom_event/jsonschema/1-0-0",
    "user_context": "iglu:com.gitlab/user_context/jsonschema/1-0-0",
}
DEFAULT_TRACKER_NAMESPACE = "gitlab"


class Client:
    """
    Client to interact with Snowplow and send tracking events.
    """

    def __init__(
        self,
        app_id: str,
        host: str,
    ):
        """
        Initializes the Client with given app_id and host.

        Args:
            app_id (str): Application ID.
            host (str): Host for the collector.
        """
        emitter_config = EmitterConfiguration(batch_size=1)
        self.tracker = Snowplow.create_tracker(
            app_id=app_id,
            namespace=DEFAULT_TRACKER_NAMESPACE,
            endpoint=host,
            emitter_config=emitter_config,
        )
        self.user_id = None
        self.user_attributes = None

    def track(self, event_name: str, event_payload: dict):
        """
        Tracks a custom event.

        Args:
            event_name (str): Name of the event.
            event_payload (dict): Event data payload.
        """
        self_desc_json = SelfDescribingJson(
            SCHEMAS["custom_event"], {"name": event_name, "props": event_payload}
        )

        track_arguments = {"event_json": self_desc_json}
        self.__set_user_data(track_arguments)

        self.tracker.track_self_describing_event(**track_arguments)

    def identify(self, user_id, user_attributes=None):
        """
        Identifies the user with given ID and attributes.
        """
        self.user_id = user_id
        if not user_attributes:
            return

        self.user_attributes = user_attributes

    def __set_user_data(self, track_arguments: dict):
        self.__set_user_id()
        self.__set_user_context(track_arguments)

    def __set_user_id(self):
        if not self.user_id:
            return

        subject = Subject()
        subject.set_user_id(self.user_id)
        self.tracker.set_subject(subject)

    def __set_user_context(self, track_arguments: dict):
        if not self.user_attributes:
            return

        user_context = SelfDescribingJson(SCHEMAS["user_context"], self.user_attributes)
        track_arguments["context"] = [user_context]
