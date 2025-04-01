class laptop_2500(): #class definition 
    brand_name = "HP" #attributes
    color = "Silver"
    storage = "256GB"
    def whats_app_calling(self):
        print("you are calling by whats app application in laptop",self.brand_name)
    def browsing(self):
        print("you are browsing internet in laptap ",self.brand_name)
    def video_player(self):
        print(f"you are watching a video from {self.brand_name} storage containing {self.storage}")
    def gaming(self):
        print(f"you are playing video games from {self.brand_name} storage containing {self.storage} ")
    def coding(self):
        print(f"you are coding daily python excerises and tasks from {self.brand_name} storage containing {self.storage} ")
#objname = classname()
obj = laptop_2500()
obj.whats_app_calling()
obj.browsing()
obj.video_player()
obj.gaming()
obj.coding()