from abc import ABC, abstractmethod


class Phone(ABC):
    def __init__(self, model: str):
        self.model = model

    @property
    @abstractmethod
    def power(self):
        ...

    @abstractmethod
    def call_target(self, name: str):
        ...


class iBanana(Phone):
    def __init__(self, model: str):
        super().__init__(model)

    @property
    def power(self):
        return '50% battery remaining'

    def call_target(self, name: str):
        raise NotImplementedError('Code missing.')


ibanana = iBanana('iBanana')
print(ibanana.power)
ibanana.call_target('Luigi')
