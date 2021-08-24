import requests

search_url = "https://musescore.com/score/comment/view/index?page=1&score_id=5926072"

def get_best_comment():
    r = requests.get(search_url, timeout=5)
    data = r.json()
    max_likes = 0
    temp = None
    me_commented_ids = set()
    for sub in data["info"]["comments"]:
        # is_liked = True can't be checked because the way request works, it's not seeing the same json that I see
        # when I login - i.e. a random user can't delete comments on my score, unless they log into my account. 
        # so instead, check the parent id to filter out the highest liked that I've replied to
        if sub["user_name"] == "TheTallJerry" and int(sub["parent_id"]) > 0:
            me_commented_ids.add(int(sub["parent_id"]))
    for sub in data["info"]["comments"]:
        if int(sub["id"]) in me_commented_ids and int(sub["likes_count"]) > max_likes:
            max_likes = int(sub["likes_count"])
            temp = sub
    return None if not temp else ("T-square", temp["user"]["name"], temp["date"], temp["html"])