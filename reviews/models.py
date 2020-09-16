from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """ Review model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    # 유저정보, 룸 정보가 리뷰와 연결되어 있다. 이 정보들이 지원지면 리뷰도 영향을 받는다.
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"