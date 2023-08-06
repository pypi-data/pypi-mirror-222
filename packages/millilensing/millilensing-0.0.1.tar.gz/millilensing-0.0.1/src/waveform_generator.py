import os
import importlib
from bilby.core.utils import infer_parameters_from_function
from bilby.gw.waveform_generator import WaveformGenerator


class LensedWaveformGenerator(WaveformGenerator):
    def __init__(self, duration=None, sampling_frequency=None, start_time=0, frequency_domain_source_model=None,
                 time_domain_source_model=None, parameters=None, parameter_conversion=None, waveform_arguments=None):
        super().__init__(duration = duration,
                         sampling_frequency = sampling_frequency,
                         start_time = start_time,
                         frequency_domain_source_model = frequency_domain_source_model,
                         time_domain_source_model = time_domain_source_model,
                         parameters = parameters,
                         parameter_conversion = parameter_conversion,
                         waveform_arguments = waveform_arguments)
        lens_model = waveform_arguments["lens_model"]
        lens_model_mod, lens_model_func = os.path.splitext(lens_model)
        lens_model_mod = importlib.import_module(lens_model_mod)
        self.amplification_factor = getattr(lens_model_mod, lens_model_func[1:])
        lens_parameters = infer_parameters_from_function(self.amplification_factor)
        self.source_parameter_keys.update(lens_parameters)
        
    def _strain_from_model(self, model_data_points, model):
        unlensed_waveform = model(model_data_points, **self.parameters)
        amplification_factor = self.amplification_factor(model_data_points, **self.parameters)
        lensed_waveform = {}
        for key, val in unlensed_waveform.items():
            lensed_waveform[key] = val * amplification_factor
        return lensed_waveform
