from models.topiclist import TopicList

# test the TopicList class

def test_get_topics_is_list():
    tl = TopicList()
    # get_topics should return a list
    assert isinstance(tl.get_topics(), list)

def test_get_topics_has_title():
    tl = TopicList()
    # a topic should have a title
    assert [i["title"] for i in tl.get_topics()]