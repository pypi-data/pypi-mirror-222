import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.utils import spectral_norm

# Copyright (c) 2019, Adobe Inc. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
# 4.0 International Public License. To view a copy of this license, visit
# https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.

import torch
import torch.nn.parallel
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
# https://github.com/adobe/antialiased-cnns/blob/d4bf038a24cb2cdeae721ccaeeb1bd0c81c8dff7/antialiased_cnns/blurpool.py
class BlurPool(nn.Module):
    def __init__(self, channels, pad_type='reflect', filt_size=4, stride=2, pad_off=0):
        super(BlurPool, self).__init__()
        self.filt_size = filt_size
        self.pad_off = pad_off
        self.pad_sizes = [int(1.*(filt_size-1)/2), int(np.ceil(1.*(filt_size-1)/2)), int(1.*(filt_size-1)/2), int(np.ceil(1.*(filt_size-1)/2))]
        self.pad_sizes = [pad_size+pad_off for pad_size in self.pad_sizes]
        self.stride = stride
        self.off = int((self.stride-1)/2.)
        self.channels = channels

        if(self.filt_size==1):
            a = np.array([1.,])
        elif(self.filt_size==2):
            a = np.array([1., 1.])
        elif(self.filt_size==3):
            a = np.array([1., 2., 1.])
        elif(self.filt_size==4):    
            a = np.array([1., 3., 3., 1.])
        elif(self.filt_size==5):    
            a = np.array([1., 4., 6., 4., 1.])
        elif(self.filt_size==6):    
            a = np.array([1., 5., 10., 10., 5., 1.])
        elif(self.filt_size==7):    
            a = np.array([1., 6., 15., 20., 15., 6., 1.])

        filt = torch.Tensor(a[:,None]*a[None,:])
        filt = filt/torch.sum(filt)
        self.register_buffer('filt', filt[None,None,:,:].repeat((self.channels,1,1,1)))

        self.pad = get_pad_layer(pad_type)(self.pad_sizes)

    def forward(self, inp):
        if(self.filt_size==1):
            if(self.pad_off==0):
                return inp[:,:,::self.stride,::self.stride]    
            else:
                return self.pad(inp)[:,:,::self.stride,::self.stride]
        else:
            return F.conv2d(self.pad(inp), self.filt, stride=self.stride, groups=inp.shape[1])

def get_pad_layer(pad_type):
    if(pad_type in ['refl','reflect']):
        PadLayer = nn.ReflectionPad2d
    elif(pad_type in ['repl','replicate']):
        PadLayer = nn.ReplicationPad2d
    elif(pad_type=='zero'):
        PadLayer = nn.ZeroPad2d
    else:
        print('Pad type [%s] not recognized'%pad_type)
    return PadLayer

class BlurPool1D(nn.Module):
    def __init__(self, channels, pad_type='reflect', filt_size=3, stride=2, pad_off=0):
        super(BlurPool1D, self).__init__()
        self.filt_size = filt_size
        self.pad_off = pad_off
        self.pad_sizes = [int(1. * (filt_size - 1) / 2), int(np.ceil(1. * (filt_size - 1) / 2))]
        self.pad_sizes = [pad_size + pad_off for pad_size in self.pad_sizes]
        self.stride = stride
        self.off = int((self.stride - 1) / 2.)
        self.channels = channels

        # print('Filter size [%i]' % filt_size)
        if(self.filt_size == 1):
            a = np.array([1., ])
        elif(self.filt_size == 2):
            a = np.array([1., 1.])
        elif(self.filt_size == 3):
            a = np.array([1., 2., 1.])
        elif(self.filt_size == 4):
            a = np.array([1., 3., 3., 1.])
        elif(self.filt_size == 5):
            a = np.array([1., 4., 6., 4., 1.])
        elif(self.filt_size == 6):
            a = np.array([1., 5., 10., 10., 5., 1.])
        elif(self.filt_size == 7):
            a = np.array([1., 6., 15., 20., 15., 6., 1.])

        filt = torch.Tensor(a)
        filt = filt / torch.sum(filt)
        self.register_buffer('filt', filt[None, None, :].repeat((self.channels, 1, 1)))

        self.pad = get_pad_layer_1d(pad_type)(self.pad_sizes)

    def forward(self, inp):
        if(self.filt_size == 1):
            if(self.pad_off == 0):
                return inp[:, :, ::self.stride]
            else:
                return self.pad(inp)[:, :, ::self.stride]
        else:
            return F.conv1d(self.pad(inp), self.filt, stride=self.stride, groups=inp.shape[1])

