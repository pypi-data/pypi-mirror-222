from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def get_data(self, pulls, res_names):
        pass
