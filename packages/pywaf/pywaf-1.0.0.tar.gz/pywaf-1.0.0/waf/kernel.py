import numpy as np


class AtomicKernel:
    @classmethod
    def ft_up(cls, t: float, nprod: int = 10) -> float:
        """ Fourier transform of atomic function \mathrm{up}{(x)}

        :param t: real scalar or array
        :param nprod: integer scalar, nprod=10 by default, 
        nprod>=5 for appropriate computation
        """
        if nprod < 1:
            raise Exception('nprod must be greater than 1')

        t = np.atleast_1d(t)
        p = np.power.outer(2, np.linspace(1, nprod, nprod))  # 2^p sinc(t/2^p)
        out = np.prod(np.sinc(np.divide.outer(t, p)/np.pi), axis=1)
        return out

    @classmethod
    def up(cls, x: float, nsum: int = 100, nprod: int = 10) -> float:
        """ Fourier series of atomic function \mathrm{up}{(x)}

        :param x: real scalar or array
        :param nsum: integer scalar, nsum=100 by default
        :param nprod: integer scalar, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        if nprod < 1:
            raise Exception('nprod must be greater than 0')
        if nsum < 1:
            raise Exception('nsum must be greater than 0')

        x = np.atleast_1d(x)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_up(np.pi*idx, nprod)
        out = .5 + \
            np.sum(coeff*np.cos(np.pi*np.multiply.outer(x, idx)), axis=1)
        return np.where(np.abs(x) <= 1., out, .0)

    @classmethod
    def up_deriv(cls, x: float, nsum: int = 100, nprod: int = 10) -> float:
        """ Fourier series of atomic function \mathrm{up}{(x)} 1st derivation

        :param x: real scalar or array
        :param nsum: integer scalar, nsum=100 by default
        :param nprod: integer scalar, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        if nprod < 1:
            raise Exception('nprod must be greater than 0')
        if nsum < 1:
            raise Exception('nsum must be greater than 0')
        x = np.atleast_1d(x)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_up(np.pi*idx, nprod)
        out = -np.pi*np.sum(idx*coeff*np.sin(np.pi *
                            np.multiply.outer(x, idx)), axis=1)
        return np.where(np.abs(x) <= 1., out, 0.)

    @classmethod
    def ft_upm(cls, t, m=1, nprod=10):
        """ Fourier transform of atomic function \mathrm{up}_m{(x)}

        :param t: real scalar or array
        :param m: integer scalar, m=1 by default
        m>=1 for appropriate computation
        :param nprod: integer scalar, nprod=10 by default, 
        nprod>=5 for appropriate computation
        """
        t = np.atleast_1d(t)
        p = np.power.outer(2*m, np.linspace(1, nprod, nprod))
        numerator = np.power(np.sinc(np.divide.outer(m*t, p)/np.pi), 2)
        denominator = np.sinc(np.divide.outer(t, p)/np.pi)
        return np.prod(numerator/denominator, axis=1)

    @classmethod
    def upm(cls, x, m=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{up}_m{(x)}

        :param x: real scalar or array
        :param m: integer scalar, m=1 by default,
        m>=1 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default,
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        x = np.atleast_1d(x)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_upm(np.pi*idx, m, nprod)
        out = .5 + \
            np.sum(coeff*np.cos(np.pi*np.multiply.outer(x, idx)), axis=1)
        return np.where(np.abs(x) <= 1., out, .0)

    @classmethod
    def upm_deriv(cls, x, m=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{up}_m{(x)} 1st derivation

        :param x: real scalar or array
        :param m: integer scalar, m=1 by default,
        m>=1 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        x = np.atleast_1d(x)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_upm(np.pi*idx, m, nprod)
        out = -np.pi*np.sum(idx*coeff*np.sin(np.pi *
                            np.multiply.outer(x, idx)), axis=1)
        return np.where(np.abs(x) <= 1., out, 0.)

    @classmethod
    def ft_ha(cls, t, a=2, nprod=10):
        """ Fourier transform of atomic function \mathrm{h}_a{(x)}

        :param t: real scalar or array
        :param a: real scalar, a=2 by default,
        a>1 for appropriate computation
        :param nprod: integer, nprod=10 by default, 
        nprod>=5 for appropriate computation
        """
        t = np.atleast_1d(t)
        p = np.power.outer(a, np.linspace(1, nprod, nprod))
        return np.prod(np.sinc(np.divide.outer(t, p)/np.pi), axis=1)

    @classmethod
    def ha(cls, x, a=2, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{h}_a{(x)}

        :param x: real scalar or array
        :param a: real scalar, a=2 by default,
        a>1 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default,
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        mlt = a-1
        x = np.atleast_1d(x)
        x = np.where(np.abs(x) <= 1./mlt, x, 1./mlt)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_ha(mlt*np.pi*idx, a, nprod)
        return mlt*(.5 + np.sum(coeff*np.cos(np.pi*np.multiply.outer(mlt*x, idx)), axis=1))

    @classmethod
    def ha_deriv(cls, x, a=2, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{h}_a{(x)} 1st derivation

        :param x: real scalar or array
        :param a: real scalar, a=2 by default,
        a>1 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        mlt = a-1
        x = np.atleast_1d(x)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_ha(mlt*np.pi*idx, a, nprod)
        out = -np.pi*np.sum(idx*coeff*np.sin(np.pi *
                            np.multiply.outer(mlt*x, idx)), axis=1)
        return np.where(np.abs(x) <= 1./mlt, out, .0)

    @classmethod
    def ft_xin(cls, t, n=1, nprod=10):
        """ Fourier transform of atomic function \mathrm{xi}_n{(x)}

        :param t: real scalar or array
        :param n: integer scalar, n=1 by default,
        n>=1 for appropriate computation
        :param nprod: integer, nprod=10 by default, 
        nprod>=5 for appropriate computation
        """
        t = np.atleast_1d(t)
        p = np.power.outer(n+1, np.linspace(1, nprod, nprod))
        tmp = np.power(np.sinc(np.divide.outer(t, p)/np.pi), n)
        return np.prod(tmp, axis=1)

    @classmethod
    def xin(cls, x, n=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{xi}_n{(x)}

        :param x: real scalar or array
        :param n: integer scalar, n=1 by default,
        n>=1 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default,
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        x = np.atleast_1d(x)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_xin(np.pi*idx, n, nprod)
        out = .5 + \
            np.sum(coeff*np.cos(np.pi*np.multiply.outer(x, idx)), axis=1)
        return np.where(np.abs(x) <= 1., out, .0)

    @classmethod
    def xin_deriv(cls, x, n=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{xi}_n{(x)} 1st derivation

        :param x: real scalar or array
        :param n: integer scalar, n=1 by default,
        n>=1 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        x = np.atleast_1d(x)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_xin(np.pi*idx, n)
        out = -np.pi*np.sum(idx*coeff*np.sin(np.pi *
                            np.multiply.outer(x, idx)), axis=1)
        return np.where(np.abs(x) <= 1., out, .0)

    @classmethod
    def ft_fupn(cls, t, n=1, nprod=10):
        """ Fourier transform of atomic function \mathrm{fup}_n{(x)}

        :param t: real scalar or array
        :param n: integer scalar, n=1 by default,
        n>=0 for appropriate computation
        :param nprod: integer, nprod=10 by default, 
        nprod>=5 for appropriate computation
        """
        t = np.atleast_1d(t)
        p = np.power.outer(2, np.linspace(1, nprod, nprod))  # 2^p sinc(t/2^p)
        mult01 = np.power(np.sinc(0.5*t/np.pi), n)
        mult02 = np.prod(np.sinc(np.divide.outer(t, p)/np.pi), axis=1)
        return np.multiply(mult01, mult02)

    @classmethod
    def fupn(cls, x, n=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{fup}_n{(x)}

        :param x: real scalar or array
        :param n: integer scalar, n=1 by default,
        n>=0 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default,
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        x = np.atleast_1d(x)
        mlt = 2./(n+2)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_fupn(mlt*np.pi*idx, n,  nprod)
        out = mlt*(.5 + np.sum(coeff*np.cos(mlt*np.pi *
                                            np.multiply.outer(x, idx)), axis=1))
        return np.where(np.abs(x) <= 1./mlt, out, .0)

    @classmethod
    def fupn_deriv(cls, x, n=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{fup}_n{(x)} 1st derivation

        :param x: real scalar or array
        :param n: integer scalar, n=1 by default,
        n>=0 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        x = np.atleast_1d(x)
        mlt = 2./(n+2)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_fup(mlt*np.pi*idx, n,  nprod)
        out = -np.pi*np.sum(idx*coeff*np.sin(mlt*np.pi *
                            np.multiply.outer(x, idx)), axis=1)
        return np.where(np.abs(x) <= 1./mlt, out, .0)

    @classmethod
    def ft_chan(cls, t, a=2, n=1, nprod=10):
        """ Fourier transform of atomic function \mathrm{ch}_{a,n}{(x)}

        :param t: real scalar or array
        :param a: real scalar, a=2 by default,
        a>1 for appropriate computation        
        :param n: integer scalar, n=1 by default,
        n>=1 for appropriate computation
        :param nprod: integer, nprod=10 by default, 
        nprod>=5 for appropriate computation
        """
        t = np.atleast_1d(t)
        p = np.power.outer(a, np.linspace(1, nprod, nprod))
        return np.prod(np.power(np.sinc(np.divide.outer(t, p)/np.pi), n), axis=1)

    @classmethod
    def chan(cls, x, a=2, n=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{ch}_{a,n}{(x)}

        :param x: real scalar or array
        :param a: real scalar, a=2 by default,
        a>1 for appropriate computation               
        :param n: integer scalar, n=1 by default,
        n>=1 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default,
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        mlt = (a-1)/n
        x = np.atleast_1d(x)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_chan(mlt*np.pi*idx, a, n, nprod)
        out = mlt * \
            (.5 + np.sum(coeff*np.cos(np.pi*np.multiply.outer(mlt*x, idx)), axis=1))
        return np.where(np.abs(x) <= 1./mlt, out, .0)

    @classmethod
    def chan_deriv(cls, x, a=2, n=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{ch}_{a,n}{(x)} 1st derivation

        :param x: real scalar or array
        :param a: real scalar, a=2 by default,
        a>1 for appropriate computation     
        :param n: integer scalar, n=1 by default,
        n>=1 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        mlt = (a-1)/n
        x = np.atleast_1d(x)
        x = np.where(np.abs(x) <= 1./mlt, x, 1./mlt)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_chan(mlt*np.pi*idx, a, n, nprod)
        out = -np.pi*np.sum(idx*coeff*np.sin(np.pi *
                            np.multiply.outer(mlt*x, idx)), axis=1)
        return np.where(np.abs(x) <= 1./mlt, out, .0)

    @classmethod
    def ft_fipan(cls, t, a=2, n=1, nprod=10):
        """ Fourier transform of atomic function \mathrm{fip}_{a,n}{(x)}

        :param t: real scalar or array
        :param a: real scalar, a=2 by default,
        a>1 for appropriate computation        
        :param n: integer scalar, n=1 by default,
        n>=0 for appropriate computation
        :param nprod: integer, nprod=10 by default, 
        nprod>=5 for appropriate computation
        """
        t = np.atleast_1d(t)
        p = np.power.outer(a, np.linspace(1, nprod, nprod))
        mult01 = np.power(np.sinc(0.5*t/np.pi), n)
        mult02 = np.prod(np.sinc(np.divide.outer(t, p)/np.pi), axis=1)
        return np.multiply(mult01, mult02)

    @classmethod
    def fipan(cls, x, a=2, n=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{fip}_{a,n}{(x)}

        :param x: real scalar or array
        :param a: real scalar, a=2 by default,
        a>1 for appropriate computation               
        :param n: integer scalar, n=1 by default,
        n>=0 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default,
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        l = n + 2./(a-1.)
        mlt = 2./l
        x = np.atleast_1d(x)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_fipan(mlt*np.pi*idx, a, n,  nprod)
        out = mlt * \
            (.5 + np.sum(coeff*np.cos(np.pi*np.multiply.outer(mlt*x, idx)), axis=1))
        return np.where(np.abs(x) <= 1./mlt, out, .0)

    @classmethod
    def fipan_deriv(cls, x, a=2, n=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{fip}_{a,n}{(x)} 1st derivation

        :param x: real scalar or array
        :param a: real scalar, a=2 by default,
        a>1 for appropriate computation     
        :param n: integer scalar, n=1 by default,
        n>=0 for appropriate computation  
        :param nsum:  nsum is an integer, nsum=100 by default
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        l = n + 2./(a-1.)
        mlt = 2./l
        x = np.atleast_1d(x)
        x = np.where(np.abs(x) <= 1./mlt, x, 1./mlt)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_fipan(mlt*np.pi*idx, a, n,  nprod)
        out = -np.pi*np.sum(idx*coeff*np.sin(np.pi *
                            np.multiply.outer(mlt*x, idx)), axis=1)
        return np.where(np.abs(x) <= 1./mlt, out, .0)

    @classmethod
    def ft_fpmn(cls, t, m=2, n=1, nprod=10):
        """ Fourier transform of atomic function \mathrm{fp}_{m,n}{(x)}

        :param t: real scalar or array
        :param m: integer scalar, m=2 by default,
        m>=1 for appropriate computation        
        :param n: integer scalar, n=1 by default,
        n>=0 for appropriate computation
        :param nprod: integer, nprod=10 by default, 
        nprod>=5 for appropriate computation
        """
        t = np.atleast_1d(t)
        p = np.power.outer(2, np.linspace(1, nprod, nprod))
        mult01 = np.power(np.sinc(0.5*t/np.pi), n)
        return np.multiply(mult01, cls.ft_upm(t, m, nprod))

    @classmethod
    def fpmn(cls, x, m=2, n=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{fp}_{m,n}{(x)}

        :param x: real scalar or array
        :param m: integer scalar, m=2 by default,
        m>=1 for appropriate computation               
        :param n: integer scalar, n=1 by default,
        n>=0 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default,
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        mlt = 2./(n+2)
        x = np.atleast_1d(x)
        x = np.where(np.abs(x) <= 1./mlt, x, 1./mlt)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_fpmn(mlt*np.pi*idx, m, n, nprod)
        out = mlt * \
            (.5 + np.sum(coeff*np.cos(np.pi*np.multiply.outer(mlt*x, idx)), axis=1))
        return np.where(np.abs(x) <= 1./mlt, out, .0)

    @classmethod
    def fpmn_deriv(cls, x, m=2, n=1, nsum=100, nprod=10):
        """ Fourier series of atomic function \mathrm{fp}_{m,n}{(x)} 1st derivation

        :param x: real scalar or array
        :param m: integer scalar, m=2 by default,
        m>=1 for appropriate computation        
        :param n: integer scalar, n=1 by default,
        n>=0 for appropriate computation
        :param nsum:  nsum is an integer, nsum=100 by default
        :param nprod:  nprod is an integer, nprod=10 by default,
        nprod>=5 for appropriate computation
        """
        mlt = 2./(n+2)
        x = np.atleast_1d(x)
        x = np.where(np.abs(x) <= 1./mlt, x, 1./mlt)
        idx = np.linspace(1, nsum, nsum)
        coeff = cls.ft_fpmn(mlt*np.pi*idx, m, n, nprod)
        out = -np.pi*np.sum(idx*coeff*np.sin(np.pi *
                            np.multiply.outer(mlt*x, idx)), axis=1)
        return np.where(np.abs(x) <= 1./mlt, out, .0)