def get_pad_layer_1d(pad_type):
    if(pad_type in ['refl', 'reflect']):
        PadLayer = nn.ReflectionPad1d
    elif(pad_type in ['repl', 'replicate']):
        PadLayer = nn.ReplicationPad1d
    elif(pad_type == 'zero'):
        PadLayer = nn.ZeroPad1d
    else:
        print('Pad type [%s] not recognized' % pad_type)
    return PadLayer

class AdaIN(nn.Module):
    def __init__(self, style_dim, num_features):
        super().__init__()
        self.norm = nn.InstanceNorm2d(num_features, affine=False)
        self.fc = nn.Linear(style_dim, num_features*2)

    def forward(self, x, s):
        h = self.fc(s)
        h = h.view(h.size(0), h.size(1), 1, 1)
        gamma, beta = torch.chunk(h, chunks=2, dim=1)
        return (1 + gamma) * self.norm(x) + beta

class Interpolate(nn.Module):
    def __init__(self, scale_factor, mode="bilinear"):
        super(Interpolate, self).__init__()
        self.interp = nn.functional.interpolate
        self.scale_factor = scale_factor
        self.mode = mode
        
    def forward(self, x):
        x = self.interp(x, scale_factor=self.scale_factor, mode=self.mode, align_corners=False)
        return x

#------------------------------------------------------------------------------------------
# ConvBlock
#   1. Upsample / Conv(padding)
#       - padding options : 'zeros'(default), 'reflect', 'replicate' or 'circular'
#       - if you choose upsample option, you have to set stride==1
#   2. Norm
#       - Norm options : 'bn', 'in', 'none'
#   3. activation
#       - activation options : 'relu', 'tanh', 'sig', 'none'
#------------------------------------------------------------------------------------------
class ConvBlock(nn.Module):
    def __init__(self, input_dim ,output_dim, kernel_size=3, stride=2, padding=1, \
        norm_type='bn', act_type='lrelu', transpose=False):
        super(ConvBlock, self).__init__()

        # convolutional layer and upsampling
        if transpose:
            self.up = Interpolate(scale_factor=stride)
            self.conv = nn.Conv2d(input_dim, output_dim, kernel_size, stride=1, padding=padding)
        else:
            self.up = transpose
            self.conv = nn.Conv2d(input_dim, output_dim, kernel_size, stride, padding=padding)
        
        # normalization
        if norm_type == 'bn':
            self.norm = nn.BatchNorm2d(output_dim)
        elif norm_type == 'in':
            self.norm = nn.InstanceNorm2d(output_dim)
        elif norm_type == 'none':
            self.norm = None
        else:
            assert 0, f"Unsupported normalization: {norm_type}"
        
        # activation
        if act_type == 'relu':
            self.act = nn.ReLU()
        elif act_type == 'lrelu':
            self.act = nn.LeakyReLU(0.2)
        elif act_type == 'tanh':
            self.act = nn.Tanh()
        elif act_type == 'sig':
            self.act = nn.Sigmoid()
        elif act_type == 'none':
            self.act = None
        else:
            assert 0, f"Unsupported activation: {act_type}"


    def forward(self, x):
        if self.up:
            x = self.up(x)

        x = self.conv(x)

        if self.norm:
            x = self.norm(x)

        if self.act:
            x = self.act(x)
        return x


class ResBlock(nn.Module):
    def __init__(self, in_c, out_c, scale_factor=1, norm='in', act='lrelu'):
        super(ResBlock, self).__init__()

        self.norm1 = nn.InstanceNorm2d(out_c)
        self.norm2 = nn.InstanceNorm2d(out_c)
        self.activ = nn.LeakyReLU(0.2)
        self.conv1 = nn.Conv2d(in_channels=in_c, out_channels=out_c, kernel_size=3, stride=1, padding=1, bias=False)
        self.conv2 = nn.Conv2d(in_channels=out_c, out_channels=out_c, kernel_size=3, stride=1, padding=1, bias=False)
        self.conv1x1 = nn.Conv2d(in_channels=in_c, out_channels=out_c, kernel_size=1, stride=1, padding=0, bias=False)
        self.resize = Interpolate(scale_factor=scale_factor)

    def forward(self, feat):
        feat1 = self.norm1(feat)
        feat1 = self.activ(feat1)
        feat1 = self.conv1(feat1)
        feat1 = self.resize(feat1)
        feat1 = self.norm2(feat1)
        feat1 = self.activ(feat1)
        feat1 = self.conv2(feat1)

        feat2 = self.conv1x1(feat)
        feat2 = self.resize(feat2)

        return feat1 + feat2


