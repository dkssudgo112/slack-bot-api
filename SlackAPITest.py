import RnDSlackAPI


if __name__ == "__main__":
    token = ""
    slack = RnDSlackAPI.SlackAPI(token)

    channel_name = "99_센터필드에도사람있어요"
    query = "점메추"
    text = "저녁 추천 드렸습니다"

    result = slack.post_just_message("C023EDBHQ79", "good" )