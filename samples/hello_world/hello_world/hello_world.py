from iconservice import *

TAG = 'HelloWorld'

class HelloWorld(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()
    
    @external(readonly=True)
    def name(self) -> str:
        return "HelloWorld"

    @external(readonly=True)
    def hello(self) -> str:
        Logger.info('Hello, world!', TAG)
        return "Hello"
    
