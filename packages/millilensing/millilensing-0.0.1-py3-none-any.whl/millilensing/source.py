import numpy as np
import bilby

GCSM = 2.47701878*1.98892*10**(-6)


def PML_waveform(frequency_array,
                 mass_1,
                 mass_2,
                 luminosity_distance,
                 a_1,
                 tilt_1,
                 phi_12,
                 a_2,
                 tilt_2,
                 phi_jl,
                 theta_jn,
                 phase,
                 MLz,
                 yL,
                 **kwargs):

    frequency_domain_source_model = bilby.gw.source.lal_binary_black_hole

    # unlensed waveform
    waveform = frequency_domain_source_model(frequency_array, mass_1, mass_2,
                                            luminosity_distance, a_1, tilt_1, phi_12,
                                            a_2, tilt_2, phi_jl, theta_jn, phase)
    hp = waveform['plus']
    hc = waveform['cross']

    # Amplification function
    # See Takahashi eq. 18
    def F(f, MLz, yL):
        mup = 0.5 + (2+yL**2)/(2*yL*np.sqrt(4+yL**2))
        mum = 0.5 - (2+yL**2)/(2*yL*np.sqrt(4+yL**2))
        w = 4*MLz*2*np.pi*f*GCSM
        del_T = yL*np.sqrt(4+yL**2)/2 + np.log((np.sqrt(4+yL**2)+yL)/(np.sqrt(4+yL**2)-yL))

        F_geo = np.abs(mup)**(0.5) - 1j*np.exp(1j*w*del_T)*np.abs(mum)**(0.5)
        return F_geo

    # lens the waveform
    amplification = F(frequency_array, MLz, yL)
    hp_lensed = hp * amplification
    hc_lensed = hc * amplification

    lensed_waveform = {}
    lensed_waveform['plus'] = hp_lensed
    lensed_waveform['cross']= hc_lensed

    return lensed_waveform

def binary_black_hole_millilens_two_images(frequency_array,
                       mass_1,
                       mass_2,
                       luminosity_distance,
                       a_1,
                       tilt_1,
                       phi_12,
                       a_2,
                       tilt_2,
                       phi_jl,
                       theta_jn,
                       phase,
                       dL2,
                       t2,
                       n1,
                       n2,
                       **kwargs):

    frequency_domain_source_model = bilby.gw.source.lal_binary_black_hole

    # unlensed waveform
    waveform = frequency_domain_source_model(frequency_array,
                                             mass_1,
                                             mass_2,
                                             luminosity_distance,
                                             a_1,
                                             tilt_1,
                                             phi_12,
                                             a_2,
                                             tilt_2,
                                             phi_jl,
                                             theta_jn,
                                             phase,
                                             **kwargs)
    hp = waveform['plus']
    hc = waveform['cross']

    # Amplification function
    def F(f, luminosity_distance, dL2, t2, n1, n2):
        w = 1j*2*np.pi*f
        #F_geo = np.sqrt(mu1)*(np.exp(w*t1-1j*n1*np.pi)) + np.sqrt(mu2)*(np.exp(w*t2-1j*n2*np.pi))
        F_geo = np.exp(-1j*n1*np.pi) + (luminosity_distance/dL2)*(np.exp(w*t2-1j*n2*np.pi))
        return F_geo

    f = frequency_array

    # lens the waveform
    hp_lensed = hp*F(f, luminosity_distance, dL2, t2, n1, n2)
    hc_lensed = hc*F(f, luminosity_distance, dL2, t2, n1, n2)
    lensed_waveform = {}
    lensed_waveform['plus'] = hp_lensed
    lensed_waveform['cross']= hc_lensed
    return lensed_waveform

def binary_black_hole_millilens_four_images(frequency_array,
                                  mass_1,
                                  mass_2,
                                  luminosity_distance,
                                  a_1,
                                  tilt_1,
                                  phi_12,
                                  a_2,
                                  tilt_2,
                                  phi_jl,
                                  theta_jn,
                                  phase,
                                  dL2,
                                  dL3,
                                  dL4,
                                  t2,
                                  dt3,
                                  dt4,
                                  n1,
                                  n2,
                                  n3,
                                  n4,
                                  **kwargs):

    frequency_domain_source_model = bilby.gw.source.lal_binary_black_hole

    # unlensed waveform
    waveform = frequency_domain_source_model(frequency_array,
                                            mass_1,
                                            mass_2,
                                            luminosity_distance,
                                            a_1,
                                            tilt_1,
                                            phi_12,
                                            a_2,
                                            tilt_2,
                                            phi_jl,
                                            theta_jn,
                                            phase,
                                            **kwargs)

    hp = waveform['plus']
    hc = waveform['cross']

    def F(f, luminosity_distance, dL2, dL3, dL4, t2, dt3, dt4, n1, n2, n3, n4):
        w = 1j*2*np.pi*f
        F_geo = np.exp(-1j*n1*np.pi) + (luminosity_distance/dL2)*(np.exp(w*t2-1j*n2*np.pi))\
                + (luminosity_distance/dL3)*(np.exp(w*(t2+dt3)-1j*n3*np.pi))\
                +(luminosity_distance/dL4)*(np.exp(w*(t2+dt4)-1j*n4*np.pi))
        return F_geo

    f = frequency_array

    # lens the waveform
    hp_lensed = hp*F(f, luminosity_distance, dL2, dL3, dL4, t2, dt3, dt4, n1, n2, n3, n4)
    hc_lensed = hc*F(f, luminosity_distance, dL2, dL3, dL4, t2, dt3, dt4, n1, n2, n3, n4)

    lensed_waveform = {}
    lensed_waveform['plus'] = hp_lensed
    lensed_waveform['cross'] = hc_lensed
    return lensed_waveform


def binary_black_hole_millilens_three_images(frequency_array,
                                   mass_1,
                                   mass_2,
                                   luminosity_distance,
                                   a_1,
                                   tilt_1,
                                   phi_12,
                                   a_2,
                                   tilt_2,
                                   phi_jl,
                                   theta_jn,
                                   phase,
                                   dL2,
                                   dL3,
                                   t2,
                                   dt3,
                                   n1,
                                   n2,
                                   n3,
                                   **kwargs):

    frequency_domain_source_model = bilby.gw.source.lal_binary_black_hole

    waveform = frequency_domain_source_model(frequency_array,
                                             mass_1,
                                             mass_2,
                                             luminosity_distance,
                                             a_1,
                                             tilt_1,
                                             phi_12,
                                             a_2,
                                             tilt_2,
                                             phi_jl,
                                             theta_jn,
                                             phase,
                                             **kwargs)
    hc = waveform['cross']
    hp = waveform['plus']

    def F(f, luminosity_distance, dL2, dL3, t2, dt3, n1, n2, n3):
        w = 1j*2*np.pi*f
        # first run of 3 images:
        #  F_geo = 1 + np.sqrt(mu1)*(np.exp(w*t1-1j*0.5*np.pi)) + np.sqrt(mu2)*(np.exp(w*t2-1j*0.5*np.pi))
        F_geo = np.exp(-1j*n1*np.pi) + (luminosity_distance/dL2)*(np.exp(w*t2-1j*n2*np.pi)) + (luminosity_distance/dL3)*(np.exp(w*(t2+dt3)-1j*n3*np.pi))
        return F_geo

    f = frequency_array

    hp_lensed = hp*F(f, luminosity_distance, dL2, dL3, t2, dt3, n1, n2, n3)
    hc_lensed = hc*F(f, luminosity_distance, dL2, dL3, t2, dt3, n1, n2, n3)
    lensed_waveform ={}
    lensed_waveform['plus'] = hp_lensed
    lensed_waveform['cross'] = hc_lensed
    return lensed_waveform

### Multi image waveform ###

from millilensing import MAX_KMAX

def amplification(f,luminosity_distance, dL, dt, n, n1):
    w = 1j*2*np.pi*f
    F_geo = np.exp(-1j*n1*np.pi) + np.sum((luminosity_distance/dL)*(np.exp(np.outer(w, dt)-1j*n*np.pi)), axis=1)
    return F_geo


for Kmax in range(1, MAX_KMAX+1):
    exec('''def multi_image_%i(frequency_array, mass_1, mass_2, luminosity_distance,
	a_1, tilt_1, phi_12, a_2, tilt_2, phi_jl, theta_jn, phase, K, n1, %s **kwargs):


    frequency_domain_source_model = bilby.gw.source.lal_binary_black_hole

    # unlensed waveform
    waveform = frequency_domain_source_model(frequency_array, mass_1, mass_2,
                                            luminosity_distance, a_1, tilt_1, phi_12,
                                            a_2, tilt_2, phi_jl, theta_jn, phase, **kwargs)
    hp = waveform['plus']
    hc = waveform['cross']

    K = int(K)
    dL = np.array([%s])[:K-1]
    dt = np.cumsum([%s])[:K-1]
    n = np.array([%s])[:K-1]

    if K == 1:
        F_geo = np.exp(-1j*n1*np.pi)
    else:
        F_geo = amplification(frequency_array, luminosity_distance, dL, dt, n, n1)

    hp_lensed = hp*F_geo
    hc_lensed = hc*F_geo

    lensed_waveform = {}
    lensed_waveform['plus'] = hp_lensed
    lensed_waveform['cross']= hc_lensed
    return lensed_waveform '''%(Kmax , " ".join(["dL%i,dt%i,n%i,"%(i,i,i) for i in range(2, Kmax+1)]), ' '.join(["dL%i,"%(i) for i in range(2, Kmax+1)]),
                               ' '.join(["dt%i,"%(i) for i in range(2, Kmax+1)]), ' '.join(["n%i,"%(i) for i in range(2, Kmax+1)])))

### function to compute amplification factor with varying number of millisignals

for Kmax in range(1, MAX_KMAX+1):
    exec('''def amplification_%i(frequency_array, K, luminosity_distance, n1, %s **kwargs):

    w = 1j*2*np.pi*frequency_array

    K = int(K)
    dL = np.array([%s])[:K-1]
    dt = np.cumsum([%s])[:K-1]
    n = np.array([%s])[:K-1]

    if K == 1:
        F_geo = np.exp(-1j*n1*np.pi)
    else:
        F_geo = np.exp(-1j*n1*np.pi) + np.sum((luminosity_distance/dL)*(np.exp(np.outer(w, dt)-1j*n*np.pi)), axis=1)

    return F_geo'''%(Kmax, " ".join(["dL%i,dt%i,n%i,"%(i,i,i) for i in range(2, Kmax+1)]), ' '.join(["dL%i,"%(i) for i in range(2, Kmax+1)]),
                               ' '.join(["dt%i,"%(i) for i in range(2, Kmax+1)]), ' '.join(["n%i,"%(i) for i in range(2, Kmax+1)])))
