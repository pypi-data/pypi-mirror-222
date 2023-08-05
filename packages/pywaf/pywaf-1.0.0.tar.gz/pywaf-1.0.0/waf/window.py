import numpy as np
from .kernel import AtomicKernel as atom

window_list = ['up', 'upm', 'ha',
               'xin', 'fupn', 'chan', 'fipan', 'fpmn']


def normalize(window, mode, npt):
    match mode:
        case 'max':
            return window/np.max(window)
        case 'area':
            return window/np.trapz(window, dx=2./(npt-1))


def up(npt, mode='max'):
    t = np.linspace(-1, 1, npt)
    window = atom.up(t)
    return normalize(window, mode, npt)


def upm(npt, m=2, mode='max'):
    t = np.linspace(-1, 1, npt)
    window = atom.upm(t, m)
    return normalize(window, mode, npt)


def ha(npt, a=2, mode='max'):
    t = np.linspace(-1/(a-1), 1/(a-1), npt)
    window = atom.ha(t, a)
    return normalize(window, mode, npt)


def xin(npt, n=2, mode='max'):
    t = np.linspace(-1, 1, npt)
    window = atom.xin(t, n)
    return normalize(window, mode, npt)


def fupn(npt, n=0, mode='max'):
    t = np.linspace(-(n+2)/2, (n+2)/2, npt)
    window = atom.fupn(t, n)
    return normalize(window, mode, npt)


def chan(npt, a=2, n=2, mode='max'):
    t = np.linspace(-n/(a-1), n/(a-1), npt)
    window = atom.chan(t, a, n)
    return normalize(window, mode, npt)


def fipan(npt, a=2, n=2, mode='max'):
    l = n+2/(a-1)
    t = np.linspace(-l/2, l/2, npt)
    window = atom.fipan(t, a, n)
    return normalize(window, mode, npt)


def fpmn(npt, m=2, n=2, mode='max'):
    t = np.linspace(-(n+2)/2, (n+2)/2, npt)
    window = atom.fpmn(t, m, n)
    return normalize(window, mode, npt)
