from typing import List

from ..constants import DEFAULT_TRAINING_DATA_PATH
from .logger import logger
from ..datautils.params import ConstavaParameters
from ..io.ensemblereader import EnsembleReader
from ..io.resultswriter import ResultWriter
from ..calc.calculator import ConfStateCalculator
from ..calc.subsampling import SubsamplingBootstrap, SubsamplingWindow
from ..calc.pdfestimators import KDEStatePdf, GridStatePdf


class Constava:
    """Interface class for all functionalities of Constava.

    Methods:
    --------
        set_param(parameter, value)
            Sets a parameters to a given value.
        get_param(parameter) -> value
            Returns the current value of the given parameter
        show_params() -> str
            Returns the current set of parameters as a string
        run()
            Runs Constava with the current parameters
    """

    def __init__(self, parameters: ConstavaParameters = None, **kwargs):
        """Initializes the python interface for Constava. Parameters can be 
        provided as a ConstavaParameters class
        
        Parameters:
        -----------
            parameters : ConstavaParameters
                ConstavaParameters object ontaining all parameters (if provided
                kwargs will be ignored)
            **kwargs :
                To only set individual parameters, those parameters can be 
                provided as keyword arguments. For all other parameters
                default values are used. For a full list of available settings
                and their defaults, check: `help(ConstavaParameters)`
        """
        logger.info("Constava: Initializing python interface...")
        if parameters is None:
            self._parameters = ConstavaParameters(**kwargs)
        else:
            self._parameters = parameters
        self.results = None
        self._calculator = None
        self._calculator_hash = None

    def __repr__(self):
        outstr = "Constava(calculator=Calculator({0}), results={1})".format(
            "None" if self._calculator is None else hex(self._calculator_hash)[:8], 
            repr(self.results))
        return outstr

    def get_param(self, parameter: str):
        """Returns the current value of the given parameter"""
        return getattr(self._parameters, parameter)
        
    def set_param(self, parameter: str, value):
        """Sets a parameters to a given value"""
        logger.debug(f"Constava: Setting parameter: [{parameter}] = {value}")
        setattr(self._parameters, parameter, value)
        logger.debug(f"Constava: New parameters:  {self.show_params()}")

    def show_params(self) -> str:
        """Returns a string with all currently set parameters"""
        return repr(self._parameters)
    
    def run(self) -> None:
        # Initialize an reader for input file(s)
        logger.info("Constava: Initializing reader for input file(s)...")
        reader = self._initialize_reader()
        # Initialize writer for results
        logger.info("Constava: Initializing writer for results...")
        writer = self._initialize_writer()
        # Initialize or load calculator (logged inside function)
        calculator = self._initialize_calculator()
        # Read input files
        input_files = self.get_param("input_files")
        logger.info(f"Constava: Reading dihedrals from files: {input_files}")
        ensemble = reader.readFiles(*input_files)
        # Do the inference
        logger.info("Constava: Starting inference...")
        self.results = calculator.calculate(ensemble)
        logger.info("Constava: done.")
        # Write results
        output_file = self.get_param("output_file")
        writer.writeToFile(self.results, output_file)
    
    def _initialize_reader(self) -> EnsembleReader:
        """Initializes an EnsembleReader"""
        reader = EnsembleReader(
            filetype_str = self.get_param("input_format"), 
            degrees2radians = self.get_param("input_degrees"))
        return reader
    
    def _initialize_writer(self) -> ResultWriter:
        """Initializes a ResultsWriter"""
        if self.get_param("output_file") is None:
            return None
        writer = ResultWriter(
            filetype_str = self.get_param("output_format"),
            float_precision = self.get_param("precision"))
        return writer
    
    def _initialize_calculator(self) -> ConfStateCalculator:
        """Initializes a ConfStateCalculator. The calculator is stored in a 
        private variable. If later another calculation is invoced without 
        changing calculation-relevant parameters, the same calculator will be 
        used.
        """
        # Generate hash for the current calculator settings
        calculator_hash = hash((
            self.get_param("load_model"),
            self.get_param("fit_model"),
            self.get_param("dump_model"),
            self.get_param("kde_bandwidth"),
            self.get_param("grid_points"),
            tuple(sorted(self.get_param("window"))),
            tuple(sorted(self.get_param("bootstrap"))),
            self.get_param("bootstrap_samples"),
            self.get_param("seed"),
            self.get_param("quick")))
        calculator_name = "Calculator({0})".format(hex(calculator_hash)[:8])
        # IF there is an already initialized calculator and the hashes match, 
        # use the old calculator
        if self._calculator is not None and self._calculator_hash == calculator_hash:
            logger.info(f"Constava:{calculator_name}: No change to settings; continue to use...")
            return self._calculator
        # Initialize PDF estimation method (for conformational state models)
        pdfestimator = self._initialize_pdfestimator()
        # Initialize ConfStateCalculator ...
        logger.info(f"Constava: Initializing {calculator_name}...")
        calculator = ConfStateCalculator(pdfestimator)
        # Adding  subsampling methods
        for window_size in self.get_param("window"):
            new_method = SubsamplingWindow(window_size)
            calculator.add_method(new_method)
            logger.debug(f"Constava:{calculator_name}: Add subsampling method: {new_method.getShortName()}")
        bootstrap_samples = self.get_param("bootstrap_samples")
        bootstrap_seed = self.get_param("seed")
        for sample_size in self.get_param("bootstrap"):
            new_method = SubsamplingBootstrap(sample_size, bootstrap_samples, seed=bootstrap_seed)
            calculator.add_method(new_method)
            logger.debug(f"Constava:{calculator_name}: Add subsampling method: {new_method.getShortName()}")
        return calculator

    def _initialize_pdfestimator(self):
        """Initializes PDF estimation method (for conformational state models)"""
        # Determine which estimator type is used
        PdfType = GridStatePdf if self.get_param("quick") else KDEStatePdf
        # Load model
        if self.get_param("load_model") is not None:
            model_source = self.get_param("load_model")
            logger.debug(f"Constava: Loading conformational state models from file: {model_source}")
            pdfestimator = PdfType.from_pickle(model_source)
        # OR fit model
        else:
            model_source = self.get_param("fit_model") or DEFAULT_TRAINING_DATA_PATH
            logger.debug(f"Constava: Fitting model to data in: {model_source}")
            pdfestimator = PdfType.from_fitting(
                model_source, bandwidth = self.get_param("kde_bandwidth"),
                degrees2radians = self.get_param("fit_degrees"))
        # Save PDF estimator if requested
        if self.get_param("dump_model"):
            model_dump_path = self.get_param("dump_model")
            logger.debug(f"Constava: Saving conformational state models to: {model_dump_path}")
            pdfestimator.dump_pickle(model_dump_path)
        return pdfestimator