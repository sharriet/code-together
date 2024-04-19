from models.topiclist import TopicList

# test the get_topics method of the TopicList class

def test_get_topics():
    tl = TopicList()
    # should return a list
    assert isinstance(tl.get_topics(), list)
    # number of topics should be > 0
    assert len(tl.get_topics()) > 0
    # topics should have a title attribute
    assert tl.get_topics()[0]["title"]