class AdaINResBlock(nn.Module):
    def __init__(self, in_c, out_c, scale_factor=1, style_dim=512):
        super(AdaINResBlock, self).__init__()

        self.AdaIN1 = AdaIN(style_dim, in_c)
        self.AdaIN2 = AdaIN(style_dim, out_c)

        self.activ1 = nn.LeakyReLU(0.2)
        self.activ2 = nn.LeakyReLU(0.2)

        self.conv1 = nn.Conv2d(in_channels=in_c, out_channels=out_c, kernel_size=3, stride=1, padding=1, bias=False)
        self.conv2 = nn.Conv2d(in_channels=out_c, out_channels=out_c, kernel_size=3, stride=1, padding=1, bias=False)
        self.conv1x1 = nn.Conv2d(in_channels=in_c, out_channels=out_c, kernel_size=1, stride=1, padding=0, bias=False)

        self.scale_factor = scale_factor
        self.resize = scale_factor != 1 #@#

    def forward(self, feat, style):

        feat1 = feat
        feat1 = self.AdaIN1(feat1, style)
        feat1 = self.activ1(feat1)
        feat1 = self.conv1(feat1)

        if self.resize:
            feat1 = F.interpolate(feat1, scale_factor=self.scale_factor, mode='bilinear')

        feat1 = self.AdaIN2(feat1, style)
        feat1 = self.activ2(feat1)
        feat1 = self.conv2(feat1)

        # skip connction
        feat2 = feat
        if self.resize:
            feat2 = self.conv1x1(feat2) # chnnel dim
            feat2 = F.interpolate(feat2, scale_factor=self.scale_factor, mode='bilinear') # size

        return feat1 + feat2
    
        

class SNAdaINResBlock(nn.Module):
    def __init__(self, in_c, out_c, scale_factor=1, style_dim=512):
        super(SNAdaINResBlock, self).__init__()

        self.conv1 = spectral_norm(nn.Conv2d(in_channels=in_c, out_channels=out_c, kernel_size=3, stride=1, padding=1, padding_mode='reflect', bias=False))
        self.AdaIN1 = AdaIN(style_dim, out_c)
        self.activ1 = nn.LeakyReLU(0.2)

        self.conv2 = spectral_norm(nn.Conv2d(in_channels=out_c, out_channels=out_c, kernel_size=3, stride=1, padding=1, padding_mode='reflect', bias=False))
        self.AdaIN2 = AdaIN(style_dim, out_c)
        self.activ2 = nn.LeakyReLU(0.2)

        self.conv1x1 = spectral_norm(nn.Conv2d(in_channels=in_c, out_channels=out_c, kernel_size=1, stride=1, padding=0, padding_mode='reflect', bias=False))

        self.scale_factor = scale_factor
        self.resize = scale_factor != 1

    def forward(self, feat, style):

        feat1 = feat
        feat1 = self.conv1(feat1)
        feat1 = self.AdaIN1(feat1, style)
        feat1 = self.activ1(feat1)

        if self.resize:
            feat1 = F.interpolate(feat1, scale_factor=self.scale_factor, mode='bilinear')

        feat1 = self.conv2(feat1)
        feat1 = self.AdaIN2(feat1, style)
        feat1 = self.activ2(feat1)

        # skip connction
        feat2 = feat
        if self.resize:
            feat2 = F.interpolate(feat2, scale_factor=self.scale_factor, mode='bilinear') # size
            feat2 = self.conv1x1(feat2) # chnnel dim

        return feat1 + feat2


class SNConvBlock(nn.Module):
    def __init__(self, input_dim ,output_dim, kernel_size=3, stride=2, padding=1, \
        norm_type='bn', act_type='lrelu', transpose=False):
        super(SNConvBlock, self).__init__()

        # convolutional layer and upsampling
        if transpose:
            self.up = Interpolate(scale_factor=stride)
            self.conv = spectral_norm(nn.Conv2d(input_dim, output_dim, kernel_size, stride=1, padding=padding))
        else:
            self.up = transpose
            self.conv = spectral_norm(nn.Conv2d(input_dim, output_dim, kernel_size, stride, padding=padding))
        
        # normalization
        if norm_type == 'bn':
            self.norm = nn.BatchNorm2d(output_dim)
        elif norm_type == 'in':
            self.norm = nn.InstanceNorm2d(output_dim)
        elif norm_type == 'none':
            self.norm = None
        else:
            assert 0, f"Unsupported normalization: {norm_type}"
        
        # activation
        if act_type == 'relu':
            self.act = nn.ReLU()
        elif act_type == 'lrelu':
            self.act = nn.LeakyReLU(0.2)
        elif act_type == 'tanh':
            self.act = nn.Tanh()
        elif act_type == 'sig':
            self.act = nn.Sigmoid()
        elif act_type == 'none':
            self.act = None
        else:
            assert 0, f"Unsupported activation: {act_type}"


    def forward(self, x):
        if self.up:
            x = self.up(x)

        x = self.conv(x)

        if self.norm:
            x = self.norm(x)

        if self.act:
            x = self.act(x)
        return x