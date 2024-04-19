import json

class TopicList:
    
    # Instance method
    def get_topics(self):

        f = open("data/topics.json")
        topics = json.load(f)
        return topics