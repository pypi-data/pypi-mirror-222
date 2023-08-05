import numpy as np
from .kernel import AtomicKernel


class Wavelet(AtomicKernel):

    def __init__(self, waf, coef=2):
        waf_list = ['up', 'upm', 'meyer4','meyer6']
        if waf not in waf_list:
            raise Exception('waf must be "up", "upm", "meyer4" or "meyer6"')
        self.coef = coef
        self.waf = waf

    def chi(self, x):
        m = self.coef

        def sum(f, x, a, b, m):
            return f(a*x-b, m)+f(a*x, m)+f(a*x+b, m)

        match self.waf:

            case 'up':
                return self.up(x*3/(2*np.pi)+1)+self.up(x*3/(2*np.pi))+self.up(x*3/(2*np.pi)-1)

            case 'upm':
                return sum(self.upm, x, 3/2/np.pi, 1, m)

            case 'meyer4':
                def nu(x):
                    return x**4*(35-84*x+70*x**2-20*x**3)

                chi = []
                for item in x:
                    if np.abs(item) >= 2*np.pi/3 and np.abs(item) <= 4*np.pi/3:
                        chi.append(
                            np.cos(np.pi/2*nu(3/2/np.pi*np.abs(item)-1)))

                    elif np.abs(item) > -2*np.pi/3 and np.abs(item) <= np.pi*2/3:
                        chi.append(1)
                    else:
                        chi.append(0)

                return np.array(chi)**2
            
            case 'meyer6':
                def nu(x):
                    return x**6*(462-1980*x+3465*x**2-3080*x**3+1386*x**4-252*x**5)

                chi = []
                for item in x:
                    if np.abs(item) >= 2*np.pi/3 and np.abs(item) <= 4*np.pi/3:
                        chi.append(
                            np.cos(np.pi/2*nu(3/2/np.pi*np.abs(item)-1)))

                    elif np.abs(item) > -2*np.pi/3 and np.abs(item) <= np.pi*2/3:
                        chi.append(1)
                    else:
                        chi.append(0)

                return np.array(chi)**2
            case _:
                raise Exception('waf must be "up", "upm", "meyer4" or "meyer6"')

    def phi_f(self, x):
        return np.sqrt(np.abs(self.chi(x)))

    def H(self, x):
        n = [-1, 0, 1]
        sum = 0
        for item in n:
            sum += self.phi_f(2*(x-2*np.pi*item))
        return sum

    def dec_lo(self, n):
        w = np.linspace(-np.pi, np.pi, 10000)

        def fourier_series(f, n):
            h = []
            func = f(w)
            for i in n:
                h.append(np.trapz(func*np.exp(1j*w*i), x=w)/(2**0.5*np.pi))
            return np.real(h)

        return fourier_series(self.H, n)

    def rec_lo(self, dec_lo):
        return np.conj(dec_lo[::-1])

    def dec_hi(self, dec_lo, n, N):
        coef = np.power(-np.ones(N), n)
        return coef*dec_lo[::-1]

    def rec_hi(self, dec_lo, n, N):
        coef = np.power(-np.ones(N), n+1)
        return coef*dec_lo

    def filter(self, N):
        n = np.arange(-N//2, N//2)
        dec_lo_mass = self.dec_lo(n)
        dec_hi_mass = self.dec_hi(dec_lo_mass, n, N)
        rec_lo_mass = self.rec_lo(dec_lo_mass)
        rec_hi_mass = self.rec_hi(dec_lo_mass, n, N)

        return {'dec_lo': dec_lo_mass,'dec_hi': dec_hi_mass,'rec_lo': rec_lo_mass,'rec_hi': rec_hi_mass}

    def psi_f(self, w):
        return np.exp(1j*w/2)*(self.phi_f(w-2*np.pi) + self.phi_f(w+2*np.pi))*self.phi_f(w/2)

    def psi(self, x, N=10000):
        w = np.linspace(2*np.pi/3, 8*np.pi/3, N)
        psi = []
        C = self.phi_f(w/2)*self.phi_f(w-2*np.pi)
        for item in x:
            psi.append(np.trapz(C*np.cos(w*(item+0.5)), x=w))
        return np.array(psi)/np.pi

    def phi(self, x, N=10000):
        w = np.linspace(0, 4*np.pi/3, N)
        phi = []
        C = self.phi_f(w)
        for item in x:
            phi.append(np.trapz(C*np.cos(w*item), x=w))
        return np.array(phi)/np.pi