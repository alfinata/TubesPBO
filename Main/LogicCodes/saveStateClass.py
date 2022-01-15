# Save State Class - Din

class saveStateClass:
    def __init__(self, hero, stageProgress, storyProgress):
        self.__hero = hero
        self.__stageProgress = stageProgress
        self.__storyProgress = storyProgress
    
    def setHero(self, hero):
        self.__hero = hero
    
    def getHero(self):
        return self.__hero

    def setStageProgress(self, stageProgress):
        self.__stageProgress = stageProgress

    def getStageProgress(self):
        return self.__stageProgress
    
    def setStoryProgress(self, storyProgress):
        self.__storyProgress = storyProgress

    def getStoryProgress(self):
        return self.__storyProgress