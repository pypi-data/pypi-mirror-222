import torch
import torch.nn as nn


class BaseEncoder(nn.Module):
    @abstractmethod
    def encoder(self) -> nn.Module:
        raise NotImplementedError()
