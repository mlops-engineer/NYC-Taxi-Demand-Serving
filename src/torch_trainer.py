import torch.nn as nn


class TabularModel(nn.Module):
    def __init__(self, n_cont, out_sz, layers, p=0.5):
        super().__init__()
        self.emb_drop = nn.Dropout(p)
        self.bn_cont = nn.BatchNorm1d(n_cont)

        layerlist = []

        for i in layers:
            layerlist.append(nn.Linear(n_cont, i))
            layerlist.append(nn.ReLU(inplace=True))
            layerlist.append(nn.BatchNorm1d(i))
            layerlist.append(nn.Dropout(p))
            n_cont = i
        layerlist.append(nn.Linear(layers[-1], out_sz))

        self.layers = nn.Sequential(*layerlist)

    def forward(self, x_cont):
        x_cont = self.emb_drop(x_cont)

        x_cont = self.bn_cont(x_cont)
        x_cont = self.layers(x_cont)
        return x_cont
