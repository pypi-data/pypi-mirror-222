class Callable():
    def __init__(self, config, blocks):
        self.config = config
        self.blocks = blocks

    def get_blocks(self):
        return self.blocks
    
    def get_config(self):
        return self.config