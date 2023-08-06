import torchvision
import torch
import numpy as np
import cv2
import torchvision.transforms.functional as F
import random

# 按比例将长边缩放至目标尺寸
class Resize1:
    def __init__(self, width):
        self.width = width

    def __call__(self, x):
        if isinstance(torch.Tensor):
            _, h, w = x.shape
            scale = self.width / max(w, h)
            W, H = round(w * scale), round(h * scale)
            x = F.resize(x, [H,W])
            return x
        elif isinstance(np.ndarray):
            h, w, c = x.shape
            scale = self.width / max(w, h)
            W, H = round(scale * w), round(scale * h)
            x = cv2.resize(x, (W, H), interpolation=cv2.INTER_LINEAR)
            return x


class PadSquare:
    def __call__(self, x):
        if isinstance(torch.Tensor):
            _, h, w = x.shape
            width = max(w, h)
            pad_left = round((width - w) / 2.0)
            pad_right = width - w - pad_left
            pad_up = round((width - h) / 2.0)
            pad_down = width - h - pad_up

            x = F.pad(x, [pad_left, pad_up, pad_right, pad_down])
            return x

        elif isinstance(np.ndarray):
            h, w, _ = x.shape
            width = max(w, h)
            pad_left = round((width - w) / 2.0)
            pad_right = width - w - pad_left
            pad_up = round((width - h) / 2.0)
            pad_down = width - h - pad_up

            x = cv2.copyMakeBorder(x, pad_up, pad_down, pad_left, pad_right, cv2.BORDER_CONSTANT, value=0)
            return x

class randomaffine_2img:
    def __init__(self, rotate, transx, transy, scale):
        self.rot_deg = random.uniform(float(rotate[0]), float(rotate[1]))
        self.transx = random.randint(transx[0], transx[1])
        self.transy = random.randint(transy[0], transy[1])
        self.scale = random.uniform(min(scale), max(scale))

    def __call__(self, x1, x2):
        x1 = F.affine(x1, self.rot_deg, [self.transx,self.transy], self.scale, interpolation=F.InterpolationMode.NEAREST)
        x2 = F.affine(x2, self.rot_deg, [self.transx,self.transy], self.scale, interpolation=F.InterpolationMode.NEAREST)
        return x1,x2