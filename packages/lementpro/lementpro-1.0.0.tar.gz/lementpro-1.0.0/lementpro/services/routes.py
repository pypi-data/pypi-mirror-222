from lementpro.builders import Build
from lementpro.data.user import User
from lementpro.sender import Sender


class Routes:
    """Service for working with Routes in UserGate Public API"""

    def button(self, by_user: User, routeInstanceId: str, routeActivityId: str, transitionId: int = None):
        """Trigger route activity button
        :return: Empty result
        """
        request_data = Build(url="/api/routes/{routeInstanceId}/activities/{routeActivityId}/button").post(
            routeInstanceId=routeInstanceId,
            routeActivityId=routeActivityId,
            transitionId=transitionId,
        )
        return Sender().send_request(request_data, by_user=by_user)
