#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:03:10 2023

@author: twguest
"""

import numpy as np
from scipy.constants import c, e, h


def e2wav(photon_energy):
    """
<<<<<<< HEAD
    Converts photon energy to photon wavelength.
    
    :param photon_energy: photon energy in eV
    
    :returns: photon wavelength in m
=======
    Convert photon energy to corresponding wavelength.
    
    :param photon_energy: float
        The photon energy in appropriate units (e.g., electronvolts).
    
    :return: float
        The corresponding wavelength in appropriate units (e.g., meters or angstroms).
    
    :Note:
        This function uses the Planck's constant (h), speed of light (c), and elementary charge (e)
        to perform the conversion. 
>>>>>>> dev
    """
    return (h * c) / (e * photon_energy)


def e2k(photon_energy):
    """
<<<<<<< HEAD
    Converts photon energy to freq. wavevector
    
    :param photon_energy: photon energy in eV
    
    :returns k: wavevector (1/m)
=======
    Convert photon energy to corresponding wave number.
    
    :param photon_energy: float
        The photon energy in appropriate units (e.g., electronvolts).
    
    :return: float
        The corresponding wave number in appropriate units (e.g., rad/m).
    
    :Note:
        This function uses the `e2wav` function to first convert the photon energy to wavelength
        and then calculates the wave number as (2 * pi) / wavelength.
>>>>>>> dev
    """
    return (np.pi * 2) / e2wav(photon_energy)


def complex_to_wpg(arr): ### converter
    """
    converter function to transform complex wavefield into wpg style electric
    field array
    
    :param arr: complex wavefield array [x,y,t] (complex128 type)
    
    :returns new_arr: wpg style electric field array [nx,ny,nz,2] (float64)
    """
    new_arr = np.zeros([arr.shape[0], arr.shape[1], arr.shape[2], 2])
    new_arr[:,:,:,0] = arr.real
    new_arr[:,:,:,1] = arr.imag
    return new_arr
