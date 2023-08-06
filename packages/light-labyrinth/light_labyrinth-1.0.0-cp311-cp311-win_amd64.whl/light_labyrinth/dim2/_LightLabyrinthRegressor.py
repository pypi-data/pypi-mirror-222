from .._bare_model import LightLabyrinth
from .._tools import _LightLabyrinthOutputTransformer
from ..hyperparams.activation import *
from ..hyperparams.error_function import *
from ..hyperparams.optimization import *
from ..hyperparams.regularization import *
from ..hyperparams.weights_init import LightLabyrinthWeightsInit
from ..utils import LightLabyrinthVerbosityLevel


class LightLabyrinthRegressor(LightLabyrinth):
    """A 2-dimensional Light Labyrinth model.

        It is meant for regression.

        ```
            X
            |__ 
            |__|
            |__|
            |__|__ y
            |__ *
        ```

        An example of `height = 5` by `width = 2` model. The lower output is omitted. 

        Parameters
        ----------
        ----------
        height : int 
            Height of the Light Labyrinth. Note that `height > 1`.

        width : int
            Width of the Light Labyrinth. Note that `width > 1`.

        bias : bool, default=True
            Whether to use bias in each node.

        activation : `light_labyrinth.hyperparams.activation.ReflectiveIndexCalculator`, default=`light_labyrinth.hyperparams.activation.ReflectiveIndexCalculator.sigmoid_dot_product`
            Activation function applied to each node's output.

            -`sigmoid_dot_product` - logistic function over dot product of weights and input light for a given node.

        error : `light_labyrinth.hyperparams.error_function.ErrorCalculator`, default=`light_labyrinth.hyperparams.error_function.ErrorCalculator.mean_squared_error`
            Error function optimized during training.

            -`mean_squared_error` - Mean Squared Error can be used for any classification or regression task.

            -`cross_entropy` - Cross Entropy Loss is meant primarily for classification task but it can be used for regression as well.

            -`scaled_mean_squared_error` - Adaptation of MSE meant primarily for multi-label classification.
            \tOutput values of consecutive pairs of output nodes are scaled to add up to \\(\\frac{1}{k}\\), before applying MSE.

        optimizer : object, default=`light_labyrinth.hyperparams.optimization.GradientDescent(0.01)`
            Optimization algorithm. 

            -`light_labyrinth.hyperparams.optimization.GradientDescent` - Standard Gradient Descent with constant learning rate, default: learning_rate=0.01

            -`light_labyrinth.hyperparams.optimization.RMSprop` - RMSprop optimization algorithm, default: learning_rate=0.01, rho=0.9, momentum=0.0, epsilon=1e-6

            -`light_labyrinth.hyperparams.optimization.Adam` - Adam optimization algorithm, default: learning_rate=0.01, beta1=0.9, beta2=0.999, epsilon=1e-6

            -`light_labyrinth.hyperparams.optimization.Nadam` - Adam with Nesterov momentum, default: learning_rate=0.01, beta1=0.9, beta2=0.999, epsilon=1e-6


        regularization : object, default=`light_labyrinth.hyperparams.regularization.RegularizationL1(0.01)`
            Regularization technique - either L1, L2, or None.

            `light_labyrinth.hyperparams.regularization.RegularizationNone` - No regularization.

            `light_labyrinth.hyperparams.regularization.RegularizationL1` - L1 regularization: \\(\\lambda\\sum|W|\\), default: lambda_factor=0.01

            `light_labyrinth.hyperparams.regularization.RegularizationL2` - L2 regularization: \\(\\frac{\\lambda}{2}\\sum||W||\\), default: lambda_factor=0.01

        weights: ndarray, optional, default=None
            Initial weights. If `None`, weights are set according to weights_init parameter.

        weights_init: `light_labyrinth.hyperparams.weights_init.LightLabyrinthWeightsInit`, default=`light_labyrinth.hyperparams.weights_init.LightLabyrinthWeightsInit.Default`
            Method for weights initialization.

            -`light_labyrinth.hyperparams.weights_init.LightLabyrinthWeightsInit.Default` - default initialization.

            -`light_labyrinth.hyperparams.weights_init.LightLabyrinthWeightsInit.Random` - weights are initialized randomly.

            -`light_labyrinth.hyperparams.weights_init.LightLabyrinthWeightsInit.Zeros` - weights are initialized with zeros.

        random_state: int, optional, default=0
            Initial random state. If 0, initial random state will be set randomly.

        Attributes
        ----------
        ----------
        height : int
            Height of the LightLabyrinth.

        width : int
            Width of the LightLabyrinth.

        trainable_params : int
            Number of trainable parameters.

        weights : ndarray of shape (height-1, width-1, n_features + bias)
            Array of weights optimized during training. If bias is set to False, n_features is equal to the number of features in the training set X.
            If bias is set to True, n_features is increased by 1.

        history : `light_labyrinth.utils.LightLabyrinthLearningHistory`
            Learning history including error on training and (if provided) validation sets.

        bias : bool
            Boolean value whether the model was trained with bias.

        activation : `light_labyrinth.hyperparams.activation.ReflectiveIndexCalculator`
            Activation function used for training.

        error_function : `light_labyrinth.hyperparams.error_function.ErrorCalculator`
            Error function used for training.

        optimizer : object
            Optimization algorithm used for training, including its parameters.

        regularization : object
            Regularization used during training, including its parameters.

        random_state : int
            Random state passed during initialization.

        Notes
        -----
        -----
        LightLabyrinth trains iteratively since at each time step
        the partial derivatives of the loss function with respect to the model
        parameters are computed to update the weights.

        It can also have a regularization term added to the loss function
        that shrinks model parameters to prevent overfitting.

        This implementation works with data represented as dense numpy arrays
        of floating point values.


        See Also
        --------
        light_labyrinth.dim2.LightLabyrinthDynamicRegressor : 2-dimensional Light Labyrinth regressor trained with dynamic algorithm.
        light_labyrinth.dim2.LightLabyrinthRandomRegressor : 2-dimensional randomized Light Labyrinth regressor.
        light_labyrinth.dim2.LightLabyrinthClassifier : 2-dimensional Light Labyrinth classifier.

        Examples
        --------
        >>> from light_labyrinth.dim2 import LightLabyrinthRegressor
        >>> from light_labyrinth.hyperparams.weights_init import LightLabyrinthWeightsInit
        >>> from light_labyrinth.hyperparams.regularization import RegularizationNone
        >>> from light_labyrinth.hyperparams.optimization import GradientDescent
        >>> from sklearn.datasets import make_regression
        >>> from sklearn.model_selection import train_test_split
        >>> from sklearn.metrics import r2_score
        >>> X, y = make_regression(n_samples=1000)
        >>> y = y.reshape(-1,1)
        >>> X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)
        >>> clf = LightLabyrinthRegressor(height=4, width=6,
        ...                            error=ErrorCalculator.mean_squared_error,
        ...                            optimizer=GradientDescent(1.5),
        ...                            regularization=RegularizationNone(),
        ...                            weights_init=LightLabyrinthWeightsInit.Zeros)
        >>> hist = clf.fit(X_train, y_train, epochs=20, batch_size=30)
        >>> y_pred = clf.predict(X_test)
        >>> r2_score(y_test, y_pred)
        0.99
        """

    def __init__(self, height, width, bias=True,
                 activation=ReflectiveIndexCalculator.sigmoid_dot_product,
                 error=ErrorCalculator.mean_squared_error,
                 optimizer=None,
                 regularization=None,
                 weights=None,
                 weights_init=LightLabyrinthWeightsInit.Default,
                 random_state=0):
        super().__init__(height, width, bias,
                         activation,
                         error,
                         optimizer,
                         regularization,
                         weights,
                         weights_init,
                         random_state)

    def fit(self, X, y, epochs, batch_size=1.0, stop_change=1e-4, n_iter_check=0, epoch_check=1, X_val=None, y_val=None, verbosity=LightLabyrinthVerbosityLevel.Nothing):
        """Fit the model to data matrix X and target(s) y.

        Parameters
        ----------
        ----------
        X : ndarray of shape (n_samples, n_features)
            The input data.

        y : ndarray of shape (n_samples, 1)
            The target values.

        epochs : int
            Number of iterations to be performed. The solver iterates until convergence
            (determined by `stop_change`, `n_iter_check`) or this number of iterations.

        batch_size : int or float, default=1.0
            Size of mini-batches for stochastic optimizers given either as portion of 
            samples (float) or the exact number (int).
            When type is float, `batch_size = max(1, int(batch_size * n_samples))`.

        stop_change : float, default=1e-4
            Tolerance for the optimization. When the loss or score is not improving
            by at least ``stop_change`` for ``n_iter_check`` consecutive iterations,
            convergence is considered to be reached and training stops.

        n_iter_check : int, default=0
            Maximum number of epochs to not meet ``stop_change`` improvement.
            When set to 0, exactly ``epochs`` iterations will be performed.

        epoch_check : int, default=1
            Determines how often the condition for convergence is checked.
            `epoch_check = i` means that the condition will be checked every i-th iteration.
            When set to 0 the condition will not be checked at all and the learning history will be empty.

        X_val : ndarray of shape (n_val_samples, n_features), default=None
            The validation data. 
            If `X_val` is given, `y_val` must be given as well.

        y_val : ndarray of shape (n_val_samples, 1), default=None
            Target values of the validation set. 
            If `y_val` is given, `X_val` must be given as well.

        verbosity: `light_labyrinth.utils.LightLabyrinthVerbosityLevel`, default=`light_labyrinth.utils.LightLabyrinthVerbosityLevel.Nothing`
            Verbosity level.

            -`light_labyrinth.utils.LightLabyrinthVerbosityLevel.Nothing` - No output is printed.

            -`light_labyrinth.utils.LightLabyrinthVerbosityLevel.Basic` - Display logs about important events during the learning process. 

            -`light_labyrinth.utils.LightLabyrinthVerbosityLevel.Full` - Detailed output from the learning process is displayed.

        Returns
        -------
        -------
        hist : object
            Returns a `light_labyrinth.utils.LightLabyrinthLearningHistory` object with fields: 
            errs_train, errs_val.
        """
        self._encoder = _LightLabyrinthOutputTransformer()
        y_transformed = self._encoder.fit_transform(y)
        y_val_transformed = self._encoder.transform(
            y_val) if y_val is not None else None
            
        return super().fit(X, y_transformed, epochs, batch_size, stop_change, n_iter_check, epoch_check, X_val, y_val_transformed, verbosity)

    def predict(self, X):
        """Predict using the Light Labyrinth regressor.

        Parameters
        ----------
        ----------
        X : ndarray of shape (n_samples, n_features)
            The input data.

        Returns
        -------
        -------
        y : ndarray of shape (n_samples, 1)
            The predicted values.
        """
        y_pred = super().predict(X)
        return self._encoder.inverse_transform(y_pred)

    def __del__(self):
        super().__del__()